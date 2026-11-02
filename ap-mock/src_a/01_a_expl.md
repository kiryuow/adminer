---
no: 科目A
title: 科目A 解説
lead: 各問の正解と考え方。学習ノートの対応章を示す
---

<div class='mq'><span class='qn'>問1　正解 イ</span>　<span class='muted'>（基礎理論／学習ノート 第1章）</span><br>nビットの2の補数の範囲は −2^(n−1)〜2^(n−1)−1。16ビットなら −32,768〜32,767。</div>
<div class='mq'><span class='qn'>問2　正解 イ</span>　<span class='muted'>（基礎理論／学習ノート 第1章）</span><br>分配法則で A・(B＋B̄) ＝ A・1 ＝ A。カルノー図で見ると、Bの値にかかわらずA＝1の2マスがまとまる。</div>
<div class='mq'><span class='qn'>問3　正解 ア</span>　<span class='muted'>（基礎理論／学習ノート 第1章）</span><br>利用率ρ＝8/10＝0.8。平均待ち時間＝0.8/0.2×8＝32秒。応答時間＝32＋8＝40秒（＝サービス時間÷(1−ρ)）。</div>
<div class='mq'><span class='qn'>問4　正解 エ</span>　<span class='muted'>（基礎理論／学習ノート 第1章）</span><br>適合率＝TP/(TP＋FP)。再現率は実際の陽性のうち陽性と予測できた割合、偽陽性率は実際の陰性のうち誤って陽性と予測した割合。</div>
<div class='mq'><span class='qn'>問5　正解 ア</span>　<span class='muted'>（基礎理論／学習ノート 第1章）</span><br>情報量＝−log₂P＝−log₂(1/8)＝3ビット。起こりにくい事象ほど情報量は大きい。</div>
<div class='mq'><span class='qn'>問6　正解 エ</span>　<span class='muted'>（アルゴリズム／学習ノート 第2章）</span><br>3を最初に取り出すには1,2,3をすべて積む必要があり、その後は2→1の順にしか取り出せない。よって3,1,2は不可能。</div>
<div class='mq'><span class='qn'>問7　正解 ウ</span>　<span class='muted'>（アルゴリズム／学習ノート 第2章）</span><br>バブルソートは二重ループでO(n²)。2分探索はO(log n)、ハッシュ探索はO(1)、マージソートはO(n log n)。</div>
<div class='mq'><span class='qn'>問8　正解 イ</span>　<span class='muted'>（アルゴリズム／学習ノート 第2章）</span><br>f(0)=f(1)=1、f(2)=2、f(3)=3、f(4)=5、f(5)=8（フィボナッチ数）。再帰で同じ計算を繰り返すので、動的計画法で表に記録すると効率的。</div>
<div class='mq'><span class='qn'>問9　正解 エ</span>　<span class='muted'>（コンピュータ構成／学習ノート 第3章）</span><br>1秒のクロック数16億÷命令数4億＝4クロック/命令。</div>
<div class='mq'><span class='qn'>問10　正解 イ</span>　<span class='muted'>（コンピュータ構成／学習ノート 第3章）</span><br>主記憶の時間を1とすると 0.05h＋1×(1−h)＝0.24 → 1−0.95h＝0.24 → h＝0.8。</div>
<div class='mq'><span class='qn'>問11　正解 ア</span>　<span class='muted'>（コンピュータ構成／学習ノート 第3章）</span><br>メモリインタリーブは連続アドレスへのアクセスを並行化する。</div>
<div class='mq'><span class='qn'>問12　正解 エ</span>　<span class='muted'>（コンピュータ構成／学習ノート 第3章）</span><br>SSDはフラッシュメモリを使う不揮発性の記憶装置。シークや回転待ちはHDDの特徴。</div>
<div class='mq'><span class='qn'>問13　正解 エ</span>　<span class='muted'>（システム構成／学習ノート 第4章）</span><br>1−(1−0.9)³＝1−0.001＝0.999。0.729は3台直列。0.972は3台中2台以上稼働の場合。</div>
<div class='mq'><span class='qn'>問14　正解 ア</span>　<span class='muted'>（システム構成／学習ノート 第4章）</span><br>PaaSは実行環境（プラットフォーム）まで提供。IaaSはインフラのみ、SaaSはアプリケーションまで提供。</div>
<div class='mq'><span class='qn'>問15　正解 エ</span>　<span class='muted'>（システム構成／学習ノート 第4章）</span><br>コールドスタンバイは安価だが切替えに時間がかかる。ホットスタンバイは待機系を起動状態で待たせる。</div>
<div class='mq'><span class='qn'>問16　正解 ウ</span>　<span class='muted'>（ソフトウェア／学習ノート 第5章）</span><br>1,2,3でフォールト3回。4で最古の1を追い出し4回目[2,3,4]、1で2を追い出し5回目[3,4,1]、2で3を追い出し6回目。</div>
<div class='mq'><span class='qn'>問17　正解 イ</span>　<span class='muted'>（ソフトウェア／学習ノート 第5章）</span><br>プリエンプション（横取り）。ディスパッチは実行可能タスクにCPUを割り当てること。</div>
<div class='mq'><span class='qn'>問18　正解 イ</span>　<span class='muted'>（ソフトウェア／学習ノート 第5章）</span><br>増分は前回のバックアップ以降の変更分なので、フルに加えてすべての増分を順に適用する。差分方式なら日曜のフル＋木曜の差分で済む。</div>
<div class='mq'><span class='qn'>問19　正解 ア</span>　<span class='muted'>（ハードウェア／学習ノート 第3章）</span><br>A NAND A ＝ NOT(A・A) ＝ Ā。NANDだけで任意の論理回路を構成できる。</div>
<div class='mq'><span class='qn'>問20　正解 エ</span>　<span class='muted'>（ハードウェア／学習ノート 第3章）</span><br>8ビットで256段階。5.12÷256＝0.02V。</div>
<div class='mq'><span class='qn'>問21　正解 ウ</span>　<span class='muted'>（ハードウェア／学習ノート 第3章）</span><br>ブラシレスDCモーターは長寿命・低騒音。ステッピングモーターはパルス数で回転角を制御する。</div>
<div class='mq'><span class='qn'>問22　正解 エ</span>　<span class='muted'>（ハードウェア／学習ノート 第3章）</span><br>ウォッチドッグタイマはプログラムの暴走や停止を検出する。</div>
<div class='mq'><span class='qn'>問23　正解 ア</span>　<span class='muted'>（UI・メディア／学習ノート 第6章）</span><br>CSSで色・配置などのスタイルを指定する。構造（HTML）と見た目（CSS）を分離できる。</div>
<div class='mq'><span class='qn'>問24　正解 イ</span>　<span class='muted'>（UI・メディア／学習ノート 第6章）</span><br>認知的ウォークスルーは専門家が初心者になったつもりで検証する。思考発話法は利用者に考えを話しながら操作してもらう。</div>
<div class='mq'><span class='qn'>問25　正解 エ</span>　<span class='muted'>（UI・メディア／学習ノート 第6章）</span><br>MPEG（H.264、H.265など）はフレーム間の差分を利用する。JPEG・PNG・GIFは静止画の形式。</div>
<div class='mq'><span class='qn'>問26　正解 イ</span>　<span class='muted'>（データベース／学習ノート 第7章）</span><br>主キーは単一の列なので部分関数従属はなく第2正規形。注文番号→顧客番号→顧客名の推移的関数従属があるため第3正規形ではない。</div>
<div class='mq'><span class='qn'>問27　正解 イ</span>　<span class='muted'>（データベース／学習ノート 第7章）</span><br>集約関数の条件はGROUP BYの後のHAVINGに書く。WHEREはグループ化前の行の条件で、集約関数は使えない。</div>
<div class='mq'><span class='qn'>問28　正解 イ</span>　<span class='muted'>（データベース／学習ノート 第7章）</span><br>専有（排他）ロック中は他のトランザクションは読取りも更新もできない。共有ロックなら読取りは可能。</div>
<div class='mq'><span class='qn'>問29　正解 イ</span>　<span class='muted'>（データベース／学習ノート 第7章）</span><br>ロールバックは更新前ログで取り消す。ロールフォワードはバックアップと更新後ログでやり直す。</div>
<div class='mq'><span class='qn'>問30　正解 ウ</span>　<span class='muted'>（データベース／学習ノート 第7章）</span><br>ETL＝Extract（抽出）・Transform（変換）・Load（書込み）。OLTPは日々の取引処理。</div>
<div class='mq'><span class='qn'>問31　正解 ウ</span>　<span class='muted'>（ネットワーク／学習ノート 第8章）</span><br>/25は最終オクテットの最上位1ビットまでがネットワーク部。130＝10000010なのでネットワークは10.1.2.128、ホスト部をすべて1にすると10.1.2.255。</div>
<div class='mq'><span class='qn'>問32　正解 イ</span>　<span class='muted'>（ネットワーク／学習ノート 第8章）</span><br>TCPはコネクション型で確認応答・再送・順序制御を行う。UDPはコネクションレスで高速だが信頼性の制御はしない。</div>
<div class='mq'><span class='qn'>問33　正解 エ</span>　<span class='muted'>（ネットワーク／学習ノート 第8章）</span><br>AAAAはIPv6、AはIPv4。MXはメールサーバ、PTRは逆引き。</div>
<div class='mq'><span class='qn'>問34　正解 イ</span>　<span class='muted'>（ネットワーク／学習ノート 第8章）</span><br>500Mバイト＝4,000Mビット。4,000÷50＝80秒。バイトとビットの換算（×8）を忘れない。</div>
<div class='mq'><span class='qn'>問35　正解 イ</span>　<span class='muted'>（ネットワーク／学習ノート 第8章）</span><br>802.1QはタグVLAN。802.11acは無線LAN、802.3afはPoE、802.1Xはポートベースの認証。</div>
<div class='mq'><span class='qn'>問36　正解 エ</span>　<span class='muted'>（セキュリティ／学習ノート 第9章）</span><br>SQLインジェクションにはプレースホルダ（バインド機構）が根本的な対策。HTMLエスケープはXSS対策。</div>
<div class='mq'><span class='qn'>問37　正解 イ</span>　<span class='muted'>（セキュリティ／学習ノート 第9章）</span><br>n(n−1)/2＝20×19÷2＝190。公開鍵暗号方式なら1人1ペアで40個。</div>
<div class='mq'><span class='qn'>問38　正解 ウ</span>　<span class='muted'>（セキュリティ／学習ノート 第9章）</span><br>衝突発見困難性。一方向性はハッシュ値から元のメッセージを求めることが困難な性質。</div>
<div class='mq'><span class='qn'>問39　正解 エ</span>　<span class='muted'>（セキュリティ／学習ノート 第9章）</span><br>DMARCはSPF・DKIMの結果に基づく処理方針をDNSで公開する。S/MIMEはメールの暗号化と署名。</div>
<div class='mq'><span class='qn'>問40　正解 ア</span>　<span class='muted'>（セキュリティ／学習ノート 第9章）</span><br>DNSリフレクション（アンプ）攻撃はDDoSの一種。オープンリゾルバを放置しないことが対策。</div>
<div class='mq'><span class='qn'>問41　正解 ア</span>　<span class='muted'>（セキュリティ／学習ノート 第9章）</span><br>FIDO2はサーバに公開鍵だけを登録するため、サーバから漏えいしてもなりすましに使えない。</div>
<div class='mq'><span class='qn'>問42　正解 イ</span>　<span class='muted'>（セキュリティ／学習ノート 第9章）</span><br>EDRは端末（エンドポイント）の挙動を監視・対応する。WAFはWebアプリの防御、DLPは情報漏えい防止。</div>
<div class='mq'><span class='qn'>問43　正解 ウ</span>　<span class='muted'>（セキュリティ／学習ノート 第9章）</span><br>否認防止は「やっていない」と言わせない性質。「アクセス及び使用が可能」は可用性、「正確さ及び完全さ」は完全性、「主張するとおりのもの」は真正性の定義。</div>
<div class='mq'><span class='qn'>問44　正解 エ</span>　<span class='muted'>（セキュリティ／学習ノート 第9章）</span><br>SBOM（ソフトウェア部品表）。CVSSは脆弱性の深刻度評価、CRLは証明書失効リスト。</div>
<div class='mq'><span class='qn'>問45　正解 イ</span>　<span class='muted'>（セキュリティ／学習ノート 第9章）</span><br>ランサムウェアは接続中のバックアップも暗号化するため、オフライン・イミュータブル（書換え不可）な複数世代のバックアップが重要（3-2-1ルール）。</div>
<div class='mq'><span class='qn'>問46　正解 エ</span>　<span class='muted'>（開発技術／学習ノート 第10章）</span><br>弱い順：データ結合＜スタンプ結合＜制御結合＜外部結合＜共通結合＜内容結合。</div>
<div class='mq'><span class='qn'>問47　正解 イ</span>　<span class='muted'>（開発技術／学習ノート 第10章）</span><br>コンポジション（黒いひし形）。集約（白いひし形）は部分が単独でも存在できる。汎化はis-aの関係。</div>
<div class='mq'><span class='qn'>問48　正解 イ</span>　<span class='muted'>（開発技術／学習ノート 第10章）</span><br>判定全体の真と偽が1回ずつあればよい。(真,真)で真、(偽,真)で偽。4つすべては複数条件網羅。</div>
<div class='mq'><span class='qn'>問49　正解 エ</span>　<span class='muted'>（開発技術／学習ノート 第10章）</span><br>レトロスペクティブはプロセスの振り返り。スプリントレビューは成果物を関係者に見せてフィードバックを得る。</div>
<div class='mq'><span class='qn'>問50　正解 イ</span>　<span class='muted'>（開発技術／学習ノート 第10章）</span><br>リファクタリングは保守性を高める。変更後は回帰テストで振る舞いが変わっていないことを確認する。</div>
<div class='mq'><span class='qn'>問51　正解 ア</span>　<span class='muted'>（プロジェクトマネジメント／学習ノート 第11章）</span><br>CPI＝EV/AC＝600/750＝0.8、SPI＝EV/PV＝600/800＝0.75。どちらも1未満で、予算超過かつ遅れ。</div>
<div class='mq'><span class='qn'>問52　正解 ア</span>　<span class='muted'>（プロジェクトマネジメント／学習ノート 第11章）</span><br>全体は4＋5＋2＝11日（A→C→Dがクリティカルパス）。Bは最も早くて4日目終了後に始めて7日目に終わるが、Dの開始（9日目終了時点）までに終わればよいので、余裕は9−7＝2日。</div>
<div class='mq'><span class='qn'>問53　正解 ウ</span>　<span class='muted'>（プロジェクトマネジメント／学習ノート 第11章）</span><br>WBSの最下位がワークパッケージ。RACIは責任分担、ガントチャートは日程の横棒グラフ。</div>
<div class='mq'><span class='qn'>問54　正解 ウ</span>　<span class='muted'>（プロジェクトマネジメント／学習ノート 第11章）</span><br>転嫁は保険や契約（定額契約など）で影響を他者に移す。</div>
<div class='mq'><span class='qn'>問55　正解 エ</span>　<span class='muted'>（サービスマネジメント／学習ノート 第12章）</span><br>問題管理は根本原因の究明と再発防止。回避策で迅速に回復させるのはインシデント管理、変更要求の評価・承認は変更管理、問合せの受付はサービスデスクの活動。</div>
<div class='mq'><span class='qn'>問56　正解 エ</span>　<span class='muted'>（サービスマネジメント／学習ノート 第12章）</span><br>30日×24時間×60分＝43,200分。×0.001＝43.2分。</div>
<div class='mq'><span class='qn'>問57　正解 ア</span>　<span class='muted'>（サービスマネジメント／学習ノート 第12章）</span><br>吸気側をコールドアイル、排気側をホットアイルとして分離すると、冷気と暖気が混ざらず効率がよい。</div>
<div class='mq'><span class='qn'>問58　正解 エ</span>　<span class='muted'>（システム監査／学習ノート 第13章）</span><br>フォローアップで改善状況を確認する。監査人は改善の実施も命令も行わない。</div>
<div class='mq'><span class='qn'>問59　正解 ウ</span>　<span class='muted'>（システム監査／学習ノート 第13章）</span><br>ITF（Integrated Test Facility）法。テストデータ法は監査人のデータを処理させる、並行シミュレーションは監査人のプログラムと結果を比較する。</div>
<div class='mq'><span class='qn'>問60　正解 エ</span>　<span class='muted'>（システム監査／学習ノート 第13章）</span><br>職務分掌によって相互けん制を働かせ、不正や誤りを防ぐ。</div>
<div class='mq'><span class='qn'>問61　正解 ア</span>　<span class='muted'>（システム戦略／学習ノート 第14章）</span><br>As-Isが現状、To-Beが理想像。両者の差（ギャップ）を埋める計画を立てる。</div>
<div class='mq'><span class='qn'>問62　正解 ウ</span>　<span class='muted'>（システム戦略／学習ノート 第14章）</span><br>APIエコノミーの例：銀行のAPIを使った家計簿アプリ。</div>
<div class='mq'><span class='qn'>問63　正解 イ</span>　<span class='muted'>（システム企画／学習ノート 第14章）</span><br>共通フレームの企画プロセスでは、経営上のニーズ・課題の確認からシステム化構想を立案する。</div>
<div class='mq'><span class='qn'>問64　正解 ウ</span>　<span class='muted'>（システム企画／学習ノート 第14章）</span><br>3年で900万円、4年で1,200万円。4年目の途中で回収できる。</div>
<div class='mq'><span class='qn'>問65　正解 ア</span>　<span class='muted'>（システム企画／学習ノート 第14章）</span><br>評価基準は事前に決め、価格だけでなく技術・実績・体制なども総合的に評価する。</div>
<div class='mq'><span class='qn'>問66　正解 イ</span>　<span class='muted'>（システム企画／学習ノート 第14章）</span><br>トレーサビリティで要件の漏れや変更の影響範囲がわかる。</div>
<div class='mq'><span class='qn'>問67　正解 ウ</span>　<span class='muted'>（経営戦略／学習ノート 第15章）</span><br>学習と成長→業務プロセス→顧客→財務という因果関係を戦略マップで表す。</div>
<div class='mq'><span class='qn'>問68　正解 ア</span>　<span class='muted'>（経営戦略／学習ノート 第15章）</span><br>成熟期は市場が飽和し、差別化やコスト削減が重要。成長期は売上が急拡大し競合が参入する段階。</div>
<div class='mq'><span class='qn'>問69　正解 ア</span>　<span class='muted'>（経営戦略／学習ノート 第15章）</span><br>ERRCグリッド（取り除く・減らす・増やす・付け加える）で新しい価値を作る。</div>
<div class='mq'><span class='qn'>問70　正解 エ</span>　<span class='muted'>（技術戦略／学習ノート 第15章）</span><br>ハイプサイクルはガートナー社が示した、技術への期待の推移。</div>
<div class='mq'><span class='qn'>問71　正解 イ</span>　<span class='muted'>（ビジネスインダストリ／学習ノート 第15章）</span><br>デジタルツインは現実の双子を仮想空間に作り、シミュレーションや予測に使う。</div>
<div class='mq'><span class='qn'>問72　正解 ウ</span>　<span class='muted'>（ビジネスインダストリ／学習ノート 第15章）</span><br>フリマアプリやネットオークションがCtoC。</div>
<div class='mq'><span class='qn'>問73　正解 イ</span>　<span class='muted'>（企業活動／学習ノート 第16章）</span><br>1個あたりの限界利益＝2,000−1,200＝800円。400万÷800＝5,000個。</div>
<div class='mq'><span class='qn'>問74　正解 イ</span>　<span class='muted'>（企業活動／学習ノート 第16章）</span><br>流動比率。高いほど短期の支払能力が高く安全。</div>
<div class='mq'><span class='qn'>問75　正解 ア</span>　<span class='muted'>（企業活動／学習ノート 第16章）</span><br>特性要因図（フィッシュボーン図）。パレート図は重点項目の把握、散布図は相関、管理図は工程の異常の判断。</div>
<div class='mq'><span class='qn'>問76　正解 ア</span>　<span class='muted'>（企業活動／学習ノート 第16章）</span><br>制約：2X＋Y≦100、Y≦60。頂点で比較：(50,0)→200万、(20,60)→80＋180＝260万、(0,60)→180万、(40,20)→160＋60＝220万。最大は(20,60)。</div>
<div class='mq'><span class='qn'>問77　正解 イ</span>　<span class='muted'>（企業活動／学習ノート 第16章）</span><br>コンピテンシーは高業績者の行動特性、メンタリングは先輩による助言・支援。</div>
<div class='mq'><span class='qn'>問78　正解 エ</span>　<span class='muted'>（法務／学習ノート 第16章）</span><br>準委任は事務処理の遂行が目的で完成責任はない。完成責任があるのは請負契約。指揮命令は受託者が行う。</div>
<div class='mq'><span class='qn'>問79　正解 ア</span>　<span class='muted'>（法務／学習ノート 第16章）</span><br>不正アクセス禁止法は、なりすましによるログインやセキュリティホールを突いた侵入、他人のID・パスワードの不正な提供などを禁止する。</div>
<div class='mq'><span class='qn'>問80　正解 ア</span>　<span class='muted'>（法務／学習ノート 第16章）</span><br>著作者人格権は公表権・氏名表示権・同一性保持権で、譲渡できない。複製権は著作財産権。</div>
