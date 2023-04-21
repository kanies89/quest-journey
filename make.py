from core import RPGScenario
import openai
from typing import Dict, Any

class ChatGPTMake:
    def __init__(self, prompt: str, api_key: str):
        self.prompt = prompt
        self.api_key = api_key

    def generate_input(self) -> Dict[str, Any]:
        # Initialize OpenAI's API client
        openai.api_key = self.api_key

        # Get field names and types for RPGScenario
        field_names = [field[0] for field in RPGScenario.fields]
        field_types = [field[1] for field in RPGScenario.fields]

        # Prompt user for input for each field
        instance_args = {}

        for field_name, field_type in zip(field_names, field_types):
            if field_type is not int:
                if "audio" in field_name:
                    continue
                if field_name == "title":
                    field_name.join(" - adjectives are only to help you to adjust the title")
                adjectives = ("harsh", "cruel", "sci-fi", "pandemic")
                inspire = "Cyberpunk"
                response = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=f"Please enter the: - {field_name} - (adjectives that describe this: {adjectives}, inspire with: {inspire}) of your LARP:\n\n",
                    max_tokens=100,
                    n=1,
                    stop=None,
                    temperature=0.7,
                )
                response.choices[0].text.strip()
                print(response)
                input_value = response.choices[0].text.strip()
                instance_args[field_name] = input_value
                print(input_value, 1)
            else:
                if field_type is int:
                    prompt = f"Please enter a value for {field_name} (type: {field_type.__name__})"
                    input_value = int(input(prompt))
                    instance_args[field_name] = input_value
        return instance_args
