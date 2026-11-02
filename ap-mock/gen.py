#!/usr/bin/env python3
"""data/*.js（模擬試験データ）から mock.json と、PDF用の原稿（src_q / src_a）を生成する"""
import json, pathlib, random, subprocess, html, re, shutil
ROOT = pathlib.Path(__file__).resolve().parent
js = "global.A=[];global.B=[];const fs=require('fs');for(const f of fs.readdirSync('data').sort())eval(fs.readFileSync('data/'+f,'utf8'));console.log(JSON.stringify({A,B}))"
data = json.loads(subprocess.run(["node", "-e", js], cwd=ROOT, capture_output=True, text=True, check=True).stdout)
KANA = "アイウエ"

A = sorted(data["A"], key=lambda q: q["n"])
for q in A:                                   # 選択肢の並びを固定シードで決める（正解が偏らないように）
    perm = list(range(4)); random.Random(q["n"] * 7919 + 11).shuffle(perm)
    q["o"] = [q["o"][i] for i in perm]; q["a"] = perm.index(0)
B = sorted(data["B"], key=lambda p: p["n"])
assert [q["n"] for q in A] == list(range(1, 81)), "科目Aの問番号が1〜80になっていない"
assert [p["n"] for p in B] == list(range(1, 12)), "科目Bの問番号が1〜11になっていない"
for p in B: assert sum(x["s"] for x in p["qs"]) == 20, f"問{p['n']}の配点合計が20点でない"
(ROOT / "dist").mkdir(exist_ok=True)
(ROOT / "dist" / "mock.json").write_text(json.dumps({"A": A, "B": B}, ensure_ascii=False), encoding="utf-8")
print("answer distribution:", {k: sum(1 for q in A if q["a"] == i) for i, k in enumerate(KANA)})

def inl(s):                                    # 本文中の **強調** と改行をHTMLに
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return s.replace("\n", "<br>")
def table(rows, cap=""):
    h = "<table>" + (f"<caption style='caption-side:top;text-align:left;font-weight:700;color:#173a63'>{html.escape(cap)}</caption>" if cap else "")
    h += "<tr>" + "".join(f"<th>{inl(c)}</th>" for c in rows[0]) + "</tr>"
    for r in rows[1:]: h += "<tr>" + "".join(f"<td>{inl(c)}</td>" for c in r) + "</tr>"
    return h + "</table>"
def body(blocks):
    out = []
    for b in blocks:
        if "h" in b: out.append(f"<h4>{inl(b['h'])}</h4>")
        elif "p" in b: out.append(f"<p>{inl(b['p'])}</p>")
        elif "tb" in b: out.append(table(b["tb"], b.get("cap", "")))
        elif "pre" in b: out.append(f"<pre>{html.escape(b['pre'])}</pre>")
    return "\n".join(out)
def front(no, title, lead): return f"---\nno: {no}\ntitle: {title}\nlead: {lead}\n---\n\n"
def write(d, name, text):
    (d / name).write_text(text, encoding="utf-8")

# ---------- 問題冊子 ----------
SQ = ROOT / "src_q"; shutil.rmtree(SQ, ignore_errors=True); SQ.mkdir()
write(SQ, "00_guide.md", front("", "受験上の注意", "試験時間・出題数・解答方法・合格基準") + """
この模擬試験は、応用情報技術者試験の出題形式・配分・時間に合わせて作成した **オリジナル問題** です（IPAの過去問題の問題文ではありません）。本番と同じ条件で解き、別冊の「解答・解説」で採点してください。

| 科目 | 試験時間 | 出題数・解答数 | 出題形式 | 合格基準 |
|---|---|---|---|---|
| 科目A（旧 午前） | 150分 | 80問すべて解答 | 多肢選択式（四肢択一） | 100点満点中60点以上 |
| 科目B（旧 午後） | 150分 | 11問中、問1（必須）＋問2〜問11から4問を選択 | 記述式 | 100点満点中60点以上 |

- 科目Aは1問1.25点です。巻末の解答用紙に、ア〜エのいずれかを記入してください。
- 科目Bは1問20点です。選択した問題の番号を解答用紙の選択欄に記入してください（5問以上選択した場合は、はじめの4問を採点の対象とします）。
- 字数の指定がある設問は、句読点も1字に数えます。
- 本番（2026年度CBT方式）では、科目Aと科目Bは別の日に実施されます。この模擬試験でも、できれば別の日に、時間を計って解いてください。

:::point おすすめの使い方
科目A：時計を150分にセットし、1周目は迷った問題に印を付けて先へ進む → 2周目で印の問題を見直す。科目B：最初の5分で選択する4問を決めてから解き始める。
:::
""")
qa = front("科目A", "科目A 問題（問1〜問80）", "試験時間150分・80問すべて解答・四肢択一") + "<p class='muted'>次の各問に対する解答を、解答群の中から一つ選べ。</p>\n"
for q in A:
    if q["n"] == 51: qa += "\n<p class='muted' style='margin-top:14px'>── 問51〜問60 はマネジメント系、問61〜問80 はストラテジ系の問題です ──</p>\n"
    qa += f"<div class='mq'><span class='qn'>問{q['n']}</span>　{inl(q['q'])}<ol>" + "".join(f"<li>{KANA[i]}　{inl(o)}</li>" for i, o in enumerate(q["o"])) + "</ol></div>\n"
