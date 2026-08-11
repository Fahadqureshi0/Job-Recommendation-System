# Importing Pickle

import pickle # Saving model files______!
from sklearn.metrics.pairwise import cosine_similarity # Cosine Similarity_____!
from pathlib import path


# Loading Models______!

# TF-IDF Vectorization Filedef load_models():

    # Get the Jobs_Recommendation_System directory
BASE_DIR = Path(__file__).resolve().parent.parent

    # Get models directory
    MODEL_DIR = BASE_DIR / "models"

    with open(MODEL_DIR / "tfidf.pkl", "rb") as file:
        tfidf = pickle.load(file)

    with open(MODEL_DIR / "job_text_vectors.pkl", "rb") as file:
        job_vectors = pickle.load(file)

    with open(MODEL_DIR / "job_dataset.pkl", "rb") as file:
        jobs_dataset = pickle.load(file)

    return tfidf, job_vectors, jobs_dataset



# Recommendation Function

def recommend_jobs(resume, tfidf, job_vectors, jobs_dataset):

    resume_vector = tfidf.transform([resume])

    similarity_scores = cosine_similarity(
        resume_vector,
        job_vectors
    )

    job_scores = similarity_scores[0]

    sorted_jobs = sorted(enumerate(job_scores),key=lambda x: x[1],reverse=True)

    recommendations = []

    for index, score in sorted_jobs[:10]:

        job_title = jobs_dataset.iloc[index]["job_title"]
        category = jobs_dataset.iloc[index]["category"]

        recommendations.append({
            "job_title": job_title,
            "category": category,
            "score": round(score * 100, 2)
        })

    return recommendations
