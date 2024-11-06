# trade_execution.py

import json
from api_connection import initialize_deriv_api
from config import TRADE_AMOUNT, TRADE_DURATION, TRADE_CURRENCY
import time

trade_tracker = {}

async def execute_trade(api, symbol, direction):
    current_time = time.time()
    if trade_tracker.get(symbol) and current_time - trade_tracker[symbol] < 60:
        print(f"Skipping trade for {symbol} to prevent over-trading.")
        return

    proposal = await api.proposal({
        "proposal": 1,
        "amount": TRADE_AMOUNT,
        "contract_type": "CALL" if direction == "buy" else "PUT",
        "currency": TRADE_CURRENCY,
        "duration": TRADE_DURATION,
        "duration_unit": "m",
        "symbol": symbol
    })
    
    proposal_id = proposal.get('proposal').get('id')
    await api.buy({"buy": proposal_id, "price": TRADE_AMOUNT})
    trade_tracker[symbol] = current_time
    print(f"Executed {direction} trade for {symbol}.")
