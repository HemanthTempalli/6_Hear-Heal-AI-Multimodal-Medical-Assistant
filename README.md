# 🩺 Hear&Heal AI — Multimodal Medical Assistant

> Speak your symptoms, upload a photo (like a rash), and get instant AI-generated medical feedback — in **text and voice**.

---

## 🚀 Features

- 🎤 **Voice Input**: Describe your symptoms using your microphone.
- 🖼️ **Image Upload**: Upload medical images (e.g. skin rash, swelling).
- 🧠 **Multimodal AI Diagnosis**: Combines voice + image to give diagnostic insight.
- 📝 **Text Output**: Natural language feedback like a real doctor.
- 🔊 **Voice Output**: Doctor's advice is spoken aloud using Text-to-Speech.
- 🌐 **Gradio Frontend**: User-friendly web UI for real-time interaction.

---

## 🧠 Models Used

| Model                   | Purpose                                 | Why This Model?                                                                                                                                                                                                           |
| ----------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Whisper Large V3**    | 🎙️ Speech-to-text (voice transcription) | Whisper is one of the most accurate open-source ASR models. `large-v3` is fast, robust across accents/languages, and easy to use via `openai-whisper` or HuggingFace.                                                     |
| **LLaMA 4 Scout (17B)** | 🧠 Medical reasoning from image + voice | `meta-llama/llama-4-scout-17b-16e-instruct` on Groq is optimized for **multimodal input** (text + image), making it ideal for analyzing patient descriptions and medical photos together with natural language reasoning. |
| **gTTS (Google TTS)**   | 🔊 Converts doctor advice into voice    | Lightweight, fast, and easy to deploy for generating speech output from text. Perfect for proof-of-concept and simple audio feedback.                                                                                     |

---

## 🛠️ Tools & Libraries

| Tool/Library        | Purpose                                     |
| ------------------- | ------------------------------------------- |
| **Gradio**          | Build and host the web UI                   |
| **LangChain**       | Build modular chains for audio/image/LLM    |
| **Groq API**        | Fast inference for LLaMA-4 model            |
| **Whisper**         | OpenAI speech recognition engine            |
| **gTTS**            | Google Text-to-Speech for voice output      |
| **Base64 Encoding** | Pass image to Groq in LLM-compatible format |
| **Python**          | End-to-end implementation                   |

---

## 🧩 Pipeline Overview

Audio Input + Image Upload
↓
Transcription (Whisper)
↓
Build Query + System Prompt
↓
Multimodal LLM Response (Groq - LLaMA 4 Scout)
↓
Text-to-Speech (gTTS)
↓
Final Output (Text + Audio)

1)Create virtual environment
python -m venv venv

# on Windows: venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Set up environment variables

Create a .env file and add:

GROQ_API_KEY=your_groq_api_key

Run the app

python app.py
You’ll get a Gradio public URL to interact with the app in the browser.

🌌 Future Improvements
Add real-time webcam analysis

Use ElevenLabs TTS for more human-like speech

Store medical history with LangChain memory

Deploy to Hugging Face Spaces or Streamlit Cloud

🧑‍⚕️ Disclaimer
This tool is for educational/demo purposes only and not a replacement for professional medical diagnosis. Always consult a real doctor for any health concerns.
