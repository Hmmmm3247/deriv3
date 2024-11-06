# config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_TOKEN = os.getenv("DERIV_API_TOKEN")
APP_ID = int(os.getenv("DERIV_APP_ID"))

SYNTHETIC_INDICES = {
    'volatility_75': 'R_75',
    'boom_500': 'BOOM_500',
    'crash_1000': 'CRASH_1000',
    'jump_25': 'R_25'
}

TRADE_AMOUNT = 10            # Stake amount
TRADE_DURATION = 1           # Duration in minutes
TRADE_CURRENCY = "USD"
MAX_TRADES_PER_MINUTE = 3    # Limit trades per minute to prevent over-trading
MODEL_DIR = 'models/'        # Directory to store model files
