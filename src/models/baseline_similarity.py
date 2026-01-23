"""
Cosine similarity baseline model.
"""

from sklearn.metrics.pairwise import cosine_similarity

def rank_roles(user_vector, job_vectors):
    scores = cosine_similarity(user_vector, job_vectors)
    return scores
