Mental Health Chatbot (Voice-Enabled)
        A local, privacy-first AI-based mental health chatbot built with Streamlit and Ollama. It supports both text and voice input/output, performs sentiment analysis, and provides supportive responses using a locally hosted large language model (LLaMA 3 via Ollama).
Features
  * Interactive chat interface via Streamlit
  * Responds empathetically to mental health topics
  * Sentiment analysis of user input using TextBlob
  * Voice-to-voice support: speak to the bot, hear it respond
  * No internet or OpenAI key required (runs entirely locally)
  * Resource links for anxiety, sadness, and anger

🧰 Technologies Used

🔹 Frontend & Interface
    
     1.Streamlit:  Interactive chat UI with chat_input, chat_message. Real-time UI updates, layout, user session.
     2. Emojis & Markdown: Friendly message styling using markdown with emojis.

🔹 Voice Support
    
    1.SpeechRecognition: Converts spoken input (via mic) to text.
     
     2.PyAudio: Captures microphone input (used by SpeechRecognition).
    
       * Note: installed via pipwin or wheel on Windows.
  
     3.pyttsx3: Text-to-speech for bot response. Works offline across platforms.

🔹 AI & NLP
    
    1.Ollama:Local LLM inference engine for running models like llama3:8b. No internet or API key required
   
    2.llama3:1 8b (via Ollama): The main language model that generates chatbot replies TextBlob. Sentiment analysis on user input. Gives 
         a polarity score (positive/neutral/negative).

🔹 Backend & Integration
    
     1.Python: Core programming languag.Manages logic, chat flow, and API calls.
     
      2.Requests: Used to send prompts to the Ollama server API
 

Install Dependencies
1. Install Dependencies:

     python -m venv venv
      venv\\Scripts\\activate

2.Then install requirements:
    
    pip install -r requirements.txt

3.Additional steps for voice support (Windows):
      
       pip install pipwin
       pipwin install pyaudio

4. Install Ollama & Pull Model:
    Install Ollama

        (https://ollama.com/):
     ollama pull llama3:18b
     ollama serve

5. Run the App:

       streamlit run App/main.py








