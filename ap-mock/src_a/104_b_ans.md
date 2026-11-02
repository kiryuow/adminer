---
no: 問4
title: システムアーキテクチャ 解答例・採点基準
lead: Webサービスのクラウド移行と性能設計
---

<table><tr><th style='width:11%'>設問</th><th style='width:38%'>解答例</th><th>採点のポイント</th><th style='width:7%'>配点</th></tr><tr><td>設問1</td><td>Webサーバ 60%、DBサーバ 48%</td><td>・120×5ms＝600ms→60%<br>・120×4ms＝480ms→48%</td><td style='text-align:center'>4</td></tr><tr><td>設問2</td><td>2台</td><td>・240×5ms＝1,200ms＝120%<br>・120÷60＝2台</td><td style='text-align:center'>4</td></tr><tr><td>設問3</td><td>オートスケール（スケールアウト／スケールインの自動化）</td><td>・オートスケール</td><td style='text-align:center'>3</td></tr><tr><td>設問4</td><td>0.989</td><td>・Web部分 1−0.01²＝0.9999<br>・0.999×0.9999×0.99≒0.9889</td><td style='text-align:center'>5</td></tr><tr><td>設問5</td><td>DBサーバを冗長化して2台構成にする</td><td>・DBサーバ（単一障害点）の冗長化</td><td style='text-align:center'>4</td></tr><tr><td colspan='3' style='text-align:right'>合計</td><td style='text-align:center'>20</td></tr></table>

:::note 解説
CPU使用率＝処理件数×1件のCPU時間。設問4は 0.999×0.9999×0.99＝0.98891… 単一障害点（DB）を冗長化すると最も効果が大きい。
:::

<p>自己採点：　　　　点 ／ 20点</p>
