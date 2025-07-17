# App/main.py

import streamlit as st
from chatbot import ask_bot

st.set_page_config(page_title="AI Mental Health Chatbot", page_icon="🧠")
st.title("🧠 AI Mental Health Companion")

# Show welcome message on startup
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        ("Bot", "Hello! I'm here to listen and support you. Feel free to share how you're feeling. "
                "Please note: I only respond in English and only about emotional wellbeing.")
    ]

user_input = st.chat_input("How are you feeling today?")

if user_input:
    st.session_state.chat_history.append(("You", user_input))
    response = ask_bot(user_input)
    st.session_state.chat_history.append(("Bot", response))

# Display chat history
for sender, message in st.session_state.chat_history:
    st.write(f"**{sender}:** {message}")
