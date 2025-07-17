
# App/main.py

import streamlit as st
from chatbot import ask_bot
from textblob import TextBlob
# Optional: from streamlit_audiorecorder import audiorecorder

st.set_page_config(page_title="AI Mental Health Chatbot", page_icon="🧠")
st.title("🧠 AI Mental Health Companion")

# Reset button
if st.button("🔁 Reset Conversation"):
    st.session_state.chat_history = [
        ("Bot", "Hello! I'm here to listen and support you. Feel free to share how you're feeling. "
                "Please note: I only respond in English and only about emotional wellbeing.")
    ]

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        ("Bot", "Hello! I'm here to listen and support you. Feel free to share how you're feeling. "
                "Please note: I only respond in English and only about emotional wellbeing.")
    ]
if "mood" not in st.session_state:
    st.session_state.mood = "😐 Neutral"

# Mood selector
st.session_state.mood = st.radio("How are you feeling now?", ["😊 Happy", "😞 Sad", "😡 Angry", "😨 Anxious", "😐 Neutral"])

# Optional: Voice input feature (placeholder)
# st.write("🎤 Voice Input (Coming Soon)")
# audio = audiorecorder("Click to record", "Recording...")
# if audio:
#     with open("audio.wav", "wb") as f:
#         f.write(audio.tobytes())
#     user_input = transcribe_audio("audio.wav")

# Chat input
user_input = st.chat_input("Share your thoughts here...")

if user_input:
    st.session_state.chat_history.append(("You", user_input))

    # Sentiment analysis
    sentiment_score = TextBlob(user_input).sentiment.polarity
    st.metric("🧭 Mood Score", sentiment_score)

    # Get bot response
    response = ask_bot(f"Mood: {st.session_state.mood}, Message: {user_input}")
    st.session_state.chat_history.append(("Bot", response))

    # Resource suggestions
    if any(word in user_input.lower() for word in ["anxiety", "anxious", "panic"]):
        st.markdown("📘 [Coping with Anxiety](https://www.helpguide.org/articles/anxiety/anxiety-disorders-and-anxiety-attacks.htm)")
    elif any(word in user_input.lower() for word in ["sad", "depressed", "unhappy"]):
        st.markdown("📘 [Managing Sadness](https://www.healthline.com/health/depression/how-to-fight-depression)")
    elif any(word in user_input.lower() for word in ["angry", "anger"]):
        st.markdown("📘 [Dealing with Anger](https://www.apa.org/topics/anger/control)")

# Display chat history
for sender, message in st.session_state.chat_history:
    st.write(f"**{sender}:** {message}")

# Disclaimer
with st.expander("🔒 Privacy & Disclaimer"):
    st.write("This chatbot does not store personal data. It is not a substitute for professional mental health services.")
