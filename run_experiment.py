from util import generate_text
from prompt import prompt1, prompt2, prompt3, prompt4, prompt5
from constant import config_settings

def experiments():
    

    for cs in config_settings:
        output = generate_text(prompt5, **cs)
        print(f"Param:{cs}\nOutput:\n{output}")