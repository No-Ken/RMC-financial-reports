#!/usr/bin/env python3
"""
HTMLファイルのスタイルを統一するスクリプト
"""

import os
import re

# html資料ディレクトリのパス
html_dir = '/Users/noriken/Desktop/01_仕事_資料置き場/01_会議資料/明/RMC_財務分析/html資料/'

# 処理対象のHTMLファイル
html_files = [
    'index.html',
    'RMC戦略パターン詳細比較.html',
    'RMC_購入分析_インフォグラフィック.html',
    '購買行動分析_インフォグラフィック.html'
]

# 統一ヘッダーHTML
unified_header = '''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="common-styles.css">
    <style>
        /* ページ固有のスタイル */
        .page-specific {{
            /* 必要に応じて追加 */
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- ヘッダー -->
        <header class="header">
            <h1>六本木メディカルクリニック</h1>
            <p class="subtitle">{subtitle}</p>
            <p class="date">2025年8月 最新データ</p>
            
            <!-- ナビゲーションタブ -->
            <nav class="nav-tabs">
                <ul>
                    <li><a href="./index.html" {nav_index}>経営分析レポート</a></li>
                    <li><a href="./RMC戦略パターン詳細比較.html" {nav_strategy}>戦略パターン比較</a></li>
                    <li><a href="./RMC_購入分析_インフォグラフィック.html" {nav_purchase}>購入分析</a></li>
                    <li><a href="./購買行動分析_インフォグラフィック.html" {nav_behavior}>購買行動分析</a></li>
                </ul>
            </nav>
        </header>
'''

# ページごとの設定
page_configs = {
    'index.html': {
        'title': '六本木メディカルクリニック 経営分析レポート',
        'subtitle': '経営KPI総合ダッシュボード',
        'nav_active': 'nav_index'
    },
    'RMC戦略パターン詳細比較.html': {
        'title': 'RMC 戦略パターン詳細比較',
        'subtitle': '複数シナリオの収益性・効率性分析',
        'nav_active': 'nav_strategy'
    },
    'RMC_購入分析_インフォグラフィック.html': {
        'title': 'RMC 購入分析インフォグラフィック',
        'subtitle': '商品別売上とセグメント分析',
        'nav_active': 'nav_purchase'
    },
    '購買行動分析_インフォグラフィック.html': {
        'title': 'RMC 購買行動分析',
        'subtitle': '顧客行動パターンとLTV分析',
        'nav_active': 'nav_behavior'
    }
}

def update_html_file(filename):
    """HTMLファイルを統一スタイルで更新"""
    filepath = os.path.join(html_dir, filename)
    
    if not os.path.exists(filepath):
        print(f"⚠️  {filename} が見つかりません")
        return False
    
    try:
        # ファイルを読み込み
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 設定を取得
        config = page_configs.get(filename, {})
        
        # ナビゲーションのアクティブ状態を設定
        nav_states = {
            'nav_index': '',
            'nav_strategy': '',
            'nav_purchase': '',
            'nav_behavior': ''
        }
        active_nav = config.get('nav_active', '')
        if active_nav:
            nav_states[active_nav] = 'class="active"'
        
        # ヘッダーを生成
        new_header = unified_header.format(
            title=config.get('title', 'RMC レポート'),
            subtitle=config.get('subtitle', ''),
            **nav_states
        )
        
        # 既存のコンテンツから本文部分を抽出
        # <body>タグ以降のコンテンツを取得
        body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
        if body_match:
            body_content = body_match.group(1)
            
            # containerクラスの内容を抽出
            container_match = re.search(r'<div class="container"[^>]*>(.*?)</div>\s*(?:</body>|$)', body_content, re.DOTALL)
            if container_match:
                inner_content = container_match.group(1)
                
                # ヘッダー部分を除去して本文のみ取得
                # 既存のheaderやnavを除去
                inner_content = re.sub(r'<header[^>]*>.*?</header>', '', inner_content, flags=re.DOTALL)
                inner_content = re.sub(r'<nav class="nav-tabs"[^>]*>.*?</nav>', '', inner_content, flags=re.DOTALL)
                inner_content = re.sub(r'<div class="header"[^>]*>.*?</div>\s*(?=<div|<section|<main)', '', inner_content, flags=re.DOTALL)
            else:
                # containerがない場合は全体を使用
                inner_content = body_content
        else:
            print(f"⚠️  {filename} の本文を抽出できませんでした")
            return False
        
        # 新しいHTMLを生成
        new_html = new_header + '''
        <!-- メインコンテンツ -->
        <div class="content">
''' + inner_content + '''
        </div>
        
        <!-- フッター -->
        <footer class="footer">
            <p>© 2025 六本木メディカルクリニック</p>
            <p>本レポートは機密情報を含むため、取り扱いには十分ご注意ください。</p>
        </footer>
    </div>
</body>
</html>'''
        
        # ファイルを書き込み
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        
        print(f"✅ {filename} のスタイルを統一しました")
        return True
        
    except Exception as e:
        print(f"❌ {filename} の処理中にエラー: {e}")
        return False

def main():
    print("="*60)
    print("HTMLファイルのスタイル統一スクリプト")
    print("="*60)
    print(f"対象ディレクトリ: {html_dir}\n")
    
    updated_count = 0
    for filename in html_files:
        if update_html_file(filename):
            updated_count += 1
    
    print("\n" + "="*60)
    print(f"処理完了: {updated_count}個のファイルを更新しました")
    print("\n📋 統一された要素:")
    print("  ✅ ヘッダーデザイン")
    print("  ✅ ナビゲーションタブ")
    print("  ✅ コンテナ幅 (max-width: 1200px)")
    print("  ✅ カラースキーム")
    print("  ✅ フォント設定")
    print("  ✅ レスポンシブ対応")

if __name__ == "__main__":
    main()