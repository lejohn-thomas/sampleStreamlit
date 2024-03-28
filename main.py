import streamlit as st
from streamlit_extras.switch_page_button import switch_page
# streamlit run main.py --server.enableCORS=false


with open('styles/login.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.title('Welcome to Study+')

st.image('styles/Harriet-Books-SEO.png')

col1, col2, col3 = st.columns(3)
with col2:
    emailbut = st.button("Login with Email", type="primary")
if emailbut:
    switch_page("about")

col4, col5, col6 = st.columns(3)
with col5:
    googlebut = st.button("Login with Google", type="primary")
if googlebut:
    switch_page("about")


