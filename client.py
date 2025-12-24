from google import genai
from google.genai import types
from cred import gemini_api_key

if not gemini_api_key: 
    raise EnvironmentError("Google_key is not found.")
else:
    client = genai.Client(api_key=gemini_api_key)
