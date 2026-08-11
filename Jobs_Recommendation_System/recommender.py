# Importing Pickle

import pickle # Saving model files______!
from sklearn.metrics.pairwise import cosine_similarity # Cosine Similarity_____!


# Loading Models______!

# TF-IDF Vectorization File

def load_models():
    with open("models/tfidf.pkl", "rb") as file:
        tfidf = pickle.load(file)

# Job Vectors File

    with open("models/job_text_vectors.pkl", "rb") as file:
        job_vectors = pickle.load(file)


# job dataset file
    with open("models/jobs_dataset.pkl", "rb") as file:
            job_dataset = pickle.load(file)


    return tfidf, job_vectors, job_dataset



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