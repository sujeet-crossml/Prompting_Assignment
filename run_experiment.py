from util import generate_text
from prompt import prompt1, prompt2, prompt3, prompt4, prompt5

# running experiments with different config values
def experiments(custom_config:dict) -> None:
    '''
    This function is used for running different custom config.
    Custom config should be in dictionary.
    '''
    # for getting every custom config
    for cs in custom_config:
        output = generate_text(prompt5, **cs)
        print(f"Param:{cs}\nOutput:\n{output}")