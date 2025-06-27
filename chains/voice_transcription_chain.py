import os
from groq import Groq
from langchain_core.runnables import RunnableLambda

def transcribe_audio(inputs: dict) -> str:
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    with open(inputs["audio_path"], "rb") as audio_file:
        result = client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=audio_file,
            language="en"
        )
    return result.text

transcribe_audio_chain = RunnableLambda(transcribe_audio)
