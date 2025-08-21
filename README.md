# Job Match Resume Parser (NLP + Streamlit App)

## 🎯 Project Goal
This project is an NLP-powered tool designed to evaluate the fit between a candidate's resume and a job description. It automates the initial screening process by parsing documents, extracting key skills, and calculating a similarity score to quantify the match.



## ✨ Features
-   **PDF Resume Parsing:** Upload resumes in PDF format for analysis.
-   **Job Description Input:** Paste any job description text.
-   **NLP-Powered Skill Extraction:** Uses **spaCy** for Named Entity Recognition (NER) and rule-based matching to identify technical skills.
-   **Similarity Scoring:** Employs **TF-IDF Vectorization** and **Cosine Similarity** to compute a match score between the resume and the job description.
-   **Skill Gap Analysis:** Highlights the skills required in the job description that are missing from the resume.
-   **Interactive UI:** A clean and user-friendly web interface built with **Streamlit**.

## 🛠️ Tech Stack
-   **Language:** Python
-   **Libraries:** Streamlit, spaCy, Scikit-Learn, PyMuPDF (fitz), Pandas

## 🚀 How to Run
1.  **Clone the repository:**
    ```bash
    git clone <your-repo-link>
    cd job-match-parser
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate # On macOS/Linux
    # venv\Scripts\activate  # On Windows
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Download spaCy model:**
    ```bash
    python -m spacy download en_core_web_sm
    ```
5.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

## 🔮 Future Work
-   **Integrate Advanced Embeddings:** Use models like Word2Vec or BERT for semantic similarity, which can understand context better than TF-IDF.
-   **Batch Processing:** Allow uploading multiple resumes to rank them against a single job description.
-   **Export Results:** Add functionality to export the analysis (scores, missing skills) to a CSV or Excel file.