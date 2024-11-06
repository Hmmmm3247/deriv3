# models.py

from tensorflow.keras.models import load_model
import os
from config import MODEL_DIR

# Define paths for each model related to scalping strategies
def load_transformer_scalping_model():
    return load_model(os.path.join(MODEL_DIR, 'transformer_scalping.h5'))

def load_cnn_rnn_scalping_model():
    return load_model(os.path.join(MODEL_DIR, 'cnn_rnn_scalping.h5'))

def load_gru_breakout_model():
    return load_model(os.path.join(MODEL_DIR, 'gru_breakout.h5'))

def load_attention_reversal_model():
    return load_model(os.path.join(MODEL_DIR, 'attention_reversal.h5'))


from tensorflow.keras.models import load_model

transformer_model = load_model('models/transformer_scalping.h5')
cnn_rnn_model = load_model('models/cnn_rnn_scalping.h5')
gru_model = load_model('models/gru_breakout.h5')
attention_model = load_model('models/attention_reversal.h5')
