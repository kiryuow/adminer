#!/usr/bin/env python3
"""questions/*.js を app.html に埋め込んで dist/index.html を作る"""
import pathlib
root = pathlib.Path(__file__).resolve().parent
qs = "\n".join(p.read_text(encoding="utf-8") for p in sorted((root / "questions").glob("*.js")))
html = (root / "app.html").read_text(encoding="utf-8").replace("/*__QUESTIONS__*/", qs)
(root / "dist").mkdir(exist_ok=True)
(root / "dist" / "index.html").write_text(html, encoding="utf-8")
print("built dist/index.html", len(html.encode()), "bytes")
