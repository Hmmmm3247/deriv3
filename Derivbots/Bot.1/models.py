from tensorflow.keras.models import load_model

# Load the pretrained model
transformer_model = load_model('models/transformer.h5')
gru_model = load_model('models/gru.h5')
attention_model = load_model('models/attention.h5')
cnn_rnn_model = load_model('models/cnn_rnn.h5')
adaptive_model = load_model('models/adaptive.h5')
