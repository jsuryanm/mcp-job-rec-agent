import streamlit as st 

st.set_page_config(page_title="Job Recommneder",layout="wide")
st.title("AI Job Recommender")
st.markdown("Upload your resume and get recommnedations based on your skills and experience from Linkedin and Naukri.")

uploaded_file = st.file_uploader("Upload your resume in pdf format", type=['pdf'])