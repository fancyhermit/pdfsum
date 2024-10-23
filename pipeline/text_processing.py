import nltk
from nltk.tokenize import word_tokenize
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

nltk.download('punkt')

# Preprocess text for LSTM input
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    return tokens

# Convert text to sequences for LSTM
def prepare_lstm_input(texts, max_len=100):
    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(texts)
    sequences = tokenizer.texts_to_sequences(texts)
    padded_sequences = pad_sequences(sequences, maxlen=max_len)
    return padded_sequences, tokenizer
