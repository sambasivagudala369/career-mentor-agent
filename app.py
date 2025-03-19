import streamlit as st
from backend import search_jobs, get_career_advice

st.title("💼 Virtual Career Mentor Agent")

st.header("🔍 Find Your Dream Job")
job_query = st.text_input("Enter job title (e.g., Data Scientist)")
job_location = st.text_input("Enter location (optional)")

if st.button("Search Jobs"):
    if job_query:
        jobs = search_jobs(job_query, job_location)
        for job in jobs:
            st.subheader(job["job_title"])
            st.write(f"Company: {job['employer_name']}")
            st.write(f"Location: {job['job_city']}, {job['job_country']}")
            st.write(f"[🔗 Apply Now]({job['job_apply_link']})")
    else:
        st.warning("Enter a job title to search.")

st.header("🤖 Get AI Career Advice")
career_question = st.text_area("Ask for career advice (e.g., How to switch to AI?)")

if st.button("Get Advice"):
    if career_question:
        advice = get_career_advice(career_question)
        st.write(advice)
    else:
        st.warning("Enter a career-related question.")
