# main.py

import asyncio
from api_connection import initialize_deriv_api, subscribe_to_ticks
from config import SYNTHETIC_INDICES

async def main():
    api = await initialize_deriv_api()

    # Subscribe to tick data for each synthetic index
    subscriptions = []
    for symbol in SYNTHETIC_INDICES.values():
        subscription = await subscribe_to_ticks(api, symbol)
        subscription.subscribe(lambda tick: print(tick))
        subscriptions.append(subscription)

    # Keep bot running
    while True:
        await asyncio.sleep(1)

# Run the bot
asyncio.run(main())