write(SQ, "01_a.md", qa)
grid = "<table class='ansgrid'><tr>" + "<th>問</th><th>解答</th>" * 4 + "</tr>"
for r in range(1, 21):
    grid += "<tr>" + "".join(f"<td>{r + 20*c}</td><td></td>" for c in range(4)) + "</tr>"
grid += "</table>"
write(SQ, "02_a_sheet.md", front("科目A", "科目A 解答用紙", "ア〜エを記入する") + grid + "\n\n<p>正解数：　　　　問 ／ 80問　　得点（正解数×1.25）：　　　　点</p>\n")
for p in B:
    req = "必須" if p.get("req") else "選択"
    t = front(f"問{p['n']}", f"{p['f']}（{req}）", p["title"])
    t += f"<p><b>{inl(p['title'])}に関する次の記述を読んで、設問に答えよ。</b></p>\n<div class='bcase'>\n{body(p['body'])}\n</div>\n\n"
    for x in p["qs"]:
        t += f"<div class='bq'><b>{inl(x['l'])}</b>　{inl(x['q'])}</div>\n"
    write(SQ, f"1{p['n']:02d}_b.md", t)
sheet = front("科目B", "科目B 解答用紙", "選択した問題の番号を記入し、設問ごとに解答を書く")
sheet += "<p>選択欄（問1は必須）：　問1 ／ 問＿＿ ／ 問＿＿ ／ 問＿＿ ／ 問＿＿</p>\n"
for i in range(5):
    sheet += f"<h3>選択{i+1}　問＿＿</h3><div class='write l'></div>\n"
write(SQ, "199_b_sheet.md", sheet)

# ---------- 解答・解説 ----------
SA = ROOT / "src_a"; shutil.rmtree(SA, ignore_errors=True); SA.mkdir()
g = "<table class='ansgrid'><tr>" + "<th>問</th><th>正解</th>" * 4 + "</tr>"
for r in range(1, 21):
    g += "<tr>" + "".join(f"<td>{r + 20*c}</td><td><b>{KANA[A[r + 20*c - 1]['a']]}</b></td>" for c in range(4)) + "</tr>"
g += "</table>"
write(SA, "00_a_key.md", front("科目A", "科目A 正解一覧と採点", "正解数×1.25点。48問以上で60点（合格基準）") + g + """

| 系 | 問題番号 | 問題数 | 正解数 | 目標 |
|---|---|---|---|---|
| テクノロジ系 | 問1〜問50 | 50 | | 32問以上 |
| マネジメント系 | 問51〜問60 | 10 | | 7問以上 |
| ストラテジ系 | 問61〜問80 | 20 | | 13問以上 |
| 合計 | | 80 | | 48問以上で合格基準 |
""")
ex = front("科目A", "科目A 解説", "各問の正解と考え方。学習ノートの対応章を示す")
for q in A:
    ex += f"<div class='mq'><span class='qn'>問{q['n']}　正解 {KANA[q['a']]}</span>　<span class='muted'>（{html.escape(q['c'])}／学習ノート 第{q['r']}章）</span><br>{inl(q['e'])}</div>\n"
write(SA, "01_a_expl.md", ex)
for p in B:
    t = front(f"問{p['n']}", f"{p['f']} 解答例・採点基準", p["title"])
    t += "<table><tr><th style='width:11%'>設問</th><th style='width:38%'>解答例</th><th>採点のポイント</th><th style='width:7%'>配点</th></tr>"
    for x in p["qs"]:
        t += f"<tr><td>{inl(x['l'])}</td><td>{inl(x['a'])}</td><td>{'<br>'.join('・' + inl(k) for k in x['k'])}</td><td style='text-align:center'>{x['s']}</td></tr>"
    t += "<tr><td colspan='3' style='text-align:right'>合計</td><td style='text-align:center'>20</td></tr></table>\n\n"
    if p.get("note"): t += f":::note 解説\n{p['note']}\n:::\n\n"
    t += "<p>自己採点：　　　　点 ／ 20点</p>\n"
    write(SA, f"1{p['n']:02d}_b_ans.md", t)
write(SA, "199_score.md", front("採点", "得点の集計と振り返り", "科目A・科目Bの得点と、次にやること") + """
| 科目 | 得点 | 合格基準 | 判定 |
|---|---|---|---|
| 科目A | 　　点（正解数　　×1.25） | 60点 | |
| 科目B | 　　点（問1：　　＋選択4問：　　） | 60点 | |

:::how 得点別の次の一手
**科目Aが60点未満**：正解数が少なかった系の章を学習ノートで読み直し、午前クイズアプリの「分野別演習」で弱点分野を繰り返す。
**科目Bが60点未満**：間違えた設問を午後対策シートの「間違えた理由の分類（A〜F）」で分類し、最も多い分類の対策から取り組む。
**両方60点以上**：IPAの最新の過去問題で、同じ条件で解いて得点が安定するか確認する。
:::
""")
print("generated src_q / src_a")

# ---------- Web版（CBT想定） ----------
app = (ROOT / "app.html").read_text(encoding="utf-8").replace("/*__MOCK__*/null", json.dumps({"A": A, "B": B}, ensure_ascii=False))
(ROOT / "dist" / "index.html").write_text(app, encoding="utf-8")
print("built dist/index.html")
