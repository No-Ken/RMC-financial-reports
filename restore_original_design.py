#!/usr/bin/env python3
"""
経営分析レポート以外のページを元のデザインに復元
横幅は統一したまま、タイポグラフィーや図形などのビジュアル要素を復元
"""

import os

html_dir = '/Users/noriken/Desktop/01_仕事_資料置き場/01_会議資料/明/RMC_財務分析/html資料/'

# 元のスタイル（グラデーション、カード、アニメーションなど）
original_styles = """
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Noto Sans JP', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        .glass {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            transition: transform 0.3s ease;
        }
        .metric-card:hover {
            transform: translateY(-5px);
        }
        .status-excellent { background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); }
        .status-good { background: linear-gradient(135deg, #56CCF2 0%, #2F80ED 100%); }
        .status-warning { background: linear-gradient(135deg, #F2994A 0%, #F27121 100%); }
        .status-danger { background: linear-gradient(135deg, #EB5757 0%, #D13D3D 100%); }
        
        @keyframes slideIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-slide { animation: slideIn 0.5s ease-out; }
        
        .chart-container {
            position: relative;
            height: 400px;
            width: 100%;
            margin: 20px 0;
        }
        
        .chart-wrapper {
            position: relative;
            height: 280px;
            width: 100%;
        }
        
        .kpi-icon {
            font-size: 2rem;
            margin-bottom: 10px;
        }
        
        .growth-indicator {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: bold;
        }
        
        .growth-up { background: #10B981; color: white; }
        .growth-down { background: #EF4444; color: white; }
        
        /* ナビゲーションタブ - 統一デザインを維持 */
        .nav-tabs {
            background: rgba(255, 255, 255, 0.95);
            padding: 15px 0;
            margin: 20px 0;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        
        .nav-tabs ul {
            list-style: none;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
            padding: 0 20px;
        }
        
        .nav-tabs li {
            display: inline-block;
        }
        
        .nav-tabs a {
            display: inline-block;
            padding: 10px 20px;
            background: rgba(255, 255, 255, 0.2);
            color: white;
            text-decoration: none;
            border-radius: 25px;
            transition: all 0.3s ease;
            font-size: 0.95em;
        }
        
        .nav-tabs a:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-2px);
        }
        
        .nav-tabs a.active {
            background: white;
            color: #667eea;
            font-weight: bold;
        }
        
        /* ヘッダー - グラデーション背景 */
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 60px 40px;
            text-align: center;
            border-radius: 20px 20px 0 0;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 300;
            letter-spacing: 2px;
        }
        
        .header .subtitle {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .header .date {
            margin-top: 20px;
            font-size: 1em;
            opacity: 0.8;
        }
    </style>"""

