import streamlit as st
from chatbot import ask_bot
from textblob import TextBlob
import tempfile
from gtts import gTTS
import base64
import speech_recognition as sr

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

# Voice Input Setup
st.subheader("🎤 Speak or Type to the chatbot")
user_input = ""

class AudioProcessor:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

    def get_text(self):
        with self.mic as source:
            st.warning("Speak now... recording started!")
            try:
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=10)
                text = self.recognizer.recognize_google(audio)
                st.success(f"You said: {text}")
                return text
            except sr.WaitTimeoutError:
                st.error("You didn't speak in time. Please try again.")
            except sr.UnknownValueError:
                st.error("Sorry, couldn't understand.")
            except sr.RequestError:
                st.error("Speech Recognition service failed.")
        return ""

# Text input comes first
text_input = st.chat_input("Type your thoughts here or click 'Start Talking' to speak...")
if text_input:
    user_input = text_input

# Only use voice if no text input was provided
elif st.button("Start Talking"):
    processor = AudioProcessor()
    user_input = processor.get_text()

# Chatbot logic
if user_input:
    st.session_state.chat_history.append(("You", user_input))

    # Sentiment analysis
    sentiment_score = TextBlob(user_input).sentiment.polarity
    st.metric("🛌️ Mood Score", sentiment_score)

    # Get bot response
    response = ask_bot(f"Mood: {st.session_state.mood}, Message: {user_input}")
    st.session_state.chat_history.append(("Bot", response))

    # Resource suggestions
    if any(word in user_input.lower() for word in ["anxiety", "anxious", "panic"]):
        st.markdown("\ud83d\udcd8 [Coping with Anxiety](https://www.helpguide.org/articles/anxiety/anxiety-disorders-and-anxiety-attacks.htm)")
    elif any(word in user_input.lower() for word in ["sad", "depressed", "unhappy"]):
        st.markdown("\ud83d\udcd8 [Managing Sadness](https://www.healthline.com/health/depression/how-to-fight-depression)")
    elif any(word in user_input.lower() for word in ["angry", "anger"]):
        st.markdown("\ud83d\udcd8 [Dealing with Anger](https://www.apa.org/topics/anger/control)")

    # Voice output (Text-to-Speech)
    def play_audio_from_text(text):
        tts = gTTS(text)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            tts.save(f.name)
            audio_bytes = open(f.name, 'rb').read()
            b64 = base64.b64encode(audio_bytes).decode()
            md = f"""
            <audio autoplay controls>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
            st.markdown(md, unsafe_allow_html=True)

    play_audio_from_text(response)

# Display chat history
for sender, message in st.session_state.chat_history:
    st.write(f"**{sender}:** {message}")

# Disclaimer
with st.expander("🔒 Privacy & Disclaimer"):
    st.write("This chatbot does not store personal data. It is not a substitute for professional mental health services.")