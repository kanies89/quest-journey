from TTS.api import TTS
from shutil import which
print(which('espeak'))
print(which('espeak-ng'))

def txt_tov(filename, text):
    OUTPUT_1 = "/".join(["voices", filename])
    OUTPUT_2 = "/".join(["voices", "coqui", filename])
    model_name = TTS.list_models()[0]
    # Init TTS
    tts = TTS(model_name)
    # wav = tts.tts("This is a test! This is also a test!!", speaker=tts.speakers[3], language=tts.languages[0])
    # tts.tts_to_file(text=text, speaker_wav="my/cloning/audio.wav", language="en", file_path=OUTPUT_1)
    # Init TTS with the target model name
    tts = TTS(model_name="tts_models/en/ljspeech/vits--neon", progress_bar=False, gpu=False)
    # Run TTS
    tts.tts_to_file(text=text, file_path=OUTPUT_1)

    # If you have a valid API token set you will see the studio speakers as separate models in the list.
    # The name format is coqui_studio/en/<studio_speaker_name>/coqui_studio
    models = TTS().list_models()
    # Init TTS with the target studio speaker
    tts = TTS(model_name="coqui_studio/en/Damien Black/coqui_studio", progress_bar=False, gpu=False)
    # Run TTS
    tts.tts_to_file(text=text, file_path=OUTPUT_2)