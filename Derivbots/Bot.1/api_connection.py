# api_connection.py

import asyncio
from deriv_api import DerivAPI
from config import API_TOKEN, APP_ID, SYNTHETIC_INDICES

async def initialize_deriv_api():
    api = DerivAPI(app_id=APP_ID)
    await api.authorize(API_TOKEN)
    print("Authorized successfully.")
    return api

async def subscribe_to_ticks(api, symbol):
    return await api.subscribe({"ticks": symbol})
