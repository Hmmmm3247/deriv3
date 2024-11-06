# strategy_logic.py

from models import (
    load_transformer_scalping_model,
    load_cnn_rnn_scalping_model,
    load_gru_breakout_model,
    load_attention_reversal_model
)
from trade_execution import execute_trade

# Load models
transformer_model = load_transformer_scalping_model()
cnn_rnn_model = load_cnn_rnn_scalping_model()
gru_model = load_gru_breakout_model()
attention_model = load_attention_reversal_model()

def run_scalping_strategy(data):
    contraction_signal = transformer_model.predict(data)
    micro_signal = cnn_rnn_model.predict(data)
    breakout_signal = gru_model.predict(data)
    reversal_signal = attention_model.predict(data)

    # Trade decisions
    if contraction_signal > 0.5 and breakout_signal > 0.5:
        execute_trade("buy")
    elif reversal_signal > 0.5:
        execute_trade("sell")
    elif micro_signal > 0.5:
        execute_trade("buy")
