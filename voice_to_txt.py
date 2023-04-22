"""
https://analyzingalpha.com/openai-whisper-python-tutorial

Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a
multitasking model that can perform multilingual speech recognition, speech translation, and language identification.

"""

import whisper

model = whisper.load_model("base")
audioPath = ("/".join(["voices", "command.wav"]))
print(audioPath)

result = model.transcribe(audioPath, fp16=False, language='English')

print(result["text"])