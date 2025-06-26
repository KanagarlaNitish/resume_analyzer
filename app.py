import streamlit as st
import fitz  # PyMuPDF
import io
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Smart Resume Analyzer", layout="centered")

st.title("📄 Smart Resume Analyzer + Job Fit Predictor")

# Upload Resume
resume_file = st.file_uploader("Upload your Resume (PDF format)", type=["pdf"])

# Upload or Enter Job Description
st.subheader("Enter or Upload Job Description")
jd_text = st.text_area("Paste Job Description here:")

jd_file = st.file_uploader("Or Upload Job Description File (TXT)", type=["txt"])

if jd_file is not None:
    jd_text = jd_file.read().decode("utf-8")

# Extract text from resume
def extract_text_from_pdf(uploaded_file):
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

# Check match
def calculate_match(resume_text, jd_text):
    cv = CountVectorizer()
    count_matrix = cv.fit_transform([resume_text, jd_text])
    match_score = cosine_similarity(count_matrix)[0][1]
    return round(match_score * 100, 2)

if st.button("Analyze"):
    if resume_file is not None and jd_text.strip() != "":
        with st.spinner("Analyzing..."):
            resume_text = extract_text_from_pdf(resume_file)
            match_percent = calculate_match(resume_text, jd_text)
            st.success(f"✅ Resume matches {match_percent}% with the Job Description!")

            if match_percent >= 80:
                st.info("Great fit! You can confidently apply for this job. ✅")
            elif match_percent >= 60:
                st.warning("Average match. You may want to improve your resume. ⚠️")
            else:
                st.error("Low match. Consider updating your resume to fit the job better. ❌")
    else:
        st.error("Please upload both Resume and Job Description.")
