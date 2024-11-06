# data_processing.py

import pandas as pd
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands, AverageTrueRange

market_data = {}

def update_market_data(tick_data):
    symbol = tick_data['symbol']
    price = float(tick_data['quote'])
    time = pd.to_datetime(tick_data['epoch'], unit='s')

    if symbol not in market_data:
        market_data[symbol] = pd.DataFrame(columns=['time', 'price'])

    market_data[symbol] = market_data[symbol].append({'time': time, 'price': price}, ignore_index=True)
    if len(market_data[symbol]) > 100:
        market_data[symbol] = market_data[symbol].tail(100)

def calculate_indicators(data):
    bb = BollingerBands(close=data['price'], window=20, window_dev=2)
    data['bollinger_high'] = bb.bollinger_hband()
    data['bollinger_low'] = bb.bollinger_lband()
    data['bollinger_mid'] = bb.bollinger_mavg()

    rsi = RSIIndicator(close=data['price'], window=14)
    data['rsi'] = rsi.rsi()

    atr = AverageTrueRange(high=data['price'], low=data['price'], close=data['price'], window=14)
    data['atr'] = atr.average_true_range()

    return data.dropna()
