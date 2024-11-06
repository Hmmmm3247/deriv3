# strategy_logic.py

from models import load_pretrained_model
from trade_execution import execute_trade
from data_processing import calculate_indicators

def run_trading_strategy(symbol):
    if symbol not in market_data or len(market_data[symbol]) < 20:
        return

    data = calculate_indicators(market_data[symbol])
    input_data = data[['price', 'bollinger_high', 'bollinger_low', 'rsi', 'atr']].values
    input_shape = (20, input_data.shape[1])

    models = {
        'transformer': load_pretrained_model("transformer"),
        'gru': load_pretrained_model("gru"),
        'attention': load_pretrained_model("attention"),
        'cnn_rnn': load_pretrained_model("cnn_rnn"),
        'adaptive': load_pretrained_model("adaptive"),
    }

    sample = input_data[-input_shape[0]:]
    contraction_expansion_signal = models['transformer'].predict(sample.reshape(1, *sample.shape))
    breakout_signal = models['gru'].predict(sample.reshape(1, *sample.shape))
    reversal_signal = models['attention'].predict(sample.reshape(1, *sample.shape))
    scalping_signal = models['cnn_rnn'].predict(sample.reshape(1, *sample.shape))
    adaptive_signal = models['adaptive'].predict(sample.reshape(1, *sample.shape))

    if contraction_expansion_signal > 0.5:
        if breakout_signal > 0.5:
            execute_trade(symbol, "buy")
        elif reversal_signal > 0.5:
            execute_trade(symbol, "sell")
