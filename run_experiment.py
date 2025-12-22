from client import generate_text
from prompt import prompt1, prompt2, prompt3, prompt4, prompt5

def experiments():
    config_settings = [
        {"temperature": 0.2, "top_p": 0.9, "top_k":20, "max_tokens": 1000},
        # {"temperature": 0.7, "top_p": 0.9, "top_k":30, "max_tokens": 150},
        # {"temperature": 1.0, "top_p": 0.95, "top_k":50, "max_tokens": 200},
    ]

    for cs in config_settings:
        output = generate_text(prompt5, **cs)
        print(f"Param:{cs}\nOutput:\n{output}")