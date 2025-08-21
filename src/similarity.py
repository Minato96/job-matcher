from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, jd_text):
    '''calculates cosine similarity between two texts using TF-IDF'''
    text_corpus = [resume_text, jd_text]
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(text_corpus)
    
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    
    return similarity_score