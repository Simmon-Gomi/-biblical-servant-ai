#!/usr/bin/env python3
"""
Safety test for Biblical Servant AI
Tests crisis keywords and emergency contacts in locale files
"""

import json
import sys
from pathlib import Path

def test_locale_file(locale: str) -> bool:
    """Test a specific locale file for required safety features"""
    try:
        # プロジェクトルートからの相対パス
        base_dir = Path(__file__).resolve().parent.parent
        locale_path = base_dir / "config" / "locales" / f"{locale}.json"
        
        # ファイル存在確認
        if not locale_path.exists():
            print(f"⚠️  Warning: {locale}.json not found at {locale_path}")
            return False
        
        # JSON読み込み
        with locale_path.open(encoding="utf-8") as f:
            data = json.load(f)
        
        # 必須フィールドの確認
        errors = []
        
        if "crisis_keywords" not in data:
            errors.append(f"{locale}: Missing 'crisis_keywords' field")
        elif not data["crisis_keywords"]:
            errors.append(f"{locale}: 'crisis_keywords' list is empty")
        elif len(data["crisis_keywords"]) < 5:
            errors.append(f"{locale}: Only {len(data['crisis_keywords'])} crisis keywords (minimum 5 recommended)")
        
        if "emergency_contacts" not in data:
            errors.append(f"{locale}: Missing 'emergency_contacts' field")
        elif not data["emergency_contacts"]:
            errors.append(f"{locale}: 'emergency_contacts' is empty")
        
        # エラーがあれば表示
        if errors:
            for error in errors:
                print(f"❌ {error}")
            return False
        
        # 成功メッセージ
        print(f"✅ {locale}.json passed all safety checks")
        print(f"   - {len(data['crisis_keywords'])} crisis keywords")
        print(f"   - {len(data['emergency_contacts'])} emergency contacts")
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ {locale}.json: Invalid JSON format - {e}")
        return False
    except Exception as e:
        print(f"❌ {locale}.json: Unexpected error - {e}")
        return False

def main():
    """Main test runner"""
    print("=== Biblical Servant AI Safety Tests ===\n")
    
    # テストする言語のリスト
    locales_to_test = ["ja", "en"]
    results = []
    
    for locale in locales_to_test:
        print(f"Testing {locale}.json...")
        results.append(test_locale_file(locale))
        print()
    
    # 最終結果
    if all(results):
        print("✅ All safety tests passed!")
        sys.exit(0)
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
