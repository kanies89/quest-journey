from core import RPGScenario, TextToVoice
from game_db import Database
from make import ChatGPTMake
import os

if __name__ == '__main__':
    db = Database('127.0.0.1', 3306, 'root', 'Xl2Km0oP', 'quest')
    # Initialize ChatGPTMake
    chat = ChatGPTMake("Please enter the:", os.environ["OPENAI_API_KEY"])

    # Generate input for RPGScenario
    instance_args = chat.generate_input()
    print(instance_args)
    # Create an instance of RPGScenario
    rpg_scenario = RPGScenario(**instance_args)

    rpg_scenario.save(db)
    t2v = TextToVoice(db)
    print(t2v.generate_audio(rpg_scenario, "prologue"))
