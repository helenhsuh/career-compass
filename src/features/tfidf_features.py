"""
Baseline TF-IDF feature extraction.
"""

from sklearn.feature_extraction.text import TfidfVectorizer

def build_tfidf_features(corpus):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)
    return vectorizer, vectors
