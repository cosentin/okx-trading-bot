# OKX AI Trading Bot 🤖

Advanced AI trading bot for OKX exchange with risk management.

## Features
- ✅ AI-powered trading signals
- ✅ 1% risk management with 2% recovery
- ✅ 50% drawdown auto-stop
- ✅ Mobile-friendly dashboard
- ✅ Multi-exchange support (OKX, Binance, Bitget)

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
cp config/config_template.py config/config.py
# Edit config.py with your API keys
RUN BOT
python src/main.py
LICENSE

---

## 📤 **STEP 7: PUSH KE GITHUB**

### **Inisialisasi Git:**
```bash
cd okx-bot-github

# Initialize git
git init

# Add all files
git add .

# First commit
git commit -m "Initial commit: AI Trading Bot for OKX"

# Link ke GitHub repository
git remote add origin https://github.com/username/okx-trading-bot.git

# Push ke GitHub
git push -u origin main

jika error tentang brench
git branch -M main
git push -u origin main

clone repository
cd ~
git clone https://github.com/username/okx-trading-bot.git
cd okx-trading-bot

# Setup configuration
cp config/config_template.py config/config.py
nano config/config.py  # Edit dengan API keys

Install & run
# Install dependencies
pip install -r requirements.txt

# Run setup script
chmod +x scripts/setup_android.sh
./scripts/setup_android.sh

# Run bot
python src/main.py

jangan commit api keys
# Pastikan config.py ada di .gitignore
git status  # Cek config.py tidak terlist

# Jika terlanjur commit API keys:
git rm --cached config/config.py
git commit -m "Remove config with API keys"
git push

Gunakan environment variables
# config_template.py
import os

class OKXConfig:
    API_KEY = os.getenv('OKX_API_KEY', 'YOUR_API_KEY_HERE')
    SECRET_KEY = os.getenv('OKX_SECRET_KEY', 'YOUR_SECRET_KEY_HERE')

Update code
# Edit file yang diperlukan
nano src/bot_core.py

# Commit perubahan
git add .
git commit -m "Improve AI signal accuracy"

# Push ke GitHub
git push

pull update di hp
cd okx-trading-bot
git pull origin main

# Restart bot dengan update terbaru
pkill -f main.py
python src/main.py
jalankan
chmod +x scripts/git_helper.sh
./git_helper.sh update
