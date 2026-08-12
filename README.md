# 💼 AI Job Recommendation System

A Machine Learning-based web application that recommends relevant jobs based on the user's resume. The application allows users to upload their resume in **PDF format**, extracts the resume text, and recommends jobs based on **TF-IDF and Cosine Similarity**.

The application is built using **Python, Scikit-learn, PyPDF, and Streamlit** and deployed on **Streamlit Community Cloud**.

## 🌐 Live Demo

[https://job-recommendation-system-p6arxjfvnvzxuhca2eues7.streamlit.app/](https://job-recommendation-system-p6arxjfvnvzxuhca2eues7.streamlit.app/)

---

## 📌 Features

- 📄 Upload resume in PDF format
- 🔍 Extract text from uploaded resume
- 🤖 AI-based job recommendation
- 📊 TF-IDF-based text vectorization
- 📐 Cosine Similarity for resume-job matching
- 🏆 Recommend top matching jobs
- 📈 Display job match percentage
- 💼 Display job title and category
- 🖥️ Interactive Streamlit user interface
- 🌐 Deployed on Streamlit Community Cloud

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Cosine Similarity
- PyPDF
- Streamlit
- Pickle

---

## 🤖 Machine Learning Approach

The recommendation system uses:

- **TF-IDF (Term Frequency-Inverse Document Frequency)** for converting resume and job text into numerical vectors.
- **Cosine Similarity** for calculating the similarity between the uploaded resume and available job postings.

The jobs are then ranked according to their similarity score and the top matching jobs are recommended to the user.

---

## 📄 Resume Processing

Users can upload their resume in PDF format.

The application extracts the text from the uploaded resume using **PyPDF** and then passes the extracted text to the recommendation system.

```text
Resume PDF
     ↓
Text Extraction
     ↓
TF-IDF Vectorization
     ↓
Cosine Similarity
     ↓
Job Ranking
     ↓
Recommended Jobs
```

---

## 📊 Recommendation Output

The application displays the recommended jobs with:

- Job Title
- Job Category
- Match Percentage

Example:

```text
1. Machine Learning Engineer
   Category: Artificial Intelligence
   Match: 87.42%

2. Data Scientist
   Category: Data Science
   Match: 82.15%

3. Python Developer
   Category: Software Development
   Match: 78.63%
```

> The current match percentage represents text similarity between the resume and job posting. It is not a prediction of whether the candidate will get the job.

---

## 📁 Project Structure

```text
Job-Recommendation-System/
│
├── Jobs_Recommendation_System/
│   │
│   ├── app.py
│   ├── requirements.txt
│   │
│   ├── models/
│   │   ├── tfidf.pkl
│   │   ├── job_text_vectors.pkl
│   │   └── job_dataset.pkl
│   │
│   └── utils/
│       ├── __init__.py
│       ├── recommender.py
│       └── resume_parser.py
│
├── all_job_post.csv
├── README.md
└── LICENSE
```

---

## ▶️ Run Locally

### Clone the repository

```bash
git clone https://github.com/Fahadqureshi0/Job-Recommendation-System.git
```

### Move to the project directory

```bash
cd Job-Recommendation-System
```

### Move to the application directory

```bash
cd Jobs_Recommendation_System
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 📦 Requirements

The project uses the following Python libraries:

```text
streamlit
pandas
scikit-learn==1.6.1
numpy
pypdf
```

---

## 🚧 Future Improvements

The project is currently being developed and additional features are planned, including:

- 🎯 Skill-based job matching
- 💼 Experience-based matching
- 📊 Improved candidate-job scoring
- 🔎 Semantic job search
- 🌐 Real-time job board API integration
- 🔗 Apply to jobs through original job postings
- 📚 Missing skill analysis
- 📝 Resume improvement suggestions
- 🎯 Personalized job recommendations

---

## 👨‍💻 Author

**Fahad Qureshi**

---

## 🌐 Connect with Me

[GitHub](https://github.com/Fahadqureshi0)

---

## 📄 License

This project is licensed under the MIT License.
