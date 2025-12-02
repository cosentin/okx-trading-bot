#!/usr/bin/env python3
"""
CONFIG COMPLETE - FOR BOT LENGKAP
"""

class TradingConfig:
    def __init__(self):
        # 🎯 LIVE CREDENTIALS - GANTI INI!
        self.API_KEY = "API_KEY_LIVE_ANDA"
        self.SECRET_KEY = "SECRET_KEY_BASE64_LIVE"
        self.PASSPHRASE = "PASSPHRASE_LIVE"
        
        # 🚨 LIVE MODE
        self.SANDBOX_MODE = False
        
        # 📊 TRADING SETTINGS
        self.SYMBOL = "DOGE/USDT:USDT"
        self.TIMEFRAME = "5m"
        self.LEVERAGE = 3
        
        # 🎯 RISK MANAGEMENT
        self.INITIAL_RISK_PERCENT = 1.5
        self.MAX_DRAWDOWN_PERCENT = 15.0
        self.MAX_POSITION_SIZE = 0.10
        self.MIN_NOTIONAL = 1.0
        
        # ⚡ TRADING LIMITS
        self.MAX_TRADES_PER_DAY = 25
        
        # 💰 AUTO-COMPOUNDING
        self.COMPOUNDING_ENABLED = True
        self.AUTO_COMPOUND_THRESHOLD = 0.50
        
        # 📈 STRATEGY PARAMETERS
        self.RSI_OVERSOLD = 30
        self.RSI_OVERBOUGHT = 70
        self.BB_PERIOD = 20
        self.BB_STD_DEV = 2.0
        
        # 🎯 EXIT STRATEGY
        self.TP_SIDEWAYS = 0.8
        self.TP_TRENDING = 1.2
        self.TP_VOLATILE = 1.5
        self.TP_RANGING = 1.0
        
        self.SL_SIDEWAYS = 0.4
        self.SL_TRENDING = 0.6
        self.SL_VOLATILE = 0.8
        self.SL_RANGING = 0.5
        
        # 📝 LOGGING
        self.LOG_LEVEL = "INFO"
        self.LOG_FILE = "trading.log"

# ✅ BUAT INSTANCE CONFIG
config = TradingConfig()

print("\n" + "⚙️" * 50)
print("⚙️           COMPLETE BOT CONFIG LOADED           ⚙️")
print("⚙️" * 50)
print(f"📊 Trading: {config.SYMBOL}")
print(f"⚡ Leverage: {config.LEVERAGE}x")
print(f"🎯 Risk/Trade: {config.INITIAL_RISK_PERCENT}%")
print(f"💰 Mode: {'LIVE' if not config.SANDBOX_MODE else 'SANDBOX'}")
print("⚙️" * 50)