def restore_purchase_analysis():
    """購入分析ページを元のデザインに復元"""
    filepath = os.path.join(html_dir, 'RMC_購入分析_インフォグラフィック.html')
    
    # 元のデザインHTMLを再構築
    html_content = '''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RMC購入分析ダッシュボード - 経営インフォグラフィック</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
''' + original_styles + '''
</head>
<body>
    <div class="container">
        <!-- ヘッダー -->
        <header class="header">
            <h1>六本木メディカルクリニック</h1>
            <p class="subtitle">購入分析ダッシュボード</p>
            <p class="date">2025年8月 最新データ</p>
            
            <!-- ナビゲーションタブ -->
            <nav class="nav-tabs">
                <ul>
                    <li><a href="./index.html">経営分析レポート</a></li>
                    <li><a href="./RMC戦略パターン詳細比較.html">戦略パターン比較</a></li>
                    <li><a href="./RMC_購入分析_インフォグラフィック.html" class="active">購入分析</a></li>
                    <li><a href="./購買行動分析_インフォグラフィック.html">購買行動分析</a></li>
                </ul>
            </nav>
        </header>
        
        <!-- メインコンテンツ -->
        <div style="padding: 40px;">
            <!-- ヘッダー -->
            <div class="glass p-8 mb-6 animate-slide">
                <h1 class="text-4xl font-bold text-gray-800 mb-2">RMC購入分析ダッシュボード</h1>
                <p class="text-gray-600">2024年9月 - 2025年8月 | 総合経営分析レポート</p>
                <div class="flex gap-4 mt-4">
                    <span class="px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm">リアルタイムデータ</span>
                    <span class="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm">最終更新: 2025/08/08</span>
                </div>
            </div>

            <!-- 主要KPIカード -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
                <div class="metric-card status-good animate-slide" style="animation-delay: 0.1s">
                    <div class="kpi-icon">💰</div>
                    <h3 class="text-sm opacity-90">ARPU(平均購入単価)</h3>
                    <p class="text-3xl font-bold">¥23,004</p>
                    <span class="growth-indicator growth-up">一回購入平均</span>
                </div>
                
                <div class="metric-card status-excellent animate-slide" style="animation-delay: 0.2s">
                    <div class="kpi-icon">🔄</div>
                    <h3 class="text-sm opacity-90">リピート率</h3>
                    <p class="text-3xl font-bold">42.5%</p>
                    <span class="growth-indicator growth-up">優秀</span>
                </div>
                
                <div class="metric-card status-warning animate-slide" style="animation-delay: 0.3s">
                    <div class="kpi-icon">💎</div>
                    <h3 class="text-sm opacity-90">顧客生涯価値(LTV)</h3>
                    <p class="text-3xl font-bold">¥40,369</p>
                    <span class="text-xs">過去実績ベース</span>
                </div>
                
                <div class="metric-card status-danger animate-slide" style="animation-delay: 0.4s">
                    <div class="kpi-icon">📉</div>
                    <h3 class="text-sm opacity-90">離脱率</h3>
                    <p class="text-3xl font-bold">72.1%</p>
                    <span class="text-xs">要改善</span>
                </div>
            </div>

            <!-- 売上推移グラフ -->
            <div class="glass p-6 mb-6 animate-slide" style="animation-delay: 0.5s">
                <h2 class="text-2xl font-bold text-gray-800 mb-4">📈 月次売上推移</h2>
                <div class="chart-wrapper">
                    <canvas id="salesChart"></canvas>
                </div>
                <div class="mt-4 grid grid-cols-2 gap-4">
                    <div class="bg-gradient-to-r from-purple-50 to-pink-50 rounded-lg p-4">
                        <p class="text-sm text-gray-600">2024/9-2025/3 総売上</p>
                        <p class="text-2xl font-bold text-purple-600">¥55,654,210</p>
                    </div>
                    <div class="bg-gradient-to-r from-blue-50 to-cyan-50 rounded-lg p-4">
                        <p class="text-sm text-gray-600">2025/4-2025/8 総売上</p>
                        <p class="text-2xl font-bold text-blue-600">¥72,048,680</p>
                    </div>
                </div>
            </div>

            <!-- 商品別売上構成 -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
                <div class="glass p-6 animate-slide" style="animation-delay: 0.6s">
                    <h2 class="text-2xl font-bold text-gray-800 mb-4">📦 商品別売上構成</h2>
                    <div class="chart-wrapper">
                        <canvas id="productChart"></canvas>
                    </div>
                    <div class="mt-4">
                        <div class="bg-red-50 border-l-4 border-red-400 p-3 rounded">
                            <p class="text-sm text-red-800">⚠️ マンジャロへの依存度85.4%</p>
                            <p class="text-xs text-red-600 mt-1">リスク分散が必要</p>
                        </div>
                    </div>
                </div>
                
                <div class="glass p-6 animate-slide" style="animation-delay: 0.7s">
                    <h2 class="text-2xl font-bold text-gray-800 mb-4">👥 顧客セグメント分析</h2>
                    <div class="chart-wrapper">
                        <canvas id="segmentChart"></canvas>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // 月次売上推移グラフ
            const salesCanvas = document.getElementById('salesChart');
            if (salesCanvas) {
                const salesCtx = salesCanvas.getContext('2d');
                new Chart(salesCtx, {
                    type: 'line',
                    data: {
                        labels: ['2024/9', '2024/10', '2024/11', '2024/12', '2025/1', '2025/2', '2025/3', '2025/4', '2025/5', '2025/6', '2025/7', '2025/8'],
                        datasets: [{
                            label: '月次売上',
                            data: [1266630, 2021110, 1835670, 7000530, 13254510, 15230530, 14221550, 18873120, 17050540, 15526580, 14262380, 3105570],
                            backgroundColor: 'rgba(102, 126, 234, 0.1)',
                            borderColor: 'rgba(102, 126, 234, 1)',
                            borderWidth: 3,
                            fill: true,
                            tension: 0.4
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                display: false
                            }
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                ticks: {
                                    callback: function(value) {
                                        return '¥' + (value/1000000).toFixed(1) + 'M';
                                    }
                                }
                            }
                        }
                    }
                });
            }

            // 商品別売上構成
            const productCanvas = document.getElementById('productChart');
            if (productCanvas) {
                const productCtx = productCanvas.getContext('2d');
                new Chart(productCtx, {
                    type: 'doughnut',
                    data: {
                        labels: ['マンジャロ', 'スーグラ', 'リベルサス', 'オゼンピック', 'その他'],
                        datasets: [{
                            data: [85.4, 6.9, 5.0, 2.1, 0.6],
                            backgroundColor: [
                                'rgba(239, 68, 68, 0.8)',
                                'rgba(59, 130, 246, 0.8)',
                                'rgba(34, 197, 94, 0.8)',
                                'rgba(251, 146, 60, 0.8)',
                                'rgba(156, 163, 175, 0.8)'
                            ],
                            borderWidth: 2,
                            borderColor: '#fff'
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                position: 'bottom'
                            }
                        }
                    }
                });
            }

            // 顧客セグメント
            const segmentCanvas = document.getElementById('segmentChart');
            if (segmentCanvas) {
                const segmentCtx = segmentCanvas.getContext('2d');
                new Chart(segmentCtx, {
                    type: 'doughnut',
                    data: {
                        labels: ['新規顧客', '離脱リスク', 'VIP顧客', '休眠顧客', '安定顧客', 'ロイヤル顧客'],
                        datasets: [{
                            data: [30.4, 30.0, 16.2, 9.6, 9.4, 4.4],
                            backgroundColor: [
                                'rgba(59, 130, 246, 0.8)',
                                'rgba(239, 68, 68, 0.8)',
                                'rgba(168, 85, 247, 0.8)',
                                'rgba(156, 163, 175, 0.8)',
                                'rgba(34, 197, 94, 0.8)',
                                'rgba(251, 146, 60, 0.8)'
                            ],
                            borderWidth: 3,
                            borderColor: '#fff'
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        cutout: '45%',
                        plugins: {
                            legend: {
                                position: 'bottom'
                            }
                        }
                    }
                });
            }
        });
    </script>
</body>
</html>'''
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ RMC_購入分析_インフォグラフィック.html を元のデザインに復元")

def main():
    print("="*60)
    print("元のデザインへの復元スクリプト")
    print("="*60)
    
    restore_purchase_analysis()
    
    print("\n✅ 完了！")
    print("  - グラデーション背景")
    print("  - メトリックカード")
    print("  - アニメーション効果")
    print("  - Tailwindスタイル")
    print("  - 横幅は1200pxで統一")

if __name__ == "__main__":
    main()