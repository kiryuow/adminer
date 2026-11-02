#!/usr/bin/env python3
"""応用情報技術者試験 学習ノート ビルドスクリプト

src/*.md（独自のボックス記法つき Markdown）→ HTML → PDF（Chromium / Playwright）

使い方:  python3 build.py
出力:    dist/ap-pm-guide.html, dist/ap-pm-guide.pdf
"""
import html
import json
import pathlib
import re
import subprocess
import sys

import markdown

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
BOOK_TITLE = "応用情報技術者試験 午後（科目B）攻略本"

BOX_LABELS = {
    "point": "ポイント",
    "calc": "計算例",
    "note": "用語メモ",
    "exam": "過去問ではこう出る",
    "trap": "ひっかけ注意",
    "how": "解き方の型",
    "sum": "この章のまとめ",
}


def parse_front(text):
    meta = {}
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip()
        text = text[m.end():]
    return meta, text


def convert_boxes(text):
    """:::type タイトル ... ::: をHTMLのボックスに変換（入れ子不可）"""
    out, buf, kind, title = [], None, None, ""
    for line in text.splitlines():
        m = re.match(r"^:::(\w+)\s*(.*)$", line)
        if buf is None and m:
            kind, title, buf = m.group(1), m.group(2), []
            continue
        if buf is not None and line.strip() == ":::":
            label = BOX_LABELS.get(kind, kind)
            head = f'<span class="box-l">{label}</span>' + (
                f'<span class="box-t">{html.escape(title)}</span>' if title else "")
            out.append(f'\n<div class="box box-{kind}" markdown="1">\n<div class="box-h">{head}</div>\n')
            out.extend(buf)
            out.append("\n</div>\n")
            buf = None
            continue
        (buf if buf is not None else out).append(line)
    if buf is not None:
        raise ValueError("unterminated box: " + kind)
    return "\n".join(out)


def mark_long_tables(h):
    """行数の多い表はページをまたいで分割できるようにする（用語集など）"""
    def f(m):
        t = m.group(0)
        return t.replace("<table>", '<table class="long">', 1) if t.count("<tr>") > 14 else t
    return re.sub(r"(?s)<table>.*?</table>", f, h)


def md_to_html(text):
    return mark_long_tables(markdown.markdown(
        convert_boxes(text),
        extensions=["tables", "fenced_code", "md_in_html", "attr_list", "sane_lists", "nl2br"],
    ))


def build_html(page_map=None):
    chapters = []
    for f in sorted(SRC.glob("*.md")):
        meta, body = parse_front(f.read_text(encoding="utf-8"))
        chapters.append((f.stem, meta, md_to_html(body)))

    css = (ROOT / "style.css").read_text(encoding="utf-8")
    parts = [f"<!doctype html><html lang='ja'><head><meta charset='utf-8'><title>{BOOK_TITLE}</title><style>{css}</style></head><body>"]
    parts.append((ROOT / "cover.html").read_text(encoding="utf-8"))

    # 目次
    rows = []
    for cid, meta, _ in chapters:
        no = meta.get("no", "")
        label = f"{no}　{meta.get('title','')}" if no else meta.get("title", "")
        pg = (page_map or {}).get(cid, "")
        rows.append(
            f"<tr><td class='toc-c'>{html.escape(label)}</td>"
            f"<td class='toc-l'>{html.escape(meta.get('lead',''))}</td>"
            f"<td class='toc-p'>{pg}</td></tr>")
    parts.append("<section class='toc'><h2 class='plain'>目次</h2><table class='toc-t'>" + "".join(rows) + "</table></section>")

    for cid, meta, body in chapters:
        no, title = meta.get("no", ""), meta.get("title", "")
        if no:
            banner = f"<div class='ch-banner'><span class='ch-no'>{no}</span><span class='ch-title'>{html.escape(title)}</span></div>"
        else:
            banner = f"<div class='ch-banner plain-banner'><span class='ch-title'>{html.escape(title)}</span></div>"
        parts.append(f"<section class='chapter' id='{cid}'><span class='mark'>CHMARK{cid.replace('_','')}END</span>{banner}{body}</section>")
    parts.append("</body></html>")
    return "".join(parts), [c[0] for c in chapters], {c[0]: c[1] for c in chapters}


PDF_JS = r"""
const { chromium } = require('playwright');
(async () => {
  const [src, out, title] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + src, { waitUntil: 'networkidle' });
  await page.pdf({
    path: out, format: 'A4', printBackground: true,
    margin: { top: '20mm', bottom: '18mm', left: '16mm', right: '16mm' },
    displayHeaderFooter: true,
    headerTemplate: `<div style="width:100%;font-size:7.5px;color:#8a94a6;padding:0 16mm;font-family:'Noto Sans CJK JP';"><div style="text-align:right;border-bottom:0.5px solid #d5dbe5;padding-bottom:3px;">${title}</div></div>`,
    footerTemplate: `<div style="width:100%;text-align:center;font-size:8px;color:#5b7fb5;font-family:'Noto Sans CJK JP';">- <span class="pageNumber"></span> -</div>`,
  });
  await browser.close();
})();
"""


def render_pdf(html_path, pdf_path):
    js = DIST / "_render.js"
    js.write_text(PDF_JS, encoding="utf-8")
    subprocess.run(["node", str(js), str(html_path), str(pdf_path), BOOK_TITLE], check=True)
    js.unlink()


def find_pages(pdf_path, ids, metas):
    """各章のバナーが載っているページ番号を探す（目次のページ番号用）"""
    txt = subprocess.run(["pdftotext", "-layout", str(pdf_path), "-"], capture_output=True, text=True).stdout
    pages = txt.split("\f")
    result = {}
    for cid in ids:
        key = "CHMARK" + cid.replace("_", "") + "END"
        for i, pg in enumerate(pages):
            if key in pg.replace(" ", ""):
                result[cid] = i + 1
                break
    return result


def main():
    DIST.mkdir(exist_ok=True)
    html_path = DIST / "ap-pm-guide.html"
    pdf_path = DIST / "ap-pm-guide.pdf"
    doc, ids, metas = build_html()
    html_path.write_text(doc, encoding="utf-8")
    render_pdf(html_path, pdf_path)
    pages = find_pages(pdf_path, ids, metas)
    doc, _, _ = build_html(pages)
    html_path.write_text(doc, encoding="utf-8")
    render_pdf(html_path, pdf_path)
    print(json.dumps(pages, ensure_ascii=False))
    print("built:", pdf_path)


if __name__ == "__main__":
    sys.exit(main())
