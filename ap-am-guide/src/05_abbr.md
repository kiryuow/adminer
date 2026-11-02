---
no: 第5章
title: 頻出の英略語 120
lead: 略語は「元の英語」に分解すると意味が推測できる。分野別の頻出略語一覧
---

科目Aの選択肢には英略語が大量に出てきます。略語は **元の英語に分解** すると、意味を推測できることが多いです（例：RPO ＝ Recovery Point Objective ＝ 復旧の「時点」の目標）。

## テクノロジ系

| 略語 | 元の英語 | 意味 |
|---|---|---|
| CPI | Cycles Per Instruction | 1命令あたりの平均クロック数 |
| MIPS | Million Instructions Per Second | 1秒間に実行できる命令数（百万単位） |
| FLOPS | FLoating-point Operations Per Second | 1秒間の浮動小数点演算の回数 |
| RISC / CISC | Reduced / Complex Instruction Set Computer | 単純な固定長命令 ／ 複雑な可変長命令 |
| VLIW | Very Long Instruction Word | コンパイル時に複数の命令を1つの長い命令にまとめる |
| SIMD | Single Instruction Multiple Data | 1つの命令で複数のデータを同時に処理 |
| DMA | Direct Memory Access | CPUを介さないメモリと入出力装置の転送 |
| DRAM / SRAM | Dynamic / Static RAM | リフレッシュが必要な主記憶 ／ 高速なキャッシュ用 |
| SSD | Solid State Drive | フラッシュメモリの補助記憶装置 |
| RAID | Redundant Arrays of Inexpensive Disks | 複数ディスクで速度・信頼性を高める |
| FPGA | Field Programmable Gate Array | 利用者が回路を書き換えられるLSI |
| ASIC | Application Specific Integrated Circuit | 特定用途向けの専用LSI |
| SoC | System on a Chip | システムの機能を1チップに集積 |
| PWM | Pulse Width Modulation | パルス幅でモーター等を制御 |
| MTBF / MTTR | Mean Time Between Failures / To Repair | 平均故障間隔 ／ 平均修理時間 |
| RASIS | Reliability, Availability, Serviceability, Integrity, Security | 信頼性の評価指標 |
| IaaS / PaaS / SaaS | Infrastructure / Platform / Software as a Service | クラウドのサービスモデル |
| IaC | Infrastructure as Code | インフラ構成をコードで記述して自動適用 |
| VDI | Virtual Desktop Infrastructure | デスクトップ環境をサーバ上で動かす |
| HCI | Hyper-Converged Infrastructure | サーバとストレージを統合した基盤 |
| NAS / SAN | Network Attached Storage / Storage Area Network | LAN接続のファイルサーバ ／ ストレージ専用ネットワーク |
| OSS | Open Source Software | ソースコードが公開されたソフトウェア |
| GPL | GNU General Public License | 改変物もソース公開が必要（コピーレフト） |
| LRU / FIFO | Least Recently Used / First In First Out | 最も長く未使用 ／ 最も古いものを追い出す |
| TLB | Translation Lookaside Buffer | アドレス変換結果のキャッシュ |
| RTOS | Real-Time Operating System | リアルタイム性を重視したOS |
| GUI / CUI | Graphical / Character User Interface | 図形による操作 ／ 文字による操作 |
| UX | User Experience | 利用者の体験全体 |
| AR / VR / MR | Augmented / Virtual / Mixed Reality | 拡張現実 ／ 仮想現実 ／ 複合現実 |
| JPEG / MPEG | Joint Photographic / Moving Picture Experts Group | 静止画 ／ 動画の圧縮規格 |
| PCM | Pulse Code Modulation | 標本化・量子化・符号化によるデジタル化 |
| DBMS | DataBase Management System | データベース管理システム |
| SQL | Structured Query Language | 関係データベースの操作言語 |
| ACID | Atomicity, Consistency, Isolation, Durability | トランザクションの4特性 |
| BASE | Basically Available, Soft state, Eventually consistent | NoSQLが重視する結果整合性 |
| ETL | Extract, Transform, Load | データの抽出・変換・書込み |
| OLAP / OLTP | Online Analytical / Transaction Processing | 多次元分析 ／ 日々の取引処理 |
| DWH | Data WareHouse | 分析用の時系列データの蓄積 |
| OSI | Open Systems Interconnection | 通信の7階層モデル |
| TCP / UDP | Transmission Control / User Datagram Protocol | 信頼性重視 ／ 速度重視 |
| ARP | Address Resolution Protocol | IPアドレス→MACアドレス |
| DHCP | Dynamic Host Configuration Protocol | IPアドレスの自動割当て |
| DNS | Domain Name System | ドメイン名とIPアドレスの対応 |
| NAT / NAPT | Network Address (Port) Translation | アドレス（＋ポート）の変換 |
| ICMP | Internet Control Message Protocol | 到達確認・エラー通知（ping） |
| CIDR | Classless Inter-Domain Routing | /24 のようなプレフィックス長表記 |
| VLAN | Virtual LAN | 論理的なネットワーク分割 |
| VRRP | Virtual Router Redundancy Protocol | デフォルトゲートウェイの冗長化 |
| CSMA/CD・CA | Carrier Sense Multiple Access with Collision Detection / Avoidance | 衝突検出（有線） ／ 衝突回避（無線） |
| SDN | Software-Defined Networking | ソフトウェアでネットワークを集中制御 |
| CDN | Content Delivery Network | コンテンツを分散配信 |
| LPWA | Low Power Wide Area | 省電力・広域のIoT向け無線 |
| MQTT | Message Queuing Telemetry Transport | IoT向けの軽量なパブリッシュ／サブスクライブ型プロトコル |
| PoE | Power over Ethernet | LANケーブルで給電 |
| SNMP | Simple Network Management Protocol | ネットワーク機器の監視・管理 |
| SMTP / POP / IMAP | Simple Mail Transfer / Post Office / Internet Message Access Protocol | メールの送信 ／ 受信（DL） ／ 受信（サーバで管理） |

