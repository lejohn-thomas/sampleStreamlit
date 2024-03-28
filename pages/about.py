import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="wide")

with open('styles/about.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.title('All About Study+')

with st.container():
    st.subheader("Introducing Study+ : Your Ultimate Academic Sidekick!")
    st.text("Say goodbye to late-night cram sessions and scattered notes. StudyMate is the revolutionary app designed to streamline your study routine and elevate your academic performance. \nWith intuitive features tailored for students, StudyMate offers customizable study schedules, interactive flashcards, collaborative study groups, and seamless integration with your course materials. \nWhether you're preparing for exams or tackling homework assignments, Study+ empowers you to study smarter, not harder. Download StudyMate today and embark on your journey to academic success!")

col1, col2, col3 = st.columns(3)
with col2:
    conbut = st.button("Continue", "/home/lejohn_thomas/sampleStreamlit/main.py")
if conbut:
    switch_page("main")