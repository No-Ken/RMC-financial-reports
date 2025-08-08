#!/usr/bin/env python3
"""
HTMLファイルのデザイン問題を修正するスクリプト
- 重複したナビゲーション要素の削除
- 壊れたスタイルの修正
- Chart.jsグラフの修正
"""

import os
import re

# html資料ディレクトリのパス
html_dir = '/Users/noriken/Desktop/01_仕事_資料置き場/01_会議資料/明/RMC_財務分析/html資料/'

def fix_index_html():
    """index.htmlの修正"""
    filepath = os.path.join(html_dir, 'index.html')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 重複したナビゲーションタブを削除（最初のheader内のものだけ残す）
    # contentクラス内の古いナビゲーションタブを削除
    content = re.sub(
        r'<div class="content">.*?<div class="nav-tabs">.*?</div>\s*(?=<div class="page"|<!-- ヘッダー -->)',
        '<div class="content">\n',
        content,
        flags=re.DOTALL
    )
    
    # 重複したヘッダー要素を削除
    content = re.sub(
        r'<!-- ヘッダー -->\s*<div class="date">.*?</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # バーチャートのスタイルを修正
    if 'bar-chart' in content and 'display: flex' not in content:
        bar_chart_style = """
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
            width: 60px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px 10px 0 0;
            position: relative;
            transition: all 0.3s ease;
        }
        
        .bar:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }
        
        .bar-value {
            position: absolute;
            top: -30px;
            left: 50%;
            transform: translateX(-50%);
            font-weight: bold;
            color: #667eea;
            white-space: nowrap;
        }
        
        .bar-label {
            position: absolute;
            bottom: -25px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 0.9em;
            color: #6b7280;
            white-space: nowrap;
        }"""
        
        # スタイルセクションに追加
        content = content.replace('</style>', bar_chart_style + '\n    </style>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ index.html を修正しました")

def fix_strategy_comparison():
    """RMC戦略パターン詳細比較.htmlの修正"""
    filepath = os.path.join(html_dir, 'RMC戦略パターン詳細比較.html')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 重複したナビゲーションを削除
    content = re.sub(
        r'<div class="content">.*?<div class="nav-tabs">.*?</div>.*?(?=<div class="container mx-auto|<section)',
        '<div class="content">\n',
        content,
        flags=re.DOTALL
    )
    
    # containerクラスの重複を修正
    content = re.sub(
        r'<div class="container">.*?<div class="max-w-7xl mx-auto">',
        '<div class="container">\n        <div class="content">',
        content,
        count=1,
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ RMC戦略パターン詳細比較.html を修正しました")

def fix_purchase_analysis():
    """RMC_購入分析_インフォグラフィック.htmlの修正"""
    filepath = os.path.join(html_dir, 'RMC_購入分析_インフォグラフィック.html')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 重複したナビゲーション削除
    content = re.sub(
        r'<div class="content">.*?<div class="max-w-7xl mx-auto">.*?<div class="nav-tabs">.*?</div>',
        '<div class="content">',
        content,
        count=1,
        flags=re.DOTALL
    )
    
    # Chart.jsの初期化を修正
    if 'new Chart(' in content and 'DOMContentLoaded' not in content:
        # スクリプトタグを探して修正
        content = re.sub(
            r'<script>\s*document\.addEventListener',
            '<script>\n        document.addEventListener(\'DOMContentLoaded\', function() {\n            document.addEventListener',
            content
        )
        
        # 最後のスクリプトタグにも終了タグを追加
        content = re.sub(
            r'</script>$',
            '        });\n    </script>',
            content
        )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ RMC_購入分析_インフォグラフィック.html を修正しました")

def fix_behavior_analysis():
    """購買行動分析_インフォグラフィック.htmlの修正"""
    filepath = os.path.join(html_dir, '購買行動分析_インフォグラフィック.html')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 重複したナビゲーション削除  
    content = re.sub(
        r'<div class="content">.*?<div class="container">.*?<div class="nav-tabs">.*?</div>',
        '<div class="content">',
        content,
        count=1,
        flags=re.DOTALL
    )
    
    # KPIカードのグリッドスタイルを確認
    if 'kpi-grid' in content and 'display: grid' not in content:
        kpi_grid_style = """
        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        
        .kpi-card {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .kpi-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        }"""
        
        content = content.replace('</style>', kpi_grid_style + '\n    </style>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 購買行動分析_インフォグラフィック.html を修正しました")

def main():
    print("="*60)
    print("HTMLファイルのデザイン修正スクリプト")
    print("="*60)
    print(f"対象ディレクトリ: {html_dir}\n")
    
    # 各HTMLファイルを修正
    fix_index_html()
    fix_strategy_comparison()
    fix_purchase_analysis()
    fix_behavior_analysis()
    
    print("\n" + "="*60)
    print("修正完了！")
    print("\n修正内容:")
    print("  ✅ 重複したナビゲーション要素の削除")
    print("  ✅ バーチャートのスタイル修正")
    print("  ✅ Chart.jsの初期化修正")
    print("  ✅ KPIグリッドのスタイル修正")
    print("  ✅ コンテナクラスの重複解消")

if __name__ == "__main__":
    main()