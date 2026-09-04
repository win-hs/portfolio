# -*- coding: utf-8 -*-
"""Obsidian -> Jekyll 同步。
讀 vault 的課程資料夾，產生 _lessons/*.md 與 assets/img/lessons/*。
產出全部重建，repo 那兩個位置請勿手改。
"""
import os, re, sys, shutil, yaml

VAULT = r"E:\8_Obsidian\Obsidian\QGIS課程"
ATT   = os.path.join(VAULT, "attachments")
REPO  = r"E:\9_ClaudeSpace\github.io\Portfolio"
OUT   = os.path.join(REPO, "_lessons")
IMG   = os.path.join(REPO, "assets", "img", "lessons")

def slugify(title):
    s = re.sub(r"\s+", "-", title.strip())
    s = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff\-]", "", s)
    return re.sub(r"-{2,}", "-", s).strip("-").lower()

# ---- 讀入全部課程，先建 檔名 -> slug 對照供 wikilink 解析 ----
lessons = []
for fn in sorted(os.listdir(VAULT)):
    if not fn.endswith(".md"):
        continue
    txt = open(os.path.join(VAULT, fn), encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    if not m:
        sys.exit("缺 front matter: " + fn)
    fm = yaml.safe_load(m.group(1))
    lessons.append(dict(stem=os.path.splitext(fn)[0], fm=fm,
                        body=txt[m.end():], slug=slugify(fm["title"])))

by_stem = {l["stem"]: l for l in lessons}
dupes = [s for s in {l["slug"] for l in lessons} if [x["slug"] for x in lessons].count(s) > 1]
if dupes:
    sys.exit("slug 重複: %s" % dupes)

for d in (OUT, IMG):
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d)

CALLOUT = re.compile(r"^>\s*\[!(\w+)\]([-+]?)\s*(.*)$")
stats = dict(imgs=0, details=0, callouts=0, links=0, missing=[])

def convert(les):
    src = les["body"]

    # 1. 圖片嵌入：![[x.png]] / ![[x.png|300]]
    def img(m):
        name = m.group(1).split("|")[0].strip()
        srcp = os.path.join(ATT, name)
        if not os.path.exists(srcp):
            stats["missing"].append("%s -> %s" % (les["stem"], name)); return m.group(0)
        shutil.copy(srcp, os.path.join(IMG, name))
        stats["imgs"] += 1
        return "![]({{ site.baseurl }}/assets/img/lessons/%s)" % name
    src = re.sub(r"!\[\[([^\]]+)\]\]", img, src)

    # 2. 課程間 wikilink：[[stem]] / [[stem|標籤]]
    def link(m):
        parts = m.group(1).split("|")
        tgt = by_stem.get(parts[0].strip())
        if not tgt:
            stats["missing"].append("%s -> [[%s]]" % (les["stem"], parts[0])); return m.group(0)
        label = parts[1].strip() if len(parts) > 1 else tgt["fm"]["title"]
        stats["links"] += 1
        return "[%s]({{ site.baseurl }}/qgis/%s/)" % (label, tgt["slug"])
    src = re.sub(r"(?<!!)\[\[([^\]]+)\]\]", link, src)

    # 3. 標題去掉開頭編號（順序由 front matter 的 order 決定）
    src = re.sub(r"^#\s+\d+\.\s*", "# ", src, count=1, flags=re.M)

    # 4. Obsidian callout -> <details> / .callout
    out, lines, i = [], src.split("\n"), 0
    while i < len(lines):
        m = CALLOUT.match(lines[i])
        if not m:
            out.append(lines[i]); i += 1; continue
        kind, fold, title = m.group(1).lower(), m.group(2), m.group(3).strip()
        body, i = [], i + 1
        while i < len(lines) and lines[i].startswith(">"):
            body.append(re.sub(r"^>\s?", "", lines[i])); i += 1
        if fold == "-":
            out += ["", '<details markdown="1">', "<summary>%s</summary>" % title, ""]
            out += body
            out += ["", "</details>", ""]
            stats["details"] += 1
        else:
            out += ["", '<div class="callout" markdown="1">', ""]
            if title: out.append("**%s**" % title)
            out += body
            out += ["", "</div>", ""]
            stats["callouts"] += 1
    return "\n".join(out).strip() + "\n"

for les in lessons:
    fm = dict(layout="lesson", theme="dark", title=les["fm"]["title"], unit=les["fm"]["unit"],
              order=les["fm"]["order"], permalink="/qgis/%s/" % les["slug"],
              hackmd=les["fm"]["hackmd"])
    txt = "---\n" + yaml.dump(fm, allow_unicode=True, sort_keys=False) + "---\n\n" + convert(les)
    open(os.path.join(OUT, les["slug"] + ".md"), "w", encoding="utf-8", newline="\n").write(txt)

print("lessons  :", len(lessons))
print("images   :", stats["imgs"])
print("details  :", stats["details"], "(摺疊區塊)")
print("callouts :", stats["callouts"])
print("內部連結 :", stats["links"])
print("缺漏     :", stats["missing"] or "無")
