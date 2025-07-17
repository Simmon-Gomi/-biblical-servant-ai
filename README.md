# Biblical Study Assistant "Servant"

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-v1.0.0-blue)](https://github.com/YOUR-USERNAME/biblical-servant-ai)
[![Maintenance](https://img.shields.io/badge/Maintained-Yes-green)](https://github.com/YOUR-USERNAME/biblical-servant-ai)

**A Safe AI Prompt System Subordinate to Church Authority**

English | [日本語](README_ja.md)

</div>

## 📖 Overview

"Servant" is an AI prompt system designed to assist with biblical study. This system is completely subordinate to church authority and does not replace human spiritual leaders.

### ✨ Features

- 🔍 **Scripture Search** - Search for verses by keywords or situations
- 📚 **Background Information** - Objective historical and cultural context
- ⛪ **Church Integration** - Access to local church activity information
- 🚨 **Built-in Safety** - Time limits and crisis response (see [Safety Features](#-safety-features))
- 🌏 **Multi-language Support** - Japanese and English (expandable)

## 🎯 Core Principles

1. **Subordination** - The AI is a tool completely subordinate to church authority
2. **Limitations** - No spiritual advice, biblical interpretation, or prayer substitution
3. **Bridge** - Always encourages consultation with human spiritual leaders
4. **Safety** - Prioritizes dependency prevention and crisis response

## 🚀 Quick Start

### Prerequisites

- Compatible AI platform (ChatGPT, Claude, etc.)
- Church leadership approval
- Basic configuration knowledge

### Installation

```bash
# Clone the repository (replace YOUR-USERNAME with your GitHub username)
git clone https://github.com/YOUR-USERNAME/biblical-servant-ai.git
cd biblical-servant-ai

# Copy configuration file
cp config/church_config_template.json config/church_config.json

# Edit church information
# Linux/Mac: nano config/church_config.json
# Windows: notepad config/church_config.json
# Or use any text editor (VSCode, Sublime Text, etc.)
```

### Basic Configuration

Edit `config/church_config.json`:

```json
{
  "church_name": "Your Church Name",
  "pastor_name": "Pastor Name",
  "church_contact": "+1-234-567-8900",
  "preferred_translation": "ESV",
  "session_timeout": 15,
  "language": "en",
  "timezone": "America/New_York"
}
```

### Language Customization

The system supports multiple languages through locale files:
- English: `config/locales/en.json`
- Japanese: `config/locales/ja.json`

To add a new language, create a new locale file following the existing format.

### Getting Started

1. Start a new chat on your AI platform
2. Set the contents of `prompts/servant_core.md` (or `servant_core_ja.md` for Japanese) as the system prompt
3. Begin operation according to church guidelines

## 📋 Feature Details

### 1. Scripture Search
- Keyword search (love, hope, forgiveness, etc.)
- Situational search (8 categories)
- Multiple translation support

### 2. Background Information
- Historical background
- Literary features
- Cultural context
※ No interpretation included

### 3. Church Activity Guide
- Regular meeting information
- Special event announcements
- Contact information

## 🛡️ Safety Features

| Feature | Description | Setting |
|---------|-------------|---------|
| Session Limit | Auto-ends after 15 minutes | Fixed |
| Daily Limit | Max 3 sessions/day | Fixed |
| Crisis Response | Immediately displays emergency contacts | Customizable |
| Log Management | Auto-deletes after 24 hours | Fixed |

## ❌ What This System Does NOT Do

- Spiritual guidance or counseling
- Biblical interpretation or doctrinal explanation
- Personal prayer provision
- Life advice or counsel
- Declaration of forgiveness

## 📚 Documentation

- [Theological Foundation](docs/theology_core.md)
- [Safety and Privacy](docs/safety_privacy.md)
- [Administrator Guide](docs/admin_guide.md)
- [Contributing Guidelines](CONTRIBUTING.md)

## 🤝 Contributing

We welcome contributions to this project. However:
- Maintain theological soundness
- Respect AI limitations
- Preserve subordination to church authority

See [Contributing Guidelines](CONTRIBUTING.md) for details.

## 📜 License

This project is released under the [MIT License](LICENSE).

## ⚖️ Legal Compliance

This system is designed to comply with:
- **GDPR** (EU General Data Protection Regulation)
- **CCPA** (California Consumer Privacy Act)
- **Personal Information Protection Act** (Japan, Reiwa 5 Amendment)
- Other applicable privacy laws in your jurisdiction

Key privacy features:
- No personal data storage
- Logs auto-delete within 24 hours
- Usage purpose: Safety feature verification only

## 📖 About Bible Quotations

Follow each Bible translation's copyright guidelines. Many publishers allow quotations up to 500 verses per day without permission¹, but please verify with specific publishers.

## 🏥 Emergency Contacts

**Global Resources:**
- International Association for Suicide Prevention: [iasp.info](https://iasp.info/resources/Crisis_Centres/)

**Regional Examples (customize in your locale file):**
- **USA**: Crisis Hotline 988
- **Japan**: いのちの電話 (Inochi no Denwa) 0120-783-556
- **UK**: Samaritans 116 123
- **Church Emergency**: Set by each church in configuration

For other regions, see `config/locales/` to add local emergency contacts.

## 🙏 Final Words

> "For even the Son of Man came not to be served but to serve,
> and to give his life as a ransom for many."
> 
> — Mark 10:45 (ESV)

We hope this system will serve churches and connect people
to living faith communities.

---

¹ Based on general publisher guidelines. Specific limits:
- [ESV Permissions](https://www.crossway.org/permissions/): 1,000 verses
- [NIV Permissions](https://www.zondervan.com/permissions): 500 verses
- NRSV: 500 verses
- KJV: Public Domain (no limit)

## 📧 Contact

- Technical Questions: [Issues](../../issues)
- Theological Questions: Your local church
- Emergency Support: See emergency contacts above

## 💡 Intended Users

This system is designed for:
- Churches seeking safe AI integration
- Biblical study groups under church oversight
- Individual believers with pastoral guidance

## 🔒 Security

- No personal data storage
- Session data encrypted in transit (requires HTTPS/TLS)
- Church-only access recommended
- Regular security audits advised

## 🌐 Deployment

Recommended platforms:
- Local church servers
- Private cloud instances
- Secure AI platforms with API access

## 📝 Changelog

See [Releases](../../releases) for version history.

## 🙏 Acknowledgments

- All contributing churches and pastors
- Open source community
- Biblical translation societies

---

*"Your word is a lamp to my feet and a light to my path." - Psalm 119:105*

⭐ If you find this project helpful, consider starring it for visibility.
```