## セキュリティ

| 略語 | 元の英語 | 意味 |
|---|---|---|
| CIA | Confidentiality, Integrity, Availability | 機密性・完全性・可用性 |
| ISMS | Information Security Management System | 情報セキュリティマネジメントシステム |
| CSIRT | Computer Security Incident Response Team | インシデント対応チーム |
| SOC | Security Operation Center | 24時間監視・分析の組織 |
| AES / RSA | Advanced Encryption Standard / 考案者3名の頭文字 | 共通鍵暗号 ／ 公開鍵暗号 |
| PKI | Public Key Infrastructure | 公開鍵基盤 |
| CA / CRL / OCSP | Certification Authority / Certificate Revocation List / Online Certificate Status Protocol | 認証局 ／ 失効リスト ／ 失効状態の問合せ |
| TLS | Transport Layer Security | 通信の暗号化（HTTPS） |
| VPN / IPsec | Virtual Private Network / IP security | 仮想専用線 ／ ネットワーク層の暗号化 |
| WAF | Web Application Firewall | Webアプリへの攻撃を防御 |
| IDS / IPS | Intrusion Detection / Prevention System | 侵入の検知 ／ 防止 |
| UTM | Unified Threat Management | 複数のセキュリティ機能を1台に統合 |
| DMZ | DeMilitarized Zone | 公開サーバを置く緩衝地帯 |
| EDR | Endpoint Detection and Response | 端末の挙動監視と対応 |
| SIEM | Security Information and Event Management | ログの統合と相関分析 |
| DLP | Data Loss Prevention | 情報漏えい防止 |
| CASB | Cloud Access Security Broker | クラウド利用の可視化・制御 |
| SWG | Secure Web Gateway | クラウド型のWebプロキシ |
| MDM | Mobile Device Management | モバイル端末の一元管理 |
| SPF / DKIM / DMARC | Sender Policy Framework / DomainKeys Identified Mail / Domain-based Message Authentication, Reporting and Conformance | 送信元の検証（IP） ／ 電子署名 ／ 失敗時の処理方針 |
| XSS / CSRF | Cross-Site Scripting / Request Forgery | スクリプト埋込み ／ 意図しないリクエスト |
| DoS / DDoS | (Distributed) Denial of Service | サービス妨害（分散型） |
| APT | Advanced Persistent Threat | 持続的な標的型攻撃 |
| C&C | Command and Control | ボットへの指令サーバ |
| CVE / CVSS / CWE | Common Vulnerabilities and Exposures / Vulnerability Scoring System / Weakness Enumeration | 脆弱性の識別番号 ／ 深刻度 ／ 種類 |
| SBOM | Software Bill of Materials | ソフトウェア部品表 |
| TPM / HSM | Trusted Platform Module / Hardware Security Module | PC内蔵のセキュリティチップ ／ 鍵管理の専用装置 |
| SAML | Security Assertion Markup Language | SSOで認証結果を受け渡す |
| FIDO | Fast IDentity Online | パスワードレス認証 |
| SSO | Single Sign-On | 1回の認証で複数サービス |

