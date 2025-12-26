from google.genai import types

from client import client
from constant import MODEL_ID, DEFAULT_PARAMS
from prompt import system_instruction

# Function for generating text
def generate_text(prompt : str|None, temperature = float|None, top_p= float|None, top_k= float|None, max_tokens = int|None) -> str : 
    '''
    Generate_text function is used for generating text from a specific model and client.
    This takes different parameter like prompt, temperature, top_p, top_k, and max_tokens. Only 'prompt' is compulsory.
    This function returns text in string. 
    '''
    config = types.GenerateContentConfig(
        system_instruction= system_instruction,
        temperature=temperature if temperature is not None else DEFAULT_PARAMS.get("temperature"), # For randomness and creative response
        top_p=top_p if top_p is not None else DEFAULT_PARAMS.get("top_p"), # selects a fixed number of the most probable words
        top_k=top_k if top_k is not None else DEFAULT_PARAMS.get("top_k"), # selects the smallest set of words whose cumulative probability exceeds a threshold 
        max_output_tokens=max_tokens if max_tokens is not None else DEFAULT_PARAMS.get("max_tokens"), # max output token allowed for the response get.
    )
    # creating response form client
    response = client.models.generate_content(
        model=MODEL_ID,
        contents = prompt,
        config=config
    )
    return response.text