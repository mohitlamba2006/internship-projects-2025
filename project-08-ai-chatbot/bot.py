import os, time, streamlit as st
import google.genai as genai
from google import genai

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

st.set_page_config(page_title="TAISUKE", layout="centered")
st.title("HI HOW MAY I HELP YOU")
st.subheader("PRESENTED BY MOHIT LAMBA")

if "history" not in st.session_state:
    st.session_state.history = []

stop = ["bye","exit","stop","quit"]

user = st.text_input("Type here")

if user:
    if any(w in user.lower() for w in stop):
        st.write("Chat ended.")
    else:
        st.session_state.history.append(("you", user))
        with st.spinner("Thinking..."):
            time.sleep(1)
            res = client.models.generate_content(model="gemini-2.0-flash", contents=user)
            reply = res.text
        st.session_state.history.append(("bot", reply))

for r,m in st.session_state.history:
    st.write(r, ":", m)
