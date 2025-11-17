# config_template.py
# COPY THIS FILE TO config.py AND ADD YOUR API KEYS

class OKXConfig:
    EXCHANGE = 'okx'
    SYMBOL = 'BTC/USDT'
    TIMEFRAME = '1m'
    
    # ⚠️ ADD YOUR API KEYS HERE AFTER COPYING
    API_KEY = 'YOUR_API_KEY_HERE'
    SECRET_KEY = 'YOUR_SECRET_KEY_HERE'
    PASSPHRASE = 'YOUR_PASSPHRASE_HERE'
    
    # Trading Parameters
    INITIAL_RISK_PERCENT = 10.0
    RECOVERY_RISK_PERCENT = 20.0
    PROFIT_TARGET_PERCENT = 5.0
    MAX_DRAWDOWN_PERCENT = 50.0
    
    # OKX Settings
    SANDBOX_MODE = True  # Set to False for live trading
