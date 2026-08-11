import streamlit as st

from resume_parser import extract_text_from_pdf
from recommender import load_models, recommend_jobs


st.set_page_config(
    page_title="AI Job Recommendation System",
    page_icon="💼",
    layout="wide"
)


@st.cache_resource
def load_resources():

    return load_models()


tfidf, job_vectors, jobs_dataset = load_resources()


st.title("💼 AI Job Recommendation System")

st.write(
    "Upload your resume and find jobs that match your profile."
)


uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)


if uploaded_file:

    st.success("Resume uploaded successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)

    with st.expander("View extracted resume text"):
        st.write(resume_text)

    if st.button("🔍 Find Recommended Jobs"):

        recommendations = recommend_jobs(
            resume_text,
            tfidf,
            job_vectors,
            jobs_dataset
        )

        st.subheader("Recommended Jobs")

        for i, job in enumerate(recommendations, 1):

            st.write(
                f"### {i}. {job['job_title']}"
            )

            st.write(
                f"Category: {job['category']}"
            )

            st.progress(
                min(job["score"] / 100, 1.0)
            )

            st.write(
                f"Match: {job['score']}%"
            )

            st.divider()