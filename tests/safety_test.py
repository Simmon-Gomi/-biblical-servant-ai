import json
import os
import pathlib

def test_crisis_keywords():
    """危機キーワードの存在を確認するテスト"""
    # プロジェクトルートからの相対パスを解決
    current_dir = pathlib.Path(__file__).parent
    locale_path = current_dir / '..' / 'config' / 'locales' / 'ja.json'
    
    # JSONファイルを読み込み
    with locale_path.open(encoding='utf-8') as f:
        data = json.load(f)
    
    # アサーション
    assert 'crisis_keywords' in data, "crisis_keywordsが存在しません"
    assert len(data['crisis_keywords']) > 0, "crisis_keywordsが空です"
    assert 'emergency_contacts' in data, "emergency_contactsが存在しません"
    
    print("✓ Crisis keywords test passed")

if __name__ == "__main__":
    test_crisis_keywords()
