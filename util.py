from google.genai import types

from client import client
from constant import MODEL_ID, DEFAULT_PARAMS

# Function for generating text
def generate_text(prompt, temperature = None, top_p= None, top_k= None, max_tokens = None):
    config = types.GenerateContentConfig(
        temperature=temperature if temperature is not None else DEFAULT_PARAMS["temperature"],
        top_p=top_p if top_p is not None else DEFAULT_PARAMS["top_p"],
        top_k=top_k if top_k is not None else DEFAULT_PARAMS["top_k"],
        max_output_tokens=max_tokens if max_tokens is not None else DEFAULT_PARAMS["max_tokens"],
    )
    # creating response form client
    response = client.models.generate_content(
        model=MODEL_ID,
        contents = prompt,
        config=config
    )
    return response.text