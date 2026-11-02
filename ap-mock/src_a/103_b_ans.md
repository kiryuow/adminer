---
no: 問3
title: プログラミング 解答例・採点基準
lead: 在庫データの区間集計（累積和）
---

<table><tr><th style='width:11%'>設問</th><th style='width:38%'>解答例</th><th>採点のポイント</th><th style='width:7%'>配点</th></tr><tr><td>設問1</td><td>acc[i − 1] ＋ ship[i]</td><td>・直前の累積和に当日の出荷数を足す</td><td style='text-align:center'>5</td></tr><tr><td>設問2</td><td>acc[t] − acc[s − 1]</td><td>・acc[t]からacc[s−1]を引く<br>・s−1 の境界を正しく扱っている</td><td style='text-align:center'>5</td></tr><tr><td>設問3</td><td>13</td><td>・acc[4]−acc[1]＝18−5＝13</td><td style='text-align:center'>4</td></tr><tr><td>設問4</td><td>単純な方法：O(nq)　累積和の方法：O(n＋q)</td><td>・単純な方法 O(nq)<br>・累積和 O(n＋q)（作成O(n)＋問合せO(1)×q）</td><td style='text-align:center'>6</td></tr><tr><td colspan='3' style='text-align:right'>合計</td><td style='text-align:center'>20</td></tr></table>

:::note 解説
設問2の境界：s 日目を含めるために acc[s−1] を引く。acc[s] を引くと s 日目が抜ける（採点講評で頻出の「境界値の誤り」）。
:::

<p>自己採点：　　　　点 ／ 20点</p>
