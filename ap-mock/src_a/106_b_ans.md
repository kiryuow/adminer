---
no: 問6
title: データベース 解答例・採点基準
lead: 図書館の貸出管理システム
---

<table><tr><th style='width:11%'>設問</th><th style='width:38%'>解答例</th><th>採点のポイント</th><th style='width:7%'>配点</th></tr><tr><td>設問1</td><td>書誌：資料＝1対多（業務ルール(2)）</td><td>・1対多<br>・根拠(2)</td><td style='text-align:center'>4</td></tr><tr><td>設問2</td><td>a：返却日 IS NULL　b：HAVING　c：資料.ISBN = 書誌.ISBN</td><td>・a 返却日 IS NULL（＝ NULL は誤り）<br>・b HAVING<br>・c ISBNで結合</td><td style='text-align:center'>9</td></tr><tr><td>設問3</td><td>書名を変更する際に複数行を更新する必要があり、不整合が生じるおそれがある</td><td>・冗長なデータによる更新時異状<br>・不整合</td><td style='text-align:center'>4</td></tr><tr><td>設問4</td><td>前者</td><td>・貸出中冊数を利用者ごとに数えるSQL</td><td style='text-align:center'>3</td></tr><tr><td colspan='3' style='text-align:right'>合計</td><td style='text-align:center'>20</td></tr></table>

:::note 解説
NULL の判定は IS NULL。集約関数の条件は HAVING。結合条件は外部キーと参照先の主キーを等号で結ぶ。
:::

<p>自己採点：　　　　点 ／ 20点</p>
