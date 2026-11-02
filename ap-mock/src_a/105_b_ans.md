---
no: 問5
title: ネットワーク 解答例・採点基準
lead: 本社と営業所を結ぶネットワークの再構築
---

<table><tr><th style='width:11%'>設問</th><th style='width:38%'>解答例</th><th>採点のポイント</th><th style='width:7%'>配点</th></tr><tr><td>設問1</td><td>192.168.2.1</td><td>・営業所ルータのLAN側アドレス</td><td style='text-align:center'>3</td></tr><tr><td>設問2</td><td>PC1から営業所ルータまでの通信は正常であること</td><td>・PC1〜営業所ルータ間（営業所LAN内）が正常</td><td style='text-align:center'>4</td></tr><tr><td>設問3</td><td>暗号化されたトンネルで転送されず、本社に届かない</td><td>・トンネル（IPsec）で転送されない<br>・プライベートアドレス宛てでインターネットに出られず届かない</td><td style='text-align:center'>5</td></tr><tr><td>設問4</td><td>198.51.100.20</td><td>・営業所ルータのインターネット側アドレス</td><td style='text-align:center'>4</td></tr><tr><td>設問5</td><td>ブロードキャストアドレス 192.168.3.255、ホスト数 510</td><td>・192.168.3.255<br>・2^9−2＝510</td><td style='text-align:center'>4</td></tr><tr><td colspan='3' style='text-align:right'>合計</td><td style='text-align:center'>20</td></tr></table>

:::note 解説
pingは「どこまで届くか」で切り分ける。IPsecトンネルでは、内側のパケット（192.168.2.x→192.168.1.10）を暗号化し、外側にルータのグローバルアドレスのヘッダを付ける。/23は第3オクテットの最下位ビットまでホスト部に含むので、192.168.2.0〜192.168.3.255。
:::

<p>自己採点：　　　　点 ／ 20点</p>
