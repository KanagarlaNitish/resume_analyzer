from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match_percentage(resume_text, job_desc):
    documents = [resume_text, job_desc]
    vectorizer = CountVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()
    similarity = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
    return similarity * 100
