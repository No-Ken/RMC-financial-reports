#!/usr/bin/env python3
"""
すべてのHTMLファイルのグラフィック問題を完全に修正
"""

import os
import re

html_dir = '/Users/noriken/Desktop/01_仕事_資料置き場/01_会議資料/明/RMC_財務分析/html資料/'

# Chart.js CDNリンク（すべてのファイルで必要）
chartjs_cdn = '<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>'

def ensure_chartjs_cdn(content):
    """Chart.js CDNリンクを確実に追加"""
    if 'cdn.jsdelivr.net/npm/chart.js' not in content:
        # </head>タグの前に追加
        content = content.replace('</head>', f'    {chartjs_cdn}\n</head>')
    return content

def fix_duplicate_elements(content):
    """重複した要素を削除"""
    # 重複したヘッダーを削除（content内にある2つ目のheaderタグ）
    pattern = r'<div class="content">.*?<header[^>]*>.*?</header>'
    matches = re.findall(pattern, content, re.DOTALL)
    if len(matches) > 1:
        # 2つ目のヘッダーを削除
        content = re.sub(
            r'(<div class="content">.*?)<header[^>]*>.*?</header>',
            r'\1',
            content,
            count=1,
            flags=re.DOTALL
        )
    return content

def fix_chartjs_initialization(content):
    """Chart.js初期化の修正"""
    # すでにDOMContentLoadedがある場合はスキップ
    if 'DOMContentLoaded' in content:
        return content
    
    # Chart.jsを使っている場合は初期化を修正
    if 'new Chart(' in content:
        # スクリプトタグ全体を探す
        script_pattern = r'<script>(.*?)</script>'
        
        def wrap_script(match):
            script_content = match.group(1)
            if 'new Chart' in script_content and 'DOMContentLoaded' not in script_content:
                return f'''<script>
    document.addEventListener('DOMContentLoaded', function() {{
{script_content}
    }});
</script>'''
            return match.group(0)
        
        content = re.sub(script_pattern, wrap_script, content, flags=re.DOTALL)
    
    return content

def fix_purchase_analysis():
    """購入分析ページの修正"""
    filepath = os.path.join(html_dir, 'RMC_購入分析_インフォグラフィック.html')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Chart.js CDNを確実に追加
    content = ensure_chartjs_cdn(content)
    
    # 重複要素を削除
    content = fix_duplicate_elements(content)
    
    # Chart.js初期化を修正
    content = fix_chartjs_initialization(content)
    
    # Tailwindクラスが問題を起こしている場合は削除
    content = re.sub(r'class="max-w-7xl mx-auto"', 'style="max-width: 1200px; margin: 0 auto;"', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ RMC_購入分析_インフォグラフィック.html を修正")
    return True

def fix_behavior_analysis():
    """購買行動分析ページの修正"""
    filepath = os.path.join(html_dir, '購買行動分析_インフォグラフィック.html')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Chart.js CDNを確実に追加
    content = ensure_chartjs_cdn(content)
    
    # 重複要素を削除
    content = fix_duplicate_elements(content)
    
    # Chart.js初期化を修正
    content = fix_chartjs_initialization(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 購買行動分析_インフォグラフィック.html を修正")
    return True

def fix_strategy_comparison():
    """戦略比較ページの修正"""
    filepath = os.path.join(html_dir, 'RMC戦略パターン詳細比較.html')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Chart.js CDNを確実に追加（必要な場合）
    if 'Chart(' in content:
        content = ensure_chartjs_cdn(content)
        content = fix_chartjs_initialization(content)
    
    # 重複要素を削除
    content = fix_duplicate_elements(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ RMC戦略パターン詳細比較.html を修正")
    return True

def fix_index():
    """メインページの修正"""
    filepath = os.path.join(html_dir, 'index.html')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # バーチャートのスタイル追加（既存のstyleタグ内に）
    if '.bar-chart' not in content:
        bar_style = '''
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
            margin: 0 5px;
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
            font-size: 0.9em;
        }
        
        .bar-label {
            position: absolute;
            bottom: -25px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 0.85em;
            color: #6b7280;
            white-space: nowrap;
        }'''
        
        # </style>の前に追加
        content = content.replace('</style>', bar_style + '\n    </style>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ index.html を修正")
    return True

def main():
    print("="*60)
    print("HTML完全修正スクリプト")
    print("="*60)
    
    # 各ファイルを修正
    results = []
    results.append(fix_index())
    results.append(fix_strategy_comparison())
    results.append(fix_purchase_analysis())
    results.append(fix_behavior_analysis())
    
    print("\n" + "="*60)
    if all(results):
        print("✅ すべての修正が完了しました！")
    else:
        print("⚠️ 一部のファイルで修正に失敗しました")
    
    print("\n修正内容:")
    print("  ✅ Chart.js CDNリンクの追加")
    print("  ✅ Chart.js初期化の修正（DOMContentLoaded）")
    print("  ✅ 重複要素の削除")
    print("  ✅ バーチャートスタイルの追加")
    print("  ✅ Tailwindクラスの問題修正")

if __name__ == "__main__":
    main()