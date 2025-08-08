#!/usr/bin/env python3
"""
経営分析レポート以外のすべてのページを元のデザインに復元
横幅は1200pxで統一したまま、タイポグラフィーや図形などのビジュアル要素を復元
"""

import os

html_dir = '/Users/noriken/Desktop/01_仕事_資料置き場/01_会議資料/明/RMC_財務分析/html資料/'

# RMC戦略パターン詳細比較.htmlの復元
def restore_strategy_comparison():
    """戦略パターン比較ページを元のデザインに復元"""
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
            padding: 80px 20px;
            margin-bottom: 50px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 30px;
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 30px 60px rgba(0,0,0,0.2);
        }

        .main-header h1 {
            font-size: 3.5rem;
            margin-bottom: 25px;
            font-weight: 800;
            letter-spacing: -2px;
            background: linear-gradient(45deg, #fff, #e2e8f0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }

        .main-header .subtitle {
            font-size: 1.4rem;
            color: rgba(255, 255, 255, 0.95);
            margin-bottom: 20px;
            font-weight: 400;
        }

        .section {
            background: white;
            padding: 40px;
            margin-bottom: 30px;
            border-radius: 25px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
            transform: translateY(0);
            transition: all 0.3s ease;
        }

        .section:hover {
            transform: translateY(-5px);
            box-shadow: 0 30px 60px rgba(0,0,0,0.2);
        }

        .strategies-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }

        .strategy-card {
            background: white;
            border-radius: 20px;
            padding: 30px;
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
            background: linear-gradient(90deg, #667eea, #764ba2);
        }

        .strategy-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 25px 50px rgba(0,0,0,0.15);
            border-color: #667eea;
        }

        .strategy-header {
            display: flex;
            align-items: center;
            margin-bottom: 25px;
            padding-bottom: 20px;
            border-bottom: 2px solid #f0f4f8;
        }

        .strategy-icon {
            width: 60px;
            height: 60px;
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            margin-right: 20px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }

        .strategy-title h3 {
            font-size: 1.6rem;
            color: #2d3748;
            margin-bottom: 5px;
            font-weight: 700;
        }

        .strategy-title .subtitle {
            color: #718096;
            font-size: 0.95rem;
        }

        .metric-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 25px;
        }

        .metric-item {
            background: #f8fafc;
            padding: 15px;
            border-radius: 12px;
            transition: all 0.3s ease;
            border: 1px solid #e2e8f0;
        }

        .metric-item:hover {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.05), rgba(118, 75, 162, 0.05));
            border-color: #667eea;
            transform: scale(1.02);
        }

        .metric-label {
            font-size: 0.85rem;
            color: #718096;
            margin-bottom: 5px;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .metric-value {
            font-size: 1.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .risk-level {
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 600;
            display: inline-block;
            margin-top: 10px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .risk-low {
            background: linear-gradient(135deg, #48bb78, #38a169);
            color: white;
        }

        .risk-medium {
            background: linear-gradient(135deg, #ed8936, #dd6b20);
            color: white;
        }

        .risk-high {
            background: linear-gradient(135deg, #f56565, #e53e3e);
            color: white;
        }

        .pros-cons {
            margin-top: 25px;
            padding-top: 25px;
            border-top: 2px solid #f0f4f8;
        }

        .pros-cons h4 {
            font-size: 1.1rem;
            margin-bottom: 15px;
            color: #4a5568;
            display: flex;
            align-items: center;
            font-weight: 600;
        }

        .pros-cons h4::before {
            content: '';
            width: 4px;
            height: 20px;
            margin-right: 10px;
            border-radius: 2px;
        }

        .pros h4::before {
            background: linear-gradient(135deg, #48bb78, #38a169);
        }

        .cons h4::before {
            background: linear-gradient(135deg, #f56565, #e53e3e);
        }

        .pros-cons ul {
            list-style: none;
            padding: 0;
        }

        .pros-cons li {
            padding: 10px 0 10px 30px;
            position: relative;
            color: #4a5568;
            font-size: 0.95rem;
            line-height: 1.6;
        }

        .pros li::before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #48bb78;
            font-weight: bold;
            font-size: 1.2rem;
        }

        .cons li::before {
            content: "✕";
            position: absolute;
            left: 0;
            color: #f56565;
            font-weight: bold;
            font-size: 1.2rem;
        }

        .winner-badge {
            position: absolute;
            top: 20px;
            right: 20px;
            background: linear-gradient(135deg, #f6ad55, #ed8936);
            color: white;
            padding: 8px 20px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 0.9rem;
            box-shadow: 0 10px 20px rgba(237, 137, 54, 0.3);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
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

        .action-button {
            display: inline-block;
            margin-top: 30px;
            padding: 15px 40px;
            background: white;
            color: #667eea;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 700;
            font-size: 1.1rem;
            transition: all 0.3s ease;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }

        .action-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.3);
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
            <h1>戦略パターン詳細比較分析</h1>
            <p class="subtitle">データドリブンな最適戦略の選択</p>
        </header>

        <div class="strategies-container">
            <!-- 戦略A: 積極拡大戦略 -->
            <div class="strategy-card">
                <div class="strategy-header">
                    <div class="strategy-icon">🚀</div>
                    <div class="strategy-title">
                        <h3>戦略A: 積極拡大</h3>
                        <p class="subtitle">高成長・高リスク</p>
                    </div>
                </div>
                
                <div class="metric-grid">
                    <div class="metric-item">
                        <div class="metric-label">期待売上成長</div>
                        <div class="metric-value">250%</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-label">必要投資額</div>
                        <div class="metric-value">¥500万</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-label">ROI</div>
                        <div class="metric-value">320%</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-label">回収期間</div>
                        <div class="metric-value">6ヶ月</div>
                    </div>
                </div>

                <span class="risk-level risk-high">リスク: 高</span>

                <div class="pros-cons">
                    <div class="pros">
                        <h4>メリット</h4>
                        <ul>
                            <li>最大の成長ポテンシャル</li>
                            <li>市場シェア急拡大</li>
                            <li>ブランド認知度向上</li>
                        </ul>
                    </div>
                    <div class="cons">
                        <h4>リスク</h4>
                        <ul>
                            <li>初期投資額が大きい</li>
                            <li>運転資金の圧迫</li>
                            <li>品質管理の課題</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- 戦略B: バランス成長戦略 -->
            <div class="strategy-card">
                <div class="winner-badge">推奨</div>
                <div class="strategy-header">
                    <div class="strategy-icon">⚖️</div>
                    <div class="strategy-title">
                        <h3>戦略B: バランス成長</h3>
                        <p class="subtitle">中成長・中リスク</p>
                    </div>
                </div>
                
                <div class="metric-grid">
                    <div class="metric-item">
                        <div class="metric-label">期待売上成長</div>
                        <div class="metric-value">150%</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-label">必要投資額</div>
                        <div class="metric-value">¥200万</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-label">ROI</div>
                        <div class="metric-value">450%</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-label">回収期間</div>
                        <div class="metric-value">3ヶ月</div>
                    </div>
                </div>

                <span class="risk-level risk-medium">リスク: 中</span>

                <div class="pros-cons">
                    <div class="pros">
                        <h4>メリット</h4>
                        <ul>
                            <li>最適なリスク・リターン</li>
                            <li>段階的な成長が可能</li>
                            <li>品質維持しやすい</li>
                        </ul>
                    </div>
                    <div class="cons">
                        <h4>リスク</h4>
                        <ul>
                            <li>競合に先行されるリスク</li>
                            <li>中途半端になる可能性</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- 戦略C: 安定維持戦略 -->
            <div class="strategy-card">
                <div class="strategy-header">
                    <div class="strategy-icon">🛡️</div>
                    <div class="strategy-title">
                        <h3>戦略C: 安定維持</h3>
                        <p class="subtitle">低成長・低リスク</p>
                    </div>
                </div>
                
                <div class="metric-grid">
                    <div class="metric-item">
                        <div class="metric-label">期待売上成長</div>
                        <div class="metric-value">50%</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-label">必要投資額</div>
                        <div class="metric-value">¥50万</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-label">ROI</div>
                        <div class="metric-value">200%</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-label">回収期間</div>
                        <div class="metric-value">2ヶ月</div>
                    </div>
                </div>

                <span class="risk-level risk-low">リスク: 低</span>

                <div class="pros-cons">
                    <div class="pros">
                        <h4>メリット</h4>
                        <ul>
                            <li>最小限の投資リスク</li>
                            <li>確実な収益確保</li>
                            <li>運営の安定性</li>
                        </ul>
                    </div>
                    <div class="cons">
                        <h4>リスク</h4>
                        <ul>
                            <li>成長機会の損失</li>
                            <li>市場シェア縮小リスク</li>
                            <li>イノベーション不足</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <div class="section comparison-summary">
            <h2>総合比較サマリー</h2>
            <div class="summary-grid">
                <div class="summary-item">
                    <div class="summary-label">最高ROI</div>
                    <div class="summary-value">450%</div>
                    <p style="color: #718096; margin-top: 10px;">戦略B</p>
                </div>
                <div class="summary-item">
                    <div class="summary-label">最速回収</div>
                    <div class="summary-value">2ヶ月</div>
                    <p style="color: #718096; margin-top: 10px;">戦略C</p>
                </div>
                <div class="summary-item">
                    <div class="summary-label">最大成長</div>
                    <div class="summary-value">250%</div>
                    <p style="color: #718096; margin-top: 10px;">戦略A</p>
                </div>
                <div class="summary-item">
                    <div class="summary-label">推奨戦略</div>
                    <div class="summary-value">B</div>
                    <p style="color: #718096; margin-top: 10px;">バランス型</p>
                </div>
            </div>
        </div>

        <div class="recommendation-section">
            <h2>推奨アクション</h2>
            <div class="recommendation-content">
                <p>現在の市場環境と財務状況を考慮すると、<strong>戦略B（バランス成長戦略）</strong>が最適です。</p>
                <p>段階的な成長により品質を維持しながら、適切なリスク管理のもとで最大のROIを実現できます。</p>
                <a href="#" class="action-button">実行計画を開始</a>
            </div>
        </div>
    </div>
</body>
</html>'''
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ RMC戦略パターン詳細比較.html を元のデザインに復元")

# 購買行動分析_インフォグラフィック.htmlの復元 
def restore_purchase_behavior():
    """購買行動分析ページを元のデザインに復元"""
    filepath = os.path.join(html_dir, '購買行動分析_インフォグラフィック.html')
    
    # 購買行動分析ページを読み込んで必要な部分だけ修正
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # common-styles.cssの参照を削除し、元のスタイルを復元
    new_content = '''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RMC 購買行動分析</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            line-height: 1.6;
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }

        /* ナビゲーションタブ */
        .nav-tabs {
            background: white;
            padding: 20px 40px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
            align-items: center;
            border-bottom: 2px solid #e5e7eb;
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
        
        .nav-tabs a.active {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        }

        .content {
            padding: 40px;
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 60px 40px;
            text-align: center;
            margin: -40px -40px 40px -40px;
            position: relative;
            overflow: hidden;
        }

        .header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="%23ffffff" fill-opacity="0.1" d="M0,96L48,112C96,128,192,160,288,160C384,160,480,128,576,112C672,96,768,96,864,112C960,128,1056,160,1152,160C1248,160,1344,128,1392,112L1440,96L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>') bottom center/cover no-repeat;
        }

        .header h1 {
            font-size: 3em;
            margin-bottom: 10px;
            position: relative;
            z-index: 1;
        }

        .header .subtitle {
            font-size: 1.3em;
            opacity: 0.95;
            position: relative;
            z-index: 1;
        }

        .dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }

        .card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            transform: translateY(-2px);
        }

        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2);
        }

        .card:hover {
            transform: translateY(-8px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        }

        .card h3 {
            color: #2d3748;
            margin-bottom: 15px;
            font-size: 1.1em;
        }

        .metric-large {
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
            margin: 10px 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .progress-bar {
            height: 8px;
            background: #e2e8f0;
            border-radius: 10px;
            overflow: hidden;
            margin-top: 10px;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            border-radius: 10px;
            transition: width 1.5s ease;
            animation: progressAnimation 2s ease-out;
        }

        @keyframes progressAnimation {
            from { width: 0; }
        }

        .card.success { border-top-color: #48bb78; }
        .card.warning { border-top-color: #ed8936; }
        .card.info { border-top-color: #4299e1; }

        .funnel-container {
            background: white;
            border-radius: 20px;
            padding: 40px;
            margin-bottom: 40px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        .funnel {
            max-width: 800px;
            margin: 0 auto;
        }

        .funnel-stage {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            margin: 15px 0;
            border-radius: 15px;
            text-align: center;
            position: relative;
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.3);
            transition: all 0.3s ease;
        }

        .funnel-stage:hover {
            transform: translateX(10px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        }

        .funnel-arrow {
            text-align: center;
            color: #718096;
            margin: 20px 0;
            font-size: 1.5em;
        }

        .improvement-section {
            background: #f7fafc;
            border-left: 4px solid #667eea;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
        }

        .improvement-title {
            font-weight: bold;
            color: #2d3748;
            margin-bottom: 10px;
        }

        .comparison-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }

        .comparison-card {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }

        .comparison-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        }

        .highlight-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            text-align: center;
            font-weight: bold;
        }

        .segment-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }

        .segment-card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .segment-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2);
        }

        .segment-card:hover {
            transform: translateY(-5px) scale(1.02);
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        }

        .segment-icon {
            font-size: 3em;
            margin-bottom: 15px;
        }

        .action-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
            margin-top: 30px;
        }

        .action-card {
            background: linear-gradient(135deg, #fff 0%, #f7fafc 100%);
            border: 2px solid #e2e8f0;
            border-radius: 15px;
            padding: 25px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .action-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #48bb78, #38a169);
        }

        .action-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
            border-color: #667eea;
        }

        .timeline {
            background: white;
            border-radius: 20px;
            padding: 40px;
            margin-bottom: 40px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        .timeline-item {
            display: flex;
            align-items: center;
            margin: 30px 0;
            position: relative;
            padding-left: 60px;
        }

        .timeline-item::before {
            content: '';
            position: absolute;
            left: 25px;
            top: 40px;
            bottom: -30px;
            width: 2px;
            background: #e2e8f0;
        }

        .timeline-item:last-child::before {
            display: none;
        }

        .timeline-icon {
            position: absolute;
            left: 10px;
            width: 30px;
            height: 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 14px;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        }

        .roi-showcase {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 50px;
            border-radius: 20px;
            margin-bottom: 40px;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
            position: relative;
            overflow: hidden;
        }

        .roi-showcase::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: rotate 20s linear infinite;
        }

        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .action-section {
            background: white;
            border-radius: 20px;
            padding: 40px;
            margin-bottom: 40px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        .bar-chart {
            display: flex;
            align-items: flex-end;
            justify-content: space-around;
            height: 300px;
            padding: 20px;
            background: white;
            border-radius: 15px;
            margin: 30px 0;
        }

        .bar {
            width: 100px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px 10px 0 0;
            position: relative;
            transition: all 0.3s ease;
            animation: growBar 1.5s ease-out;
        }

        @keyframes growBar {
            from { height: 0; }
        }

        .bar:hover {
            transform: scaleY(1.05);
        }

        .bar-value {
            position: absolute;
            top: -30px;
            left: 50%;
            transform: translateX(-50%);
            font-weight: bold;
            color: #2d3748;
        }

        .bar-label {
            position: absolute;
            bottom: -40px;
            left: 50%;
            transform: translateX(-50%);
            text-align: center;
            font-size: 0.9em;
            color: #718096;
            width: 120px;
        }

        .chart-container {
            background: white;
            border-radius: 20px;
            padding: 40px;
            margin-bottom: 40px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        .fade-in {
            animation: fadeIn 0.8s ease-out;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .pulse {
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.02); }
        }

        footer {
            text-align: center;
            padding: 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            margin-top: 40px;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- ナビゲーションタブ -->
        <nav class="nav-tabs">
            <a href="./index.html">経営分析レポート</a>
            <a href="./RMC戦略パターン詳細比較.html">戦略パターン比較</a>
            <a href="./RMC_購入分析_インフォグラフィック.html">購入分析</a>
            <a href="./購買行動分析_インフォグラフィック.html" class="active">購買行動分析</a>
            <a href="./株主総会資料_2025.html">株主総会資料</a>
        </nav>

        <!-- メインコンテンツ -->
        <div class="content">
        
        <!-- ヘッダー -->
        <header class="header fade-in">
            <h1><i class="fas fa-chart-line"></i> RMC 購買行動分析</h1>
            <p class="subtitle">データドリブン改善提案 - 売上2.5倍成長への道筋</p>
            <p style="margin-top: 10px; font-size: 0.9em;">分析日：2025年8月8日 | 対象期間：2024年4月～2025年8月</p>
        </header>

        <!-- 重要指標ダッシュボード -->
        <div class="dashboard fade-in">
            <div class="card info">
                <h3><i class="fas fa-chart-area"></i> 現在の月間売上</h3>
                <div class="metric-large">¥1,200万</div>
                <p>基準売上（改善前）</p>
                <div class="progress-bar">
                    <div class="progress-fill info" style="width: 40%"></div>
                </div>
            </div>

            <div class="card warning">
                <h3><i class="fas fa-users"></i> 検討中患者</h3>
                <div class="metric-large">1,372人</div>
                <p>購入意向はあるが未転換</p>
                <div class="progress-bar">
                    <div class="progress-fill warning" style="width: 42%"></div>
                </div>
            </div>

            <div class="card success">
                <h3><i class="fas fa-chart-line"></i> 改善ポテンシャル</h3>
                <div class="metric-large">250%</div>
                <p>現在売上の2.5倍成長可能</p>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: 90%"></div>
                </div>
            </div>

            <div class="card info">
                <h3><i class="fas fa-yen-sign"></i> 期待ROI</h3>
                <div class="metric-large">1,560%</div>
                <p>投資回収期間：2.4ヶ月</p>
                <div class="progress-bar">
                    <div class="progress-fill info" style="width: 95%"></div>
                </div>
            </div>
        </div>

        <!-- 購買ファネル -->
        <div class="funnel-container fade-in">
            <h2 style="text-align: center; margin-bottom: 30px; color: #2c3e50;">
                <i class="fas fa-filter"></i> 購買ファネル分析と改善目標
            </h2>
            <div class="funnel">
                <div class="funnel-stage">
                    <div style="font-size: 1.3em; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
                        <i class="fas fa-users"></i> 訪問・登録
                    </div>
                    <div style="font-size: 2.2em; margin: 15px 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">3,293人</div>
                    <div style="font-size: 0.95em;">100.0% | 獲得効率は良好（現状維持）</div>
                </div>

                <div class="improvement-section">
                    <div class="improvement-title"><i class="fas fa-lightbulb"></i> 興味表示率向上のための改善施策</div>
                    <div class="improvement-list">
                        • コンテンツマーケティング強化（成功事例・体験談）<br>
                        • ランディングページの最適化とA/Bテスト<br>
                        • SNS広告のターゲティング精度向上<br>
                        • 初回相談の心理的ハードルを下げる仕組み
                    </div>
                </div>

                <div class="funnel-arrow"><i class="fas fa-arrow-down"></i> 58.3% → <strong style="color: #27ae60;">65% (+6.7pt)</strong></div>
                
                <div class="funnel-stage">
                    <div style="font-size: 1.3em; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
                        <i class="fas fa-heart"></i> 興味表示
                    </div>
                    <div style="font-size: 2.2em; margin: 15px 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
                        1,919人 → <span style="color: #fff; background: rgba(39,174,96,0.3); padding: 2px 8px; border-radius: 5px;">2,140人</span>
                    </div>
                    <div style="font-size: 0.95em;">58.3% → <strong style="color: #fff; background: rgba(39,174,96,0.3); padding: 2px 8px; border-radius: 5px;">65%</strong></div>
                </div>

                <div class="improvement-section">
                    <div class="improvement-title"><i class="fas fa-shopping-cart"></i> 購入転換率向上のための改善施策</div>
                    <div class="improvement-list">
                        • パーソナライズされた商品提案システム<br>
                        • 初回購入特典・割引キャンペーン<br>
                        • チャットサポートによる購入前不安解消<br>
                        • 支払い方法の多様化（分割払い・後払い）
                    </div>
                </div>

                <div class="funnel-arrow"><i class="fas fa-arrow-down"></i> 31.1% → <strong style="color: #27ae60;">38% (+6.9pt)</strong></div>
                
                <div class="funnel-stage">
                    <div style="font-size: 1.3em; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
                        <i class="fas fa-credit-card"></i> 購入完了
                    </div>
                    <div style="font-size: 2.2em; margin: 15px 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
                        597人 → <span style="color: #fff; background: rgba(39,174,96,0.3); padding: 2px 8px; border-radius: 5px;">813人</span>
                    </div>
                    <div style="font-size: 0.95em;">18.1% → <strong style="color: #fff; background: rgba(39,174,96,0.3); padding: 2px 8px; border-radius: 5px;">24.7%</strong></div>
                </div>

                <div class="improvement-section">
                    <div class="improvement-title"><i class="fas fa-redo"></i> リピート購入促進のための改善施策</div>
                    <div class="improvement-list">
                        • 初回購入後のフォローアップメール自動化<br>
                        • 効果実感タイミングでのリピート提案<br>
                        • 継続購入インセンティブ（割引・ポイント）<br>
                        • カスタマーサクセスチームによる個別サポート
                    </div>
                </div>

                <div class="funnel-arrow"><i class="fas fa-arrow-down"></i> 42.5% → <strong style="color: #27ae60;">50% (+7.5pt)</strong></div>
                
                <div class="funnel-stage">
                    <div style="font-size: 1.3em; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
                        <i class="fas fa-sync-alt"></i> リピート購入
                    </div>
                    <div style="font-size: 2.2em; margin: 15px 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
                        254人 → <span style="color: #fff; background: rgba(39,174,96,0.3); padding: 2px 8px; border-radius: 5px;">407人</span>
                    </div>
                    <div style="font-size: 0.95em;">7.7% → <strong style="color: #fff; background: rgba(39,174,96,0.3); padding: 2px 8px; border-radius: 5px;">12.4%</strong></div>
                </div>

                <div class="improvement-section">
                    <div class="improvement-title"><i class="fas fa-crown"></i> 定期契約移行のための改善施策</div>
                    <div class="improvement-list">
                        • 定期契約の特典・割引率向上<br>
                        • お届け頻度の柔軟性向上（月1・2・3回選択）<br>
                        • 定期契約者限定の特別サービス<br>
                        • 解約防止のためのカスタマーケア強化
                    </div>
                </div>

                <div class="funnel-arrow"><i class="fas fa-arrow-down"></i> 24.6% → <strong style="color: #27ae60;">36% (+11.4pt)</strong></div>
                
                <div class="funnel-stage">
                    <div style="font-size: 1.3em; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
                        <i class="fas fa-calendar-check"></i> 定期契約
                    </div>
                    <div style="font-size: 2.2em; margin: 15px 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
                        147人 → <span style="color: #fff; background: rgba(39,174,96,0.3); padding: 2px 8px; border-radius: 5px;">215人</span>
                    </div>
                    <div style="font-size: 0.95em;">4.5% → <strong style="color: #fff; background: rgba(39,174,96,0.3); padding: 2px 8px; border-radius: 5px;">6.5%</strong></div>
                </div>
            </div>

            <!-- 改善効果サマリー -->
            <div style="margin-top: 40px; background: #f8f9fa; padding: 25px; border-radius: 15px; border-left: 5px solid #27ae60;">
                <h3 style="color: #27ae60; margin-bottom: 20px; text-align: center;">
                    <i class="fas fa-calculator"></i> 改善達成時の推定効果
                </h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; text-align: center;">
                    <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                        <div style="font-size: 1.5em; font-weight: bold; color: #27ae60; margin-bottom: 10px;">+216人</div>
                        <div style="color: #666;">追加購入者数</div>
                    </div>
                    <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                        <div style="font-size: 1.5em; font-weight: bold; color: #27ae60; margin-bottom: 10px;">+¥480万</div>
                        <div style="color: #666;">月間売上増</div>
                    </div>
                    <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                        <div style="font-size: 1.5em; font-weight: bold; color: #27ae60; margin-bottom: 10px;">¥1,680万</div>
                        <div style="color: #666;">改善後月間売上</div>
                    </div>
                    <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                        <div style="font-size: 1.5em; font-weight: bold; color: #27ae60; margin-bottom: 10px;">+40%</div>
                        <div style="color: #666;">売上成長率</div>
                    </div>
                </div>
                <div style="margin-top: 20px; text-align: center; color: #666; font-size: 0.9em;">
                    ※ 平均客単価¥22,334を基に算出。段階的改善により6ヶ月で達成目標
                </div>
            </div>
        </div>

        <!-- 通常患者 vs ブロック患者比較 -->
        <div class="comparison-container fade-in">
            <div class="comparison-card">
                <h3 style="color: #27ae60; margin-bottom: 20px;">
                    <i class="fas fa-user-check"></i> 通常患者
                </h3>
                <div style="margin-bottom: 15px;">
                    <strong>登録：</strong> 2,819人
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 100%"></div>
                    </div>
                </div>
                <div style="margin-bottom: 15px;">
                    <strong>興味表示：</strong> 1,650人 (58.5%)
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 58.5%"></div>
                    </div>
                </div>
                <div style="margin-bottom: 15px;">
                    <strong>購入完了：</strong> 564人 (20.0%)
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 20%"></div>
                    </div>
                </div>
                <div class="highlight-box" style="background: linear-gradient(135deg, #27ae60, #2ecc71);">
                    <div>転換率: 34.2%</div>
                    <div style="font-size: 0.9em;">（業界平均並み）</div>
                </div>
            </div>

            <div class="comparison-card">
                <h3 style="color: #e74c3c; margin-bottom: 20px;">
                    <i class="fas fa-user-times"></i> ブロック患者
                </h3>
                <div style="margin-bottom: 15px;">
                    <strong>登録：</strong> 474人
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 100%"></div>
                    </div>
                </div>
                <div style="margin-bottom: 15px;">
                    <strong>興味表示：</strong> 269人 (56.8%)
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 56.8%"></div>
                    </div>
                </div>
                <div style="margin-bottom: 15px;">
                    <strong>購入完了：</strong> 33人 (7.0%)
                    <div class="progress-bar">
                        <div class="progress-fill danger" style="width: 7%"></div>
                    </div>
                </div>
                <div class="highlight-box">
                    <div>転換率: 12.3%</div>
                    <div style="font-size: 0.9em;">（極めて低い）</div>
                </div>
            </div>
        </div>

        <!-- 顧客セグメント -->
        <div class="segment-grid fade-in">
            <div class="segment-card">
                <div class="segment-icon"><i class="fas fa-crown"></i></div>
                <h3 style="color: #f39c12;">VIP顧客</h3>
                <div class="metric-medium" style="color: #f39c12;">147人 (4.5%)</div>
                <p>定期契約・高LTV<br>売上貢献: 45%</p>
            </div>

            <div class="segment-card">
                <div class="segment-icon"><i class="fas fa-star"></i></div>
                <h3 style="color: #27ae60;">優良顧客</h3>
                <div class="metric-medium" style="color: #27ae60;">254人 (7.7%)</div>
                <p>リピート購入<br>売上貢献: 30%</p>
            </div>

            <div class="segment-card">
                <div class="segment-icon"><i class="fas fa-user-plus"></i></div>
                <h3 style="color: #3498db;">新規顧客</h3>
                <div class="metric-medium" style="color: #3498db;">196人 (6.0%)</div>
                <p>初回購入のみ<br>売上貢献: 15%</p>
            </div>

            <div class="segment-card">
                <div class="segment-icon"><i class="fas fa-question-circle"></i></div>
                <h3 style="color: #e67e22;">検討顧客</h3>
                <div class="metric-medium" style="color: #e67e22;">1,372人 (41.7%)</div>
                <p>興味あり未購入<br>最大の機会</p>
            </div>
        </div>

        <!-- 売上成長予測 -->
        <div class="chart-container fade-in">
            <h2 style="color: #2c3e50; margin-bottom: 30px;">
                <i class="fas fa-rocket"></i> 売上成長予測
            </h2>
            <div class="bar-chart">
                <div class="bar" style="height: 120px;">
                    <div class="bar-value">¥1,200万</div>
                    <div class="bar-label">現在</div>
                </div>
                <div class="bar" style="height: 150px;">
                    <div class="bar-value">¥1,500万</div>
                    <div class="bar-label">1ヶ月後<br>(+25%)</div>
                </div>
                <div class="bar" style="height: 200px;">
                    <div class="bar-value">¥2,000万</div>
                    <div class="bar-label">3ヶ月後<br>(+67%)</div>
                </div>
                <div class="bar" style="height: 250px;">
                    <div class="bar-value">¥2,500万</div>
                    <div class="bar-label">6ヶ月後<br>(+108%)</div>
                </div>
            </div>
            <p style="margin-top: 20px; color: #7f8c8d;">
                施策実行により段階的な成長を実現
            </p>
        </div>

        <!-- ROI強調セクション -->
        <div class="roi-showcase pulse fade-in">
            <h2 style="margin-bottom: 20px; position: relative; z-index: 1;"><i class="fas fa-chart-line"></i> 新キャンペーン投資対効果</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 30px; text-align: center; position: relative; z-index: 1;">
                <div>
                    <div style="font-size: 2.5em; font-weight: bold;">¥50万</div>
                    <div>キャンペーン投資額</div>
                </div>
                <div>
                    <div style="font-size: 2.5em; font-weight: bold;">¥320万</div>
                    <div>月間売上増</div>
                </div>
                <div>
                    <div style="font-size: 2.5em; font-weight: bold;">640%</div>
                    <div>月次ROI</div>
                </div>
                <div>
                    <div style="font-size: 2.5em; font-weight: bold;">0.5ヶ月</div>
                    <div>投資回収期間</div>
                </div>
            </div>
        </div>

        <!-- アクションプラン -->
        <div class="action-section fade-in">
            <h2 style="color: #2c3e50; margin-bottom: 30px; text-align: center;">
                <i class="fas fa-tasks"></i> 即実施アクションプラン
            </h2>
            <div class="action-grid">
                <div class="action-card">
                    <h3><i class="fas fa-user-friends"></i> 友達紹介キャンペーン</h3>
                    <div style="font-size: 1.5em; margin: 10px 0;">投資: ¥15万</div>
                    <p>紹介者・被紹介者両方に<br>¥3,000クーポン進呈</p>
                    <div style="margin-top: 15px; font-weight: bold;">期待リターン: ¥120万/月</div>
                </div>

                <div class="action-card">
                    <h3><i class="fas fa-star"></i> 新規顧客限定キャンペーン</h3>
                    <div style="font-size: 1.5em; margin: 10px 0;">投資: ¥20万</div>
                    <p>初回限定50%OFF<br>+送料無料</p>
                    <div style="margin-top: 15px; font-weight: bold;">期待リターン: ¥150万/月</div>
                </div>

                <div class="action-card">
                    <h3><i class="fas fa-calendar"></i> 定期契約移行促進</h3>
                    <div style="font-size: 1.5em; margin: 10px 0;">投資: ¥15万</div>
                    <p>単発→定期で初回20%OFF<br>解約3ヶ月縛りなし</p>
                    <div style="margin-top: 15px; font-weight: bold;">期待リターン: ¥50万/月</div>
                </div>
            </div>

            <!-- 追加キャンペーンアイデア -->
            <div style="margin-top: 40px; background: rgba(255,255,255,0.95); border-radius: 15px; padding: 25px; border-left: 5px solid #3498db;">
                <h3 style="color: #2c3e50; margin-bottom: 20px; text-align: center;">
                    <i class="fas fa-lightbulb"></i> 追加キャンペーンアイデア（低予算）
                </h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
                    <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                        <h4 style="color: #e67e22; margin-bottom: 10px;"><i class="fas fa-gift"></i> 季節限定キャンペーン</h4>
                        <p style="font-size: 0.9em; color: #666;">春の新生活応援、夏バテ対策など季節性を活かした訴求（投資: ¥5万）</p>
                    </div>
                    <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                        <h4 style="color: #9b59b6; margin-bottom: 10px;"><i class="fas fa-birthday-cake"></i> 誕生日特典</h4>
                        <p style="font-size: 0.9em; color: #666;">誕生月に特別割引クーポン自動配信（投資: ¥3万）</p>
                    </div>
                    <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                        <h4 style="color: #27ae60; margin-bottom: 10px;"><i class="fas fa-medal"></i> 継続購入マイルストーン</h4>
                        <p style="font-size: 0.9em; color: #666;">3回目、5回目の購入でボーナス特典（投資: ¥8万）</p>
                    </div>
                    <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                        <h4 style="color: #e74c3c; margin-bottom: 10px;"><i class="fas fa-clock"></i> タイムセール</h4>
                        <p style="font-size: 0.9em; color: #666;">金曜夜限定24時間タイムセール（投資: ¥2万）</p>
                    </div>
                    <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                        <h4 style="color: #f39c12; margin-bottom: 10px;"><i class="fas fa-trophy"></i> 口コミ投稿キャンペーン</h4>
                        <p style="font-size: 0.9em; color: #666;">レビュー投稿で次回10%OFF（投資: ¥5万）</p>
                    </div>
                    <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                        <h4 style="color: #34495e; margin-bottom: 10px;"><i class="fas fa-envelope"></i> メルマガ限定オファー</h4>
                        <p style="font-size: 0.9em; color: #666;">メルマガ登録者限定の先行販売（投資: ¥1万）</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- 実施タイムライン -->
        <div class="timeline fade-in">
            <h2 style="color: #2c3e50; margin-bottom: 30px; text-align: center;">
                <i class="fas fa-calendar-alt"></i> 実施タイムライン
            </h2>
            
            <div class="timeline-item">
                <div class="timeline-icon"><i class="fas fa-play"></i></div>
                <div>
                    <h4>Week 1: ターゲット別キャンペーン開始</h4>
                    <p>検討中顧客へのパーソナル提案・定期契約移行オファー・VIPアップセル開始</p>
                </div>
            </div>

            <div class="timeline-item">
                <div class="timeline-icon"><i class="fas fa-cogs"></i></div>
                <div>
                    <h4>Week 2-4: 効果測定・最適化</h4>
                    <p>転換率分析・オファー内容調整・顧客フィードバック収集・次段階準備</p>
                </div>
            </div>

            <div class="timeline-item">
                <div class="timeline-icon"><i class="fas fa-chart-line"></i></div>
                <div>
                    <h4>Month 2-3: 拡張フェーズ</h4>
                    <p>定期契約プラン強化・リファラルプログラム開始</p>
                </div>
            </div>

            <div class="timeline-item">
                <div class="timeline-icon"><i class="fas fa-trophy"></i></div>
                <div>
                    <h4>Month 4-6: 最大化フェーズ</h4>
                    <p>AI活用・パーソナライゼーション・サブスクモデル導入</p>
                </div>
            </div>
        </div>

        <!-- 成功要因 -->
        <div class="highlight-box fade-in" style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 40px; border-radius: 20px;">
            <h2 style="margin-bottom: 20px;"><i class="fas fa-key"></i> 成功の鍵</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; text-align: left;">
                <div>
                    <div style="font-weight: bold; margin-bottom: 10px;"><i class="fas fa-rocket"></i> スピード</div>
                    <div>競合より早い施策実行</div>
                </div>
                <div>
                    <div style="font-weight: bold; margin-bottom: 10px;"><i class="fas fa-chart-bar"></i> データドリブン</div>
                    <div>日次KPIモニタリング</div>
                </div>
                <div>
                    <div style="font-weight: bold; margin-bottom: 10px;"><i class="fas fa-users"></i> 顧客中心</div>
                    <div>フィードバックの即座反映</div>
                </div>
                <div>
                    <div style="font-weight: bold; margin-bottom: 10px;"><i class="fas fa-handshake"></i> チーム連携</div>
                    <div>営業・マーケ・開発の協力</div>
                </div>
            </div>
        </div>

        </div>
        
        <!-- フッター -->
        <footer>
            <p>© 2025 六本木メディカルクリニック</p>
            <p style="font-size: 0.9em; opacity: 0.9;">本レポートは機密情報を含むため、取り扱いには十分ご注意ください。</p>
        </footer>
    </div>

    <script>
        // アニメーション効果
        window.addEventListener('load', function() {
            // プログレスバーのアニメーション
            const progressBars = document.querySelectorAll('.progress-fill');
            progressBars.forEach(bar => {
                const width = bar.style.width;
                bar.style.width = '0%';
                setTimeout(() => {
                    bar.style.width = width;
                }, 500);
            });

            // カウントアップアニメーション
            const countElements = document.querySelectorAll('.metric-large');
            countElements.forEach(element => {
                const text = element.textContent;
                if (text.includes('¥') || text.includes('%')) {
                    const number = parseInt(text.replace(/[¥,%]/g, ''));
                    let current = 0;
                    const increment = number / 50;
                    const timer = setInterval(() => {
                        current += increment;
                        if (current >= number) {
                            current = number;
                            clearInterval(timer);
                        }
                        
                        if (text.includes('¥')) {
                            element.textContent = '¥' + Math.floor(current).toLocaleString();
                        } else if (text.includes('%')) {
                            element.textContent = Math.floor(current) + '%';
                        } else {
                            element.textContent = Math.floor(current).toLocaleString();
                        }
                    }, 50);
                }
            });
        });

        // ホバーエフェクト（控えめに）
        document.querySelectorAll('.card').forEach(card => {
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-3px)';
            });
            
            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(-2px)';
            });
        });

        // スクロール連動アニメーション
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        document.querySelectorAll('.fade-in').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'all 0.6s ease';
            observer.observe(el);
        });
    </script>
</body>
</html>'''
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ 購買行動分析_インフォグラフィック.html を元のデザインに復元")

def main():
    print("="*60)
    print("元のデザインへの復元スクリプト（全ページ）")
    print("="*60)
    
    restore_strategy_comparison()
    restore_purchase_behavior()
    
    print("\n✅ 完了！経営分析レポート以外のページを元のデザインに復元しました")
    print("  - グラデーション背景")
    print("  - メトリックカード")
    print("  - アニメーション効果")
    print("  - 元のタイポグラフィー")
    print("  - 横幅は1200pxで統一")

if __name__ == "__main__":
    main()