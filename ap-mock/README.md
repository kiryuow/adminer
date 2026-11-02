# 応用情報技術者試験 本番想定 模擬試験

科目A 80問（四肢択一・150分）と科目B 11問（問1必須＋4問選択・記述式・150分）のオリジナル模擬試験。

- 問題冊子: [`dist/ap-mock-questions.pdf`](dist/ap-mock-questions.pdf)
- 解答・解説: [`dist/ap-mock-answers.pdf`](dist/ap-mock-answers.pdf)
- Web版（CBT想定）: `dist/index.html` ／ https://claude.ai/artifact/H4VoRHjbxaBUXs3vJs8Vji

データは `data/*.js`（a=科目A、b=科目B）。`python3 gen.py` で mock.json・PDF原稿・Web版を生成し、
`SRC=src_q OUT=ap-mock-questions COVER=cover_q.html python3 build_pdf.py`（解答は src_a / cover_a.html）でPDFを作る。
