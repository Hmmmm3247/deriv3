# strategy_logic.py

from models import (
    load_transformer_scalping_model, 
    load_cnn_rnn_scalping_model, 
    load_gru_breakout_model, 
    load_attention_reversal_model
)
from trade_execution import execute_trade
from data_processing import calculate_indicators

# Load all models
transformer_model = load_transformer_scalping_model()
cnn_rnn_model = load_cnn_rnn_scalping_model()
gru_model = load_gru_breakout_model()
attention_model = load_attention_reversal_model()

def run_scalping_strategy(symbol):
    if symbol not in market_data or len(market_data[symbol]) < 20:
        return

    data = calculate_indicators(market_data[symbol])
    input_data = data[['price', 'bollinger_high', 'bollinger_low', 'rsi', 'atr']].values
    input_shape = (20, input_data.shape[1])

    sample = input_data[-input_shape[0]:]

    # Predictions from each model
    contraction_expansion_signal = transformer_model.predict(sample.reshape(1, *sample.shape))
    micro_movement_signal = cnn_rnn_model.predict(sample.reshape(1, *sample.shape))
    breakout_signal = gru_model.predict(sample.reshape(1, *sample.shape))
    reversal_signal = attention_model.predict(sample.reshape(1, *sample.shape))

    # Decision-making logic based on multiple scalping signals
    if contraction_expansion_signal > 0.5:
        if breakout_signal > 0.5:
            execute_trade(symbol, "buy")
        elif reversal_signal > 0.5:
            execute_trade(symbol, "sell")
        elif micro_movement_signal > 0.5:
            execute_trade(symbol, "buy")
