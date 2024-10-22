from sklearn.feature_extraction.text import TfidfVectorizer

# Extract top N keywords using TF-IDF
def extract_keywords(text, top_n=5):
    vectorizer = TfidfVectorizer(max_features=top_n, stop_words='english')
    vectors = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    return feature_names
