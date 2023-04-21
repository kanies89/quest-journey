from core import RPGScenario, TextToVoice
from game_db import Database
from make import ChatGPTMake
import os
import simpleaudio as sa


def play(obj):
    print(1)
    audio = []
    for field in obj.fields:
        print(field[0])
        if "audio" in field[0]:
            audio.append(field[0])
    print(audio)
    if len(audio) == 1 and audio[0] == "prologue_audio":
        wave_obj = sa.WaveObject.from_wave_file("voices/ui/prologue.wav")

        play_obj = wave_obj.play()
        play_obj.wait_done()
        play = input(f"Yes / No")
        if play == "Yes":
            wave_obj = sa.WaveObject.from_wave_file("/".join(["voices", obj.prologue_audio]))
            play_obj = wave_obj.play()
            play_obj.wait_done()


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

    # Generate voice
    t2v = TextToVoice(db)
    t2v.generate_audio(rpg_scenario, "prologue")

    scenario_id = rpg_scenario.id
    print(scenario_id)
    prologue_voice = RPGScenario.load(db, scenario_id)
    print(prologue_voice)
    play(prologue_voice)
