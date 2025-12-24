import os
from dotenv import load_dotenv

# Loading Gemini API key
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")