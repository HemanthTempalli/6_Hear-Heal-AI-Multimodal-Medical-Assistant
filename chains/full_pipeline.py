# full_pipeline.py
from langchain_core.runnables import RunnableLambda
from chains.voice_transcription_chain import transcribe_audio_chain
from chains.image_analysis_chain import image_analysis_chain
from chains.tts_chains import gtts_tts_chain

# Step 1: Merge audio and image paths
def merge_audio_and_image(inputs: dict) -> dict:
    return {
        "audio_path": inputs["audio"],
        "image_path": inputs["image"]
    }

merge_inputs_chain = RunnableLambda(merge_audio_and_image)


# Step 2: Build query from voice + system prompt
def build_image_query(inputs: dict) -> dict:
    transcription = transcribe_audio_chain.invoke({"audio_path": inputs["audio_path"]})
    system_prompt = """You have to act as a professional doctor, I know you are not but this is for learning purpose. 
        What's in this image? Do you find anything wrong with it medically? 
        If you make a differential, suggest some remedies for them. Do not add any numbers or special characters in 
        your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
        Do not say 'In the image I see' but say 'With what I see, I think you have ....'
        Don't respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
        Keep your answer concise (max 2 sentences). No preamble, start your answer right away please."""

    return {
        "query": system_prompt + "\n" + transcription,
        "image_path": inputs["image_path"],
        "transcription": transcription  # carry forward original speech-to-text
    }

build_query_chain = RunnableLambda(build_image_query)


# Step 3: Prepare TTS inputs from model output
def prepare_tts_inputs(inputs):
    if isinstance(inputs, str):
        return {
            "text": inputs,
            "output_path": "final.mp3",
            "transcription": ""
        }
    return {
        "text": inputs.get("text", inputs),  # fallback to raw string if 'text' missing
        "output_path": "final.mp3",
        "transcription": inputs.get("transcription", "")
    }

prepare_tts_chain = RunnableLambda(prepare_tts_inputs)


# Step 4: Final extraction of outputs
def extract_final_output(inputs: dict) -> dict:
    return {
        "transcription": inputs.get("transcription", ""),
        "text_output": inputs.get("text", ""),
        "audio_path": inputs.get("output_path", "final.mp3")
    }

extract_output_chain = RunnableLambda(extract_final_output)


# Step 5: Chain all steps into a full pipeline
full_medical_pipeline = (
    merge_inputs_chain
    | build_query_chain
    | image_analysis_chain  # returns analyzed text from image + query as 'text'
    | prepare_tts_chain     # prepares TTS input dict with 'text', 'transcription', 'output_path'
    | gtts_tts_chain        # generates audio and returns updated inputs
    | extract_output_chain  # extract what to show on UI
)
