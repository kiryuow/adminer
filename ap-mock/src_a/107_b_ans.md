---
no: 問7
title: 組込みシステム開発 解答例・採点基準
lead: 自動給水装置の設計
---

<table><tr><th style='width:11%'>設問</th><th style='width:38%'>解答例</th><th>採点のポイント</th><th style='width:7%'>配点</th></tr><tr><td>設問1</td><td>a：給水　b：休止　c：異常</td><td>・a 測定値＜しきい値→給水<br>・b 給水完了→休止<br>・c 水位空→異常</td><td style='text-align:center'>6</td></tr><tr><td>設問2</td><td>計測 240秒、給水 20秒</td><td>・48回×5秒＝240秒<br>・2回×10秒＝20秒</td><td style='text-align:center'>4</td></tr><tr><td>設問3</td><td>0.11mA</td><td>・(15×240＋200×20＋0.02×86,140)÷86,400≒0.108</td><td style='text-align:center'>6</td></tr><tr><td>設問4</td><td>水がない状態でポンプを空運転させないため</td><td>・空運転（故障）の防止</td><td style='text-align:center'>4</td></tr><tr><td colspan='3' style='text-align:right'>合計</td><td style='text-align:center'>20</td></tr></table>

:::note 解説
消費電流量（mA・秒）を状態ごとに足して、1日の秒数で割る。15×240＝3,600、200×20＝4,000、0.02×86,140≒1,723、合計9,323÷86,400≒0.108。
:::

<p>自己採点：　　　　点 ／ 20点</p>
