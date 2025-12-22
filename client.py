from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from model_config import MODEL_ID, DEFAULT_PARAMS

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key: 
    raise EnvironmentError("Google_key is not found.")
else:
    client = genai.Client(api_key=api_key)


def generate_text(prompt, temperature = None, top_p= None, top_k= None, max_tokens = None):
    config = types.GenerateContentConfig(
        temperature=temperature if temperature is not None else DEFAULT_PARAMS["temperature"],
        top_p=top_p if top_p is not None else DEFAULT_PARAMS["top_p"],
        top_k=top_k if top_k is not None else DEFAULT_PARAMS["top_k"],
        max_output_tokens=max_tokens if max_tokens is not None else DEFAULT_PARAMS["max_tokens"],
    )

    response = client.models.generate_content(
        model=MODEL_ID,
        contents = prompt,
        config=config
    )
    return response.text


