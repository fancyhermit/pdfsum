from keras.models import Sequential
from keras.layers import LSTM, Dense, Embedding, Bidirectional
from keras.preprocessing.sequence import pad_sequences

# Build LSTM model for summarization
def build_lstm_model(vocab_size, embedding_dim=100, max_len=100):
    model = Sequential()
    model.add(Embedding(vocab_size, embedding_dim, input_length=max_len))
    model.add(Bidirectional(LSTM(128, return_sequences=True)))
    model.add(Bidirectional(LSTM(64)))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Generate summary with the LSTM model
def generate_summary(text, model, tokenizer, max_len=100):
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=max_len)
    summary = model.predict(padded_sequence)
    return summary
