from google.genai import types

from client import client

from constant import MODEL_ID, DEFAULT_PARAMS
from prompt import *

# Function for generating text
def generate_text(prompt : str|None, temperature = float|None, top_p= float|None, top_k= float|None, max_tokens = int|None) -> str : 
    """
    Summary:
        Generate text from a language model using configurable generation parameters.

    Args:
        prompt (str | None): Input text prompt for generation (required).
        temperature (float | None): Controls randomness of the output.
        top_p (float | None): Nucleus sampling probability threshold.
        top_k (float | None): Limits sampling to top-k probable tokens.
        max_tokens (int | None): Maximum number of tokens in the generated output.

    Returns:
        str: Generated text response from the model.
    """
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

# special fuction for self consistency implement
def self_consistency(prompt: str|list, runs: int = 4,) -> list:
    """
    Summary:
        Generate multiple responses for the same prompt using self-consistency.

    Args:
        prompt (str | list): Input prompt(s) used for generation.
        image: Image input for multimodal text generation.
        runs (int): Number of generation runs to produce diverse outputs.

    Returns:
        list: A list of generated text outputs including the original prompt.
    """
    outputs = []
    outputs.append(prompt)
    # for running prompt multiple times
    for _ in range(runs):
        result = generate_text(
            prompt = outputs,
        )
        if result:
            outputs.insert(0, result)

    return outputs