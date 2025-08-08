#!/usr/bin/env python3
"""
戦略パターンページを縦並びに変更し、情報量を復元
"""

import os

html_dir = '/Users/noriken/Desktop/01_仕事_資料置き場/01_会議資料/明/RMC_財務分析/html資料/'

def fix_strategy_pattern():
    """戦略パターンページを修正"""
    filepath = os.path.join(html_dir, 'RMC戦略パターン詳細比較.html')
    
    html_content = '''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RMCクリニック 戦略パターン詳細比較分析</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', 'Hiragino Kaku Gothic ProN', 'Yu Gothic', sans-serif;
            line-height: 1.6;
            color: #2d3748;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        /* ナビゲーションタブ */
        .nav-tabs {
            background: white;
            padding: 20px 40px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 100;
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
            align-items: center;
            border-bottom: 2px solid #e5e7eb;
            border-radius: 15px;
            margin-bottom: 20px;
        }
        
        .nav-tabs .nav-title {
            font-size: 1.1em;
            font-weight: bold;
            color: #667eea;
            margin-right: auto;
        }
        
        .nav-tabs a {
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 8px;
            background: linear-gradient(135deg, #f5f7fa 0%, #e2e8f0 100%);
            color: #333;
            font-weight: 500;
            transition: all 0.3s;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            font-size: 0.95em;
        }
        
        .nav-tabs a:hover {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        }
        
        .nav-tabs a.current {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        }

        .main-header {
            text-align: center;
            color: white;
            padding: 60px 20px;
            margin-bottom: 40px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 30px;
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 30px 60px rgba(0,0,0,0.2);
        }

        .main-header h1 {
            font-size: 3rem;
            margin-bottom: 20px;
            font-weight: 800;
            letter-spacing: -1px;
            background: linear-gradient(45deg, #fff, #e2e8f0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }

        .main-header .subtitle {
            font-size: 1.3rem;
            color: rgba(255, 255, 255, 0.95);
            margin-bottom: 30px;
            font-weight: 400;
        }

        .key-insights {
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
            margin-top: 30px;
        }

        .insight-card {
            background: rgba(255, 255, 255, 0.2);
            padding: 15px 25px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            text-align: center;
        }

        .insight-number {
            display: block;
            font-size: 1.8rem;
            font-weight: bold;
            color: white;
            margin-bottom: 5px;
        }

        .insight-label {
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.9);
        }

        /* 戦略カード - 縦並びレイアウト */
        .strategy-card {
            background: white;
            border-radius: 20px;
            padding: 40px;
            margin-bottom: 30px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            border: 2px solid transparent;
            position: relative;
            overflow: hidden;
        }

        .strategy-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 5px;
        }

        .strategy-card.pattern-conservative::before {
            background: linear-gradient(90deg, #48bb78, #38a169);
        }

        .strategy-card.pattern-aggressive::before {
            background: linear-gradient(90deg, #f56565, #e53e3e);
        }

        .strategy-card.pattern-newbusiness::before {
            background: linear-gradient(90deg, #4299e1, #3182ce);
        }

        .strategy-card.pattern-steady::before {
            background: linear-gradient(90deg, #ed8936, #dd6b20);
        }

        .strategy-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 25px 50px rgba(0,0,0,0.15);
        }

        .pattern-header {
            display: flex;
            align-items: center;
            margin-bottom: 30px;
            padding-bottom: 25px;
            border-bottom: 2px solid #f0f4f8;
        }

        .pattern-icon {
            font-size: 3rem;
            margin-right: 20px;
        }

        .pattern-title {
            font-size: 2rem;
            color: #2d3748;
            margin-bottom: 5px;
            font-weight: 700;
        }

        .pattern-subtitle {
            color: #718096;
            font-size: 1.1rem;
        }

        .strategy-description {
            background: #f8fafc;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 30px;
            line-height: 1.8;
            color: #4a5568;
        }

        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-bottom: 30px;
        }

        .metric-box {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.05), rgba(118, 75, 162, 0.05));
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            border: 1px solid rgba(102, 126, 234, 0.2);
            transition: all 0.3s ease;
        }

        .metric-box:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.2);
        }

        .metric-value {
            display: block;
            font-size: 1.8rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 5px;
        }

        .metric-label {
            font-size: 0.9rem;
            color: #718096;
        }

        .detailed-timeline {
            margin-bottom: 30px;
        }

        .timeline-title {
            font-size: 1.5rem;
            color: #2d3748;
            margin-bottom: 20px;
            font-weight: 600;
        }

        .timeline-phases {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }

        .timeline-phase {
            background: #f8fafc;
            padding: 20px;
            border-radius: 12px;
            border-left: 4px solid #667eea;
            position: relative;
        }

        .phase-marker {
            position: absolute;
            left: -15px;
            top: 20px;
            width: 30px;
            height: 30px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
        }

        .phase-details h4 {
            color: #2d3748;
            margin-bottom: 5px;
            font-size: 1.2rem;
        }

        .phase-period {
            color: #667eea;
            font-size: 0.9rem;
            margin-bottom: 10px;
            font-weight: 600;
        }

        .phase-actions {
            margin-top: 10px;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .action-tag {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
            color: #667eea;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            border: 1px solid rgba(102, 126, 234, 0.3);
        }

        .risk-assessment {
            background: #f8fafc;
            padding: 30px;
            border-radius: 15px;
            margin-top: 30px;
        }

        .risk-title {
            font-size: 1.5rem;
            color: #2d3748;
            margin-bottom: 20px;
            font-weight: 600;
        }

        .pros-cons-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
        }

        .pros, .cons {
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        }

        .pros {
            border-top: 3px solid #48bb78;
        }

        .cons {
            border-top: 3px solid #f56565;
        }

        .pros h5, .cons h5 {
            font-size: 1.2rem;
            margin-bottom: 15px;
            color: #2d3748;
        }

        .pros ul, .cons ul {
            list-style: none;
            padding: 0;
        }

        .pros li, .cons li {
            padding: 8px 0;
            padding-left: 25px;
            position: relative;
            color: #4a5568;
            line-height: 1.6;
        }

        .pros li::before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #48bb78;
            font-weight: bold;
        }

        .cons li::before {
            content: "✕";
            position: absolute;
            left: 0;
            color: #f56565;
            font-weight: bold;
        }

        .comparison-summary {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
            padding: 40px;
            border-radius: 20px;
            margin-top: 40px;
            border: 2px solid rgba(102, 126, 234, 0.2);
        }

        .comparison-summary h2 {
            font-size: 2rem;
            margin-bottom: 30px;
            color: #2d3748;
            text-align: center;
            font-weight: 700;
        }

        .summary-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }

        .summary-item {
            background: white;
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }

        .summary-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        }

        .summary-label {
            font-size: 0.9rem;
            color: #718096;
            margin-bottom: 10px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .summary-value {
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .recommendation-section {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 50px;
            border-radius: 25px;
            margin-top: 40px;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }

        .recommendation-section h2 {
            font-size: 2.5rem;
            margin-bottom: 20px;
            font-weight: 700;
        }

        .recommendation-content {
            font-size: 1.2rem;
            line-height: 1.8;
            max-width: 800px;
            margin: 0 auto;
        }

        @media (max-width: 768px) {
            .metrics-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .timeline-phases {
                grid-template-columns: 1fr;
            }
            
            .pros-cons-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- ナビゲーションタブ -->
        <nav class="nav-tabs">
            <div class="nav-title">六本木メディカルクリニック</div>
            <a href="./index.html">経営分析レポート</a>
            <a href="./RMC戦略パターン詳細比較.html" class="current">戦略パターン比較</a>
            <a href="./RMC_購入分析_インフォグラフィック.html">購入分析</a>
            <a href="./購買行動分析_インフォグラフィック.html">購買行動分析</a>
            <a href="./株主総会資料_2025.html">株主総会資料</a>
        </nav>

        <header class="main-header">
            <h1>📊 戦略パターン詳細比較分析</h1>
            <p class="subtitle">自己資金2,500万円から始める4つの成長シナリオ完全分析</p>
            
            <div class="key-insights">
                <div class="insight-card">
                    <span class="insight-number">4種類</span>
                    <span class="insight-label">戦略パターン</span>
                </div>
                <div class="insight-card">
                    <span class="insight-number">30ヶ月</span>
                    <span class="insight-label">分析期間</span>
                </div>
                <div class="insight-card">
                    <span class="insight-number">2.4-8.0億円</span>
                    <span class="insight-label">想定売上範囲</span>
                </div>
                <div class="insight-card">
                    <span class="insight-number">0%</span>
                    <span class="insight-label">借入依存</span>
                </div>
            </div>
        </header>

        <!-- 戦略A: 慎重パターン -->
        <div class="strategy-card pattern-conservative">
            <div class="pattern-header">
                <span class="pattern-icon">🛡️</span>
                <div>
                    <h2 class="pattern-title">慎重パターン</h2>
                    <div class="pattern-subtitle">超保守的・リスク最小化戦略</div>
                </div>
            </div>
            
            <div class="strategy-description">
                <strong>戦略概要:</strong> リスクを極限まで抑制し、小額投資によるテストマーケティングを重視。効果が実証された施策のみに段階的に予算を配分し、確実性を最重要視する安全第一の成長戦略。現金流出を最小限に抑え、既存事業の安定運営を維持しながらの緩やかな成長を目指す。
            </div>

            <div class="metrics-grid">
                <div class="metric-box">
                    <span class="metric-value">900万円</span>
                    <span class="metric-label">30ヶ月総投資額</span>
                </div>
                <div class="metric-box">
                    <span class="metric-value">3.0億円</span>
                    <span class="metric-label">30ヶ月後年商</span>
                </div>
                <div class="metric-box">
                    <span class="metric-value">極低</span>
                    <span class="metric-label">リスクレベル</span>
                </div>
                <div class="metric-box">
                    <span class="metric-value">3ヶ月</span>
                    <span class="metric-label">平均回収期間</span>
                </div>
            </div>

            <div class="detailed-timeline">
                <h4 class="timeline-title">📅 詳細実行タイムライン</h4>
                <div class="timeline-phases">
                    <div class="timeline-phase">
                        <div class="phase-marker">1</div>
                        <div class="phase-details">
                            <h4>テスト検証期</h4>
                            <div class="phase-period">0-3ヶ月 | 投資額：150万円</div>
                            <p>Google広告・リファラル・LINE最適化を月30万円で小規模テスト。効果測定ツールを導入し、各チャネルのROIを厳密に測定。</p>
                            <div class="phase-actions">
                                <span class="action-tag">Google広告テスト</span>
                                <span class="action-tag">リファラル開始</span>
                                <span class="action-tag">効果測定強化</span>
                            </div>
                        </div>
                    </div>
                    <div class="timeline-phase">
                        <div class="phase-marker">2</div>
                        <div class="phase-details">
                            <h4>選択的拡大期</h4>
                            <div class="phase-period">3-9ヶ月 | 投資額：300万円</div>
                            <p>ROI250%以上を達成したチャネルのみに月50万円上限で投資拡大。効果の低い施策は即座に停止し、成功施策に予算集中。</p>
                            <div class="phase-actions">
                                <span class="action-tag">成功チャネル拡大</span>
                                <span class="action-tag">CRM導入</span>
                                <span class="action-tag">効果監視強化</span>
                            </div>
                        </div>
                    </div>
                    <div class="timeline-phase">
                        <div class="phase-marker">3</div>
                        <div class="phase-details">
                            <h4>安定成長期</h4>
                            <div class="phase-period">9-18ヶ月 | 投資額：300万円</div>
                            <p>実績のある施策に継続投資し、オペレーション効率化に注力。顧客満足度向上と再診率改善に取り組み、安定基盤を構築。</p>
                            <div class="phase-actions">
                                <span class="action-tag">効率化推進</span>
                                <span class="action-tag">顧客満足向上</span>
                                <span class="action-tag">再診率改善</span>
                            </div>
                        </div>
                    </div>
                    <div class="timeline-phase">
                        <div class="phase-marker">4</div>
                        <div class="phase-details">
                            <h4>最適化完成期</h4>
                            <div class="phase-period">18-30ヶ月 | 投資額：150万円</div>
                            <p>既存施策の最適化とコスト効率改善に集中。月商2,500万円を安定維持し、次段階成長への資金蓄積と準備を実施。</p>
                            <div class="phase-actions">
                                <span class="action-tag">最適化完成</span>
                                <span class="action-tag">コスト改善</span>
                                <span class="action-tag">次段階準備</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="risk-assessment">
                <h4 class="risk-title">🛡️ リスク評価・メリット/デメリット分析</h4>
                <div class="pros-cons-grid">
                    <div class="pros">
                        <h5>✅ 主要メリット</h5>
                        <ul>
                            <li>リスクが極めて低く、失敗時の損失を最小限に抑制</li>
                            <li>確実な成長を期待でき、予測可能性が高い</li>
                            <li>現金安全性が保たれ、経営安定性を維持</li>
                            <li>小規模投資での効果検証により、最適化が容易</li>
                            <li>既存事業への悪影響がほぼ皆無</li>
                            <li>市場環境悪化時にも柔軟に対応可能</li>
                        </ul>
                    </div>
                    <div class="cons">
                        <h5>⚠️ 主要デメリット</h5>
                        <ul>
                            <li>成長スピードが遅く、競合に後れを取るリスク</li>
                            <li>市場機会の逸失により、長期的競争力低下</li>
                            <li>積極投資による高リターンの機会を放棄</li>
                            <li>事業規模拡大に時間がかかり効率性が低い</li>
                            <li>市場シェア獲得が困難で影響力拡大に制約</li>
                            <li>革新的な成長機会への対応力が限定的</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- 戦略B: 段階的投資パターン -->
        <div class="strategy-card pattern-aggressive">
            <div class="pattern-header">
                <span class="pattern-icon">🚀</span>
                <div>
                    <h2 class="pattern-title">段階的投資パターン</h2>
                    <div class="pattern-subtitle">成功倍増・利益再投資戦略</div>
                </div>
            </div>
            
            <div class="strategy-description">
                <strong>戦略概要:</strong> 小額テストで効果を検証後、成功チャネルに大胆な投資を実行。利益の50%を継続的に再投資し、資金循環による急成長を実現。段階的にリスクを管理しながら、最大成長ポテンシャルを追求する攻めの戦略。市場シェア獲得と競合優位確立を目指す。
            </div>

            <div class="metrics-grid">
                <div class="metric-box">
                    <span class="metric-value">5,000万円</span>
                    <span class="metric-label">30ヶ月総投資額</span>
                </div>
                <div class="metric-box">
                    <span class="metric-value">8.0億円</span>
                    <span class="metric-label">30ヶ月後年商</span>
                </div>
                <div class="metric-box">
                    <span class="metric-value">中程度</span>
                    <span class="metric-label">リスクレベル</span>
                </div>
                <div class="metric-box">
                    <span class="metric-value">4ヶ月</span>
                    <span class="metric-label">平均回収期間</span>
                </div>
            </div>

            <div class="detailed-timeline">
                <h4 class="timeline-title">📅 詳細実行タイムライン</h4>
                <div class="timeline-phases">
                    <div class="timeline-phase">
                        <div class="phase-marker">1</div>
                        <div class="phase-details">
                            <h4>効果検証期</h4>
                            <div class="phase-period">0-6ヶ月 | 投資額：600万円</div>
                            <p>Google・Facebook広告を並行テストし、月100万円上限で複数チャネルを同時検証。リファラル・LINE強化も併行実施し、成功チャネルを特定。</p>
                            <div class="phase-actions">
                                <span class="action-tag">多チャネル並行テスト</span>
                                <span class="action-tag">成功パターン特定</span>
                                <span class="action-tag">ROI厳密測定</span>
                            </div>
                        </div>
                    </div>
                    <div class="timeline-phase">
                        <div class="phase-marker">2</div>
                        <div class="phase-details">
                            <h4>大胆投資期</h4>
                            <div class="phase-period">6-12ヶ月 | 投資額：1,800万円</div>
                            <p>成功チャネルに月300万円の大型投資を実行。インフルエンサー・アフィリエイトを本格展開し、利益の50%を再投資に回して成長加速。</p>
                            <div class="phase-actions">
                                <span class="action-tag">大型投資実行</span>
                                <span class="action-tag">新チャネル追加</span>
                                <span class="action-tag">利益50%再投資</span>
                            </div>
                        </div>
                    </div>
                    <div class="timeline-phase">
                        <div class="phase-marker">3</div>
                        <div class="phase-details">
                            <h4>スケール拡大期</h4>
                            <div class="phase-period">12-24ヶ月 | 投資額：2,400万円</div>
                            <p>月400万円の大規模投資で全チャネル同時展開。ブランディング強化とシステム自動化を推進し、市場シェア拡大を加速。</p>
                            <div class="phase-actions">
                                <span class="action-tag">大規模展開</span>
                                <span class="action-tag">ブランド強化</span>
                                <span class="action-tag">自動化推進</span>
                            </div>
                        </div>
                    </div>
                    <div class="timeline-phase">
                        <div class="phase-marker">4</div>
                        <div class="phase-details">
                            <h4>市場制覇期</h4>
                            <div class="phase-period">24-30ヶ月 | 投資額：200万円/月</div>
                            <p>効率化により投資を削減しながら月商6,700万円を維持。市場シェア維持と利益率最大化に注力し、次段階成長への準備を完了。</p>
                            <div class="phase-actions">
                                <span class="action-tag">効率化完成</span>
                                <span class="action-tag">市場シェア維持</span>
                                <span class="action-tag">利益最大化</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="risk-assessment">
                <h4 class="risk-title">🚀 リスク評価・メリット/デメリット分析</h4>
                <div class="pros-cons-grid">
                    <div class="pros">
                        <h5>✅ 主要メリット</h5>
                        <ul>
                            <li>最大成長ポテンシャルを実現し、4.4倍の売上拡大</li>
                            <li>高ROI（200-250%）を維持した効率的成長</li>
                            <li>市場シェア大幅拡大と競合優位性の確立</li>
                            <li>段階的検証によりリスクを適切に管理</li>
                            <li>利益再投資により資金循環の好循環を創出</li>
                            <li>業界リーダーポジション獲得の可能性</li>
                        </ul>
                    </div>
                    <div class="cons">
                        <h5>⚠️ 主要デメリット</h5>
                        <ul>
                            <li>中程度のリスクを伴い、市場環境に依存</li>
                            <li>大型投資により現金流出が大きい</li>
                            <li>各段階での適切な判断力が必要</li>
                            <li>投資効果が期待を下回る可能性</li>
                            <li>競合の反撃や市場飽和のリスク</li>
                            <li>組織体制の急拡大に伴う管理負荷</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- 戦略C: 新規事業パターン -->
        <div class="strategy-card pattern-newbusiness">
            <div class="pattern-header">
                <span class="pattern-icon">🌟</span>
                <div>
                    <h2 class="pattern-title">新規事業パターン</h2>
                    <div class="pattern-subtitle">多角化・収益源分散戦略</div>
                </div>
            </div>
            
            <div class="strategy-description">
                <strong>戦略概要:</strong> 自己資金範囲内でB2B健康管理サービスとVIPプレミアムサービスを段階的に立ち上げ。既存C2C事業との相乗効果を活用し、収益源の多角化により安定成長を実現。リスク分散と高付加価値サービスによる差別化戦略。
            </div>

            <div class="metrics-grid">
                <div class="metric-box">
                    <span class="metric-value">2,200万円</span>
                    <span class="metric-label">30ヶ月総投資額</span>
                </div>
                <div class="metric-box">
                    <span class="metric-value">6.5億円</span>
                    <span class="metric-label">30ヶ月後年商</span>
                </div>
                <div class="metric-box">
                    <span class="metric-value">中程度</span>
                    <span class="metric-label">リスクレベル</span>
                </div>
                <div class="metric-box">
                    <span class="metric-value">8ヶ月</span>
                    <span class="metric-label">平均回収期間</span>
                </div>
            </div>

            <div class="detailed-timeline">
                <h4 class="timeline-title">📅 詳細実行タイムライン</h4>
                <div class="timeline-phases">
                    <div class="timeline-phase">
                        <div class="phase-marker">1</div>
                        <div class="phase-details">
                            <h4>基盤強化期</h4>
                            <div class="phase-period">0-6ヶ月 | 投資額：400万円</div>
                            <p>既存事業の最適化とシステム基盤強化を実施。新規事業に必要な人材採用・教育を開始し、B2B・VIP市場の詳細調査を実行。</p>
                            <div class="phase-actions">
                                <span class="action-tag">基盤システム強化</span>
                                <span class="action-tag">人材採用</span>
                                <span class="action-tag">市場調査</span>
                            </div>
                        </div>
                    </div>
                    <div class="timeline-phase">
                        <div class="phase-marker">2</div>
                        <div class="phase-details">
                            <h4>B2B事業立上</h4>
                            <div class="phase-period">6-12ヶ月 | 投資額：800万円</div>
                            <p>企業向け健康管理サービスを正式開始。B2B営業チームを結成し、10社との初期契約獲得を目指す。既存事業も並行して維持・拡大。</p>
                            <div class="phase-actions">
                                <span class="action-tag">B2Bサービス開始</span>
                                <span class="action-tag">営業チーム結成</span>
                                <span class="action-tag">10社契約獲得</span>
                            </div>
                        </div>
                    </div>
                    <div class="timeline-phase">
                        <div class="phase-marker">3</div>
                        <div class="phase-details">
                            <h4>VIP事業追加</h4>
                            <div class="phase-period">12-18ヶ月 | 投資額：600万円</div>
                            <p>富裕層向けVIPサービスを開始。専任医師・コンシェルジュを配置し、50名のVIP会員獲得を目標。B2B事業の拡大も継続。</p>
                            <div class="phase-actions">
                                <span class="action-tag">VIPサービス開始</span>
                                <span class="action-tag">専任スタッフ配置</span>
                                <span class="action-tag">50名VIP獲得</span>
                            </div>
                        </div>
                    </div>
                    <div class="timeline-phase">
                        <div class="phase-marker">4</div>
                        <div class="phase-details">
                            <h4>事業統合期</h4>
                            <div class="phase-period">18-30ヶ月 | 投資額：400万円</div>
                            <p>3事業（C2C・B2B・VIP）の統合最適化を実施。B2B30社・VIP150名への拡大を達成し、月商5,400万円の安定運営を実現。</p>
                            <div class="phase-actions">
                                <span class="action-tag">3事業統合</span>
                                <span class="action-tag">B2B30社達成</span>
                                <span class="action-tag">VIP150名達成</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="risk-assessment">
                <h4 class="risk-title">🌟 リスク評価・メリット/デメリット分析</h4>
                <div class="pros-cons-grid">
                    <div class="pros">
                        <h5>✅ 主要メリット</h5>
                        <ul>
                            <li>収益源分散により経営安定性が大幅向上</li>
                            <li>B2B・VIPの高付加価値により利益率改善</li>
                            <li>市場環境変化に対するリスク分散効果</li>
                            <li>既存事業との相乗効果で効率的成長</li>
                            <li>競合他社との差別化ポジション確立</li>
                            <li>3.6倍の売上成長を安定的に実現</li>
                        </ul>
                    </div>
                    <div class="cons">
                        <h5>⚠️ 主要デメリット</h5>
                        <ul>
                            <li>複数事業の並行管理により運営が複雑化</li>
                            <li>B2B・VIP専門人材の確保が困難</li>
                            <li>初期投資が大きく回収期間が長期</li>
                            <li>各事業分野での専門知識・経験が必要</li>
                            <li>市場開拓に想定以上の時間が必要な可能性</li>
                            <li>3事業の最適バランス維持が課題</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- 戦略D: 現状改善パターン -->
        <div class="strategy-card pattern-steady">
            <div class="pattern-header">
                <span class="pattern-icon">📈</span>
                <div>
                    <h2 class="pattern-title">現状改善パターン</h2>
                    <div class="pattern-subtitle">安定成長・内部改善戦略</div>
                </div>
            </div>
            
            <div class="strategy-description">
                <strong>戦略概要:</strong> 大型投資は避けて内部改善に集中し、業務効率化・品質向上・顧客満足度改善により着実な成長を実現。投資リスクを回避し、既存リソースの最適活用と運営品質向上により、安全で持続可能な経営基盤を構築する戦略。
            </div>

            <div class="metrics-grid">
                <div class="metric-box">
                    <span class="metric-value">300万円</span>
                    <span class="metric-label">30ヶ月総投資額</span>
                </div>
                <div class="metric-box">
                    <span class="metric-value">2.4億円</span>
                    <span class="metric-label">30ヶ月後年商</span>
                </div>
                <div class="metric-box">
                    <span class="metric-value">極低</span>
                    <span class="metric-label">リスクレベル</span>
                </div>
                <div class="metric-box">
                    <span class="metric-value">即座</span>
                    <span class="metric-label">投資回収</span>
                </div>
            </div>

            <div class="detailed-timeline">
                <h4 class="timeline-title">📅 詳細実行タイムライン</h4>
                <div class="timeline-phases">
                    <div class="timeline-phase">
                        <div class="phase-marker">1</div>
                        <div class="phase-details">
                            <h4>効率化集中期</h4>
                            <div class="phase-period">0-6ヶ月 | 投資額：50万円</div>
                            <p>業務プロセス見直しとテンプレート最適化を実施。スタッフ教育強化により品質向上を図り、無料で実行可能な改善施策を中心に推進。</p>
                            <div class="phase-actions">
                                <span class="action-tag">プロセス見直し</span>
                                <span class="action-tag">テンプレート最適化</span>
                                <span class="action-tag">スタッフ教育</span>
                            </div>
                        </div>
                    </div>
                    <div class="timeline-phase">
                        <div class="phase-marker">2</div>
                        <div class="phase-details">
                            <h4>品質向上期</h4>
                            <div class="phase-period">6-12ヶ月 | 投資額：100万円</div>
                            <p>サービス品質向上と顧客満足度調査を実施。再診率改善施策と最小限のシステム改善により、顧客体験の向上を図る。</p>
                            <div class="phase-actions">
                                <span class="action-tag">品質向上</span>
                                <span class="action-tag">満足度調査</span>
                                <span class="action-tag">再診率改善</span>
                            </div>
                        </div>
                    </div>
                    <div class="timeline-phase">
                        <div class="phase-marker">3</div>
                        <div class="phase-details">
                            <h4>継続改善期</h4>
                            <div class="phase-period">12-24ヶ月 | 投資額：100万円</div>
                            <p>小規模な改善を継続実施し、オペレーション最適化を推進。口コミ誘導と紹介プログラムを強化し、自然成長を促進。</p>
                            <div class="phase-actions">
                                <span class="action-tag">継続改善</span>
                                <span class="action-tag">口コミ強化</span>
                                <span class="action-tag">紹介促進</span>
                            </div>
                        </div>
                    </div>
                    <div class="timeline-phase">
                        <div class="phase-marker">4</div>
                        <div class="phase-details">
                            <h4>安定運営期</h4>
                            <div class="phase-period">24-30ヶ月 | 投資額：50万円</div>
                            <p>安定運営を維持しながら、次段階成長への準備を実施。月商2,000万円を確実に維持し、内部留保を蓄積。</p>
                            <div class="phase-actions">
                                <span class="action-tag">安定運営</span>
                                <span class="action-tag">内部留保</span>
                                <span class="action-tag">次段階準備</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="risk-assessment">
                <h4 class="risk-title">📈 リスク評価・メリット/デメリット分析</h4>
                <div class="pros-cons-grid">
                    <div class="pros">
                        <h5>✅ 主要メリット</h5>
                        <ul>
                            <li>リスクがほぼゼロで、失敗の可能性が極めて低い</li>
                            <li>最小限の投資で確実な改善を実現</li>
                            <li>現金流出が最小で、財務安全性を確保</li>
                            <li>既存チームで実行可能、追加人材不要</li>
                            <li>内部改善により組織力が向上</li>
                            <li>持続可能な経営基盤を構築</li>
                        </ul>
                    </div>
                    <div class="cons">
                        <h5>⚠️ 主要デメリット</h5>
                        <ul>
                            <li>成長速度が極めて遅く、競合に遅れを取る</li>
                            <li>市場機会を逸失し、シェア縮小の可能性</li>
                            <li>売上成長が限定的（1.3倍程度）</li>
                            <li>革新的な施策を実行できない</li>
                            <li>市場変化への対応力が限定的</li>
                            <li>長期的な競争力確保が困難</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <div class="comparison-summary">
            <h2>総合比較サマリー</h2>
            <div class="summary-grid">
                <div class="summary-item">
                    <div class="summary-label">最大成長</div>
                    <div class="summary-value">8.0億円</div>
                    <p style="color: #718096; margin-top: 10px;">段階的投資</p>
                </div>
                <div class="summary-item">
                    <div class="summary-label">最小リスク</div>
                    <div class="summary-value">300万円</div>
                    <p style="color: #718096; margin-top: 10px;">現状改善</p>
                </div>
                <div class="summary-item">
                    <div class="summary-label">最速回収</div>
                    <div class="summary-value">即座</div>
                    <p style="color: #718096; margin-top: 10px;">現状改善</p>
                </div>
                <div class="summary-item">
                    <div class="summary-label">推奨戦略</div>
                    <div class="summary-value">段階的</div>
                    <p style="color: #718096; margin-top: 10px;">最大成長型</p>
                </div>
            </div>
        </div>

        <div class="recommendation-section">
            <h2>推奨アクション</h2>
            <div class="recommendation-content">
                <p>現在の市場環境と財務状況を考慮すると、<strong>段階的投資パターン</strong>が最適です。</p>
                <p>小額テストで効果を検証後、成功チャネルへの大胆な投資により、リスクを管理しながら最大成長を実現できます。</p>
                <p>利益の50%再投資により、自己資金内で年商8億円への成長が可能です。</p>
            </div>
        </div>
    </div>
</body>
</html>'''
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ RMC戦略パターン詳細比較.html を修正（縦並び・情報量復元）")

def main():
    print("="*60)
    print("戦略パターンページ修正スクリプト")
    print("="*60)
    
    fix_strategy_pattern()
    
    print("\n✅ 完了！")
    print("  - 縦並びレイアウトに変更")
    print("  - 元の詳細情報を復元")
    print("  - 横幅は1200pxで統一")

if __name__ == "__main__":
    main()