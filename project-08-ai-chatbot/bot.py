import streamlit as st
import time
import google.genai as genai
from google import genai

client = genai.Client(api_key="AIzaSyBEClk3AcjUD7UyCw01aZX0Z-QtofND4pM")

st.set_page_config(page_title="JAATBOT - Your Personal Guide ",layout="centered")
st.title(" HI HOW MAY I HELP YOU :  ")
st.subheader(" PRESENTED BY MOHIT LAMBA :")
st.header("I AM JAAT YOUR PERSONAL GUIDE :")


st.markdown("""
    <style>
    body {
        background-color: #0f1117;
        font-family: 'Poppins', sans-serif;
        color: white;
    }
    .chat {
        margin-top: 20px;
        font-size: 17px;
        line-height: 1.6;
        color: #f8f8f2;
    }
    .user-msg {
        color: #00b4d8;
        font-weight: bold;
        text-align: right;
        margin-top: 10px;
    }
    .bot-msg {
        color: #fff5c3;
        background: rgba(255, 255, 255, 0.05);
        padding: 10px 15px;
        border-radius: 12px;
        margin: 8px 0;
        border-left: 3px solid #ffd166;
        box-shadow: 0 0 10px rgba(255, 209, 102, 0.2);
    }
    .stTextInput>div>div>input {
        background-color: #0f1117;
        border: 2px solid #ffd166;
        color: #fff5c3;
        font-family: 'Caveat', cursive;
        font-size: 18px;
        padding: 10px;
        border-radius: 10px;
        width: 100%;
        box-shadow: 0 0 10px rgba(255, 209, 102, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

if "chathistory" not in st.session_state:
    st.session_state.chathistory = []
if "chat_active" not in st.session_state:
    st.session_state.chat_active = True

st.markdown('<div class="chat">', unsafe_allow_html=True)
for role, msg in st.session_state.chathistory:
    if role == "user":
        st.markdown(f'<div class="user-msg">You: {msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg"><b>Jaat:</b> {msg}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

stop = ["bye", "exit", "stop", "quit","rukjao"]

if st.session_state.chat_active:
    user_input = st.text_input(" Write your thought here, my mitr:", placeholder="Type here...")
else:
    user_input = st.text_input(" Chat ended. Refresh to start again.", disabled=True)

    
if any(word in user_input.lower() for word in stop):
        st.session_state.chathistory.append(("bot", "Jaat:Thank you for interacting with this Jaat bot. "))
        st.session_state.chat_active = False
        st.rerun()

if st.session_state.chat_active:
        st.session_state.chathistory.append(("user", user_input))
        with st.spinner("Jaat is thinking..."):
            time.sleep(1.2)
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=user_input
            )
            reply = response.text

        st.session_state.chathistory.append(("Jaat :", reply))
        st.rerun()