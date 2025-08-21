import streamlit as st
from src.skill_extraction import extract_text_from_pdf, extract_skills
from src.preprocessing import clean_text
from src.similarity import calculate_similarity

st.set_page_config(page_title="Job Match Parser", layout="wide")

st.title('📄 Job Match Resume Parser')
st.write('Upload a resume (PDF) and a job description to see the match score and skill analysis')
st.write("-"*10)

col1, col2 = st.columns(2)

with col1:
    st.header("Resume Analysis")
    uploaded_resume = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

    if uploaded_resume:
        with open("temp_resume.pdf", "wb") as f:
            f.write(uploaded_resume.getbuffer())
        
        resume_text = extract_text_from_pdf("temp_resume.pdf")
        cleaned_resume = clean_text(resume_text)
        resume_skills = extract_skills(resume_text)
        
        st.subheader("Extracted Resume Skills")
        st.info(", ".join(resume_skills) if resume_skills else "No specific skills found.")
        
        with st.expander("Show Full Resume Text"):
            st.text(resume_text)

with col2:
    st.header("Job Description Analysis")
    jd_text = st.text_area("Paste the Job Description here",value=open('data/job_description.txt').read(),height='content')

    if jd_text:
        cleaned_jd = clean_text(jd_text)
        jd_skills = extract_skills(jd_text)
        
        st.subheader("Extracted Job Description Skills")
        st.info(", ".join(jd_skills) if jd_skills else "No specific skills found.")

if uploaded_resume and jd_text:
    st.write("---")
    st.header("Match Results")

    similarity_score = calculate_similarity(cleaned_resume, cleaned_jd)

    st.subheader(f"Similarity Score: {similarity_score:.2%}")
    st.progress(similarity_score)

    missing_skills = list(set(jd_skills) - set(resume_skills))
    
    st.subheader("Skill Gap Analysis")
    if missing_skills:
        st.warning(f"**Skills missing from resume:** {', '.join(missing_skills)}")
    else:
        st.success("🎉 All required skills seem to be present in the resume!")
