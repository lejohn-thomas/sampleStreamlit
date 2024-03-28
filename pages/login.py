import streamlit as st
import google.generativeai as genai
from io import StringIO

genai.configure(api_key="AIzaSyCi6oWTFGPd9VU5kEfeJ17A5jrDlAGNNoI")
model = genai.GenerativeModel('gemini-pro')

with open('/home/lejohn_thomas/sampleStreamlit/styles/main.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


st.title("Study+")


#CHATBOX
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

with st.container():
    # file upload
    files = st.file_uploader("Upload file(s)")


    #Logic for talking to Ai and receiving response
    userinput = st.chat_input("What do you need help with today")
    if userinput:
        st.session_state.messages.append({"role": "user", "content": userinput})
        if files is not None:
            filedata = StringIO(files.getvalue().decode("utf-8"))
            response = model.generate_content(userinput + " " + filedata.read())
        else:
            response = model.generate_content(userinput)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        with st.chat_message("user"):
            st.markdown(userinput)
        with st.chat_message("assistant"):
            st.markdown(response.text)



