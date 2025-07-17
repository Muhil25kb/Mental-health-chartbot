# App/chatbot.py

import requests

SYSTEM_PROMPT = (
    "You are an AI mental health support assistant. "
    "Only respond in English. If the user sends a message in another language or "
    "asks anything outside of mental health, depression, anxiety, stress, or emotional wellbeing, "
    "politely redirect them to stay on-topic. Never give medical advice or diagnoses."
)

def ask_bot(prompt, model="llama3.1"):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": f"{SYSTEM_PROMPT}\n\nUser: {prompt}",
                "stream": False
            }
        )
        response.raise_for_status()
        return response.json()["response"].strip()
    except Exception as e:
        print("Error:", e)
        return "Sorry, something went wrong."
