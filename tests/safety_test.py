import json
import os

def test_crisis_keywords():
    # 相対パスで読み込み
    base_dir = os.path.dirname(os.path.abspath(__file__))
    locale_path = os.path.join(base_dir, '..', 'config', 'locales', 'ja.json')
    
    with open(locale_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        assert len(data['crisis_keywords']) > 0
        assert 'emergency_contacts' in data
        print("Crisis keywords test passed")

if __name__ == "__main__":
    test_crisis_keywords()
