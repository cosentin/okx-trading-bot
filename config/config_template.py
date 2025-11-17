# config_template.py
# COPY THIS FILE TO config.py AND ADD YOUR API KEYS

class OKXConfig:
    EXCHANGE = 'okx'
    SYMBOL = 'BTC/USDT'
    TIMEFRAME = '1m'
    
    # ⚠️ ADD YOUR API KEYS HERE AFTER COPYING
    API_KEY = 'd12e72bb-42b5-4ef9-85fe-df2c897934ae'
    SECRET_KEY = '7A0187A21DADACA2B5133DCEF459B763'
    PASSPHRASE = 'K4ngg0_r1k0'
    
    # Trading Parameters
    INITIAL_RISK_PERCENT = 10.0
    RECOVERY_RISK_PERCENT = 20.0
    PROFIT_TARGET_PERCENT = 5.0
    MAX_DRAWDOWN_PERCENT = 50.0
    
    # OKX Settings
    SANDBOX_MODE = True  # Set to False for live trading
