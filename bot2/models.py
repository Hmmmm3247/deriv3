# models.py

from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, GRU, Conv1D, MaxPooling1D, Flatten, Attention, MultiHeadAttention
from tensorflow.keras.optimizers import Adam
import os
from config import MODEL_DIR

# Contraction/Expansion Model - Transformer
def build_transformer_scalping_model(input_shape):
    model = Sequential([
        MultiHeadAttention(num_heads=4, key_dim=input_shape[1]),
        Flatten(),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Micro-Price Movement Model - CNN-RNN Hybrid
def build_cnn_rnn_scalping_model(input_shape):
    model = Sequential([
        Conv1D(32, kernel_size=3, activation='relu', input_shape=input_shape),
        MaxPooling1D(pool_size=2),
        GRU(32, return_sequences=True),
        GRU(16),
        Flatten(),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Breakout Detection Model - GRU
def build_gru_breakout_model(input_shape):
    model = Sequential([
        GRU(64, input_shape=input_shape, return_sequences=True),
        GRU(32),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Momentum Reversal Model - Attention Layer
def build_attention_reversal_model(input_shape):
    model = Sequential([
        Attention(),
        Flatten(),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Save trained models
def save_models():
    build_transformer_scalping_model((20, 5)).save(os.path.join(MODEL_DIR, 'transformer_scalping.h5'))
    build_cnn_rnn_scalping_model((20, 5)).save(os.path.join(MODEL_DIR, 'cnn_rnn_scalping.h5'))
    build_gru_breakout_model((20, 5)).save(os.path.join(MODEL_DIR, 'gru_breakout.h5'))
    build_attention_reversal_model((20, 5)).save(os.path.join(MODEL_DIR, 'attention_reversal.h5'))
