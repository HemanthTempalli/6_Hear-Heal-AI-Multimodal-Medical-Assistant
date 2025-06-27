# chains/tts_chains.py

from langchain_core.runnables import RunnableLambda
from gtts import gTTS
import os
import platform
import subprocess

def _play_audio(output_path):
    os_name = platform.system()
    try:
        if os_name == "Darwin":
            subprocess.run(["afplay", output_path])
        elif os_name == "Windows":
            subprocess.run(["powershell", "-c", f'(New-Object Media.SoundPlayer \"{output_path}\").PlaySync();'])
        elif os_name == "Linux":
            subprocess.run(["aplay", output_path])
    except Exception as e:
        print(f"[TTS Playback Error] {e}")

def gtts_tts(inputs: dict) -> dict:
    tts = gTTS(text=inputs["text"])
    tts.save(inputs["output_path"])
    return {
        "transcription": inputs["transcription"],
        "text": inputs["text"],
        "audio_path": inputs["output_path"]
    }

gtts_tts_chain = RunnableLambda(gtts_tts)
