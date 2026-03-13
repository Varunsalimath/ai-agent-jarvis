import streamlit as st
from agent import ask_agent

st.title("Jarvis AI Agent 🤖")

user_input = st.text_input("Ask Jarvis something:")

if user_input:
    response = ask_agent(user_input)
    st.write(response)