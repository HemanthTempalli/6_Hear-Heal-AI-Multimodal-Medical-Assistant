from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableLambda
import base64

def encode_image(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

def query_llm(inputs: dict) -> dict:
    llm = ChatGroq(model_name="meta-llama/llama-4-scout-17b-16e-instruct")
    image_base64 = encode_image(inputs["image_path"])
    prompt = {
        "role": "user",
        "content": [
            {"type": "text", "text": inputs["query"]},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
        ]
    }
    response = llm.invoke([prompt])
    return {
        "text": response.content,
        "transcription": inputs.get("transcription", "")
    }


image_analysis_chain = RunnableLambda(query_llm)