## マネジメント・ストラテジ系

| 略語 | 元の英語 | 意味 |
|---|---|---|
| WBS | Work Breakdown Structure | 作業の階層的分解 |
| EVM | Earned Value Management | 出来高で進捗とコストを管理 |
| PV / EV / AC | Planned Value / Earned Value / Actual Cost | 計画 ／ 出来高 ／ 実コスト |
| SPI / CPI | Schedule / Cost Performance Index | スケジュール ／ コストの効率 |
| CCPM | Critical Chain Project Management | バッファで管理する日程手法 |
| PMO | Project Management Office | プロジェクト横断の支援部門 |
| RACI | Responsible, Accountable, Consulted, Informed | 責任分担の4区分 |
| SLA / OLA | Service / Operational Level Agreement | 顧客との合意 ／ 内部部門間の合意 |
| ITIL | IT Infrastructure Library | ITサービスマネジメントのベストプラクティス |
| CMDB | Configuration Management DataBase | 構成管理データベース |
| RFC | Request For Change | 変更要求 |
| CAB | Change Advisory Board | 変更諮問委員会 |
| SPOC | Single Point Of Contact | 単一窓口（サービスデスク） |
| RTO / RPO | Recovery Time / Point Objective | 目標復旧時間 ／ 目標復旧時点 |
| BCP / BCM | Business Continuity Plan / Management | 事業継続計画 ／ その管理 |
| UPS | Uninterruptible Power Supply | 無停電電源装置 |
| PUE | Power Usage Effectiveness | データセンタの電力効率 |
| CAAT | Computer Assisted Audit Techniques | コンピュータ支援監査技法 |
| CIO / CISO | Chief Information / Information Security Officer | 最高情報責任者 ／ 最高情報セキュリティ責任者 |
| EA | Enterprise Architecture | 業務とシステムの全体最適化の手法 |
| BPR / BPM / BPO | Business Process Re-engineering / Management / Outsourcing | 抜本的再設計 ／ 継続的改善 ／ 外部委託 |
| SOA | Service Oriented Architecture | サービス部品の組合せでシステム構築 |
| ERP | Enterprise Resource Planning | 基幹業務の統合パッケージ |
| CRM / SFA / SCM | Customer Relationship / Sales Force Automation / Supply Chain Management | 顧客関係 ／ 営業支援 ／ 供給連鎖 |
| RPA | Robotic Process Automation | 定型操作の自動化 |
| RFI / RFP / RFQ | Request For Information / Proposal / Quotation | 情報提供 ／ 提案 ／ 見積りの依頼 |
| ROI / NPV / IRR | Return On Investment / Net Present Value / Internal Rate of Return | 投資利益率 ／ 正味現在価値 ／ 内部収益率 |
| DX | Digital Transformation | デジタル技術による変革 |
| SWOT | Strengths, Weaknesses, Opportunities, Threats | 内部・外部環境の分析 |
| PPM | Product Portfolio Management | 事業の資源配分の分析 |
| BSC | Balanced ScoreCard | 4つの視点の業績評価 |
| KGI / KPI / CSF | Key Goal / Performance Indicator / Critical Success Factor | 最終目標 ／ 途中指標 ／ 成功要因 |
| MOT | Management Of Technology | 技術経営 |
| PoC / MVP | Proof of Concept / Minimum Viable Product | 概念実証 ／ 実用最小限の製品 |
| CPS | Cyber-Physical System | 現実と仮想の融合 |
| JIT | Just In Time | 必要な時に必要な量だけ生産 |
| MRP | Material Requirements Planning | 資材所要量計画 |
| EOQ | Economic Order Quantity | 経済的発注量 |
| ROE / ROA | Return On Equity / Assets | 自己資本 ／ 総資産利益率 |
| CSR / ESG / SDGs | Corporate Social Responsibility / Environment, Social, Governance / Sustainable Development Goals | 社会的責任 ／ 投資の観点 ／ 開発目標 |
| M&A / TOB / MBO | Mergers and Acquisitions / Take Over Bid / Management Buy-Out | 合併・買収 ／ 公開買付け ／ 経営陣による買収 |
| PL法 | Product Liability | 製造物責任法 |
