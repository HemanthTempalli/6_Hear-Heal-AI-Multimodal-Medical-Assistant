# app.py
import os
import gradio as gr
from chains.full_pipeline import full_medical_pipeline
from dotenv import load_dotenv
load_dotenv()


def process_inputs(audio, image):
    result = full_medical_pipeline.invoke({
        "audio": audio,
        "image": image
    })

    return result["transcription"], result["text_output"], result["audio_path"]


iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="Describe your symptom verbally"),
        gr.Image(type="filepath", label="Upload an image of the issue (e.g. rash)")
    ],
    outputs=[
        gr.Textbox(label="You Said (speech to text)"),
        gr.Textbox(label="Doctor's Advice"),
          gr.Audio(label="Spoken Advice (AI voice)", autoplay=True)
    ],
    title="🩺 Hear&Heal AI — Multimodal Medical Assistant",
    description="Speak your symptoms and optionally upload an image. Get AI-generated medical insight in voice + text."
)

iface.launch(share=True)
