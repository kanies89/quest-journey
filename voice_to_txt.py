"""
https://analyzingalpha.com/openai-whisper-python-tutorial

Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a
multitasking model that can perform multilingual speech recognition, speech translation, and language identification.

"""

import whisper
import os
import os
from whisper.audio import load_audio
from whisper import transcribe

model = whisper.load_model("base")
audioPath = os.path.abspath('C:/Users/Admin/OneDrive/Pulpit/Kodilla/Quest/voices/command.wav')
result = model.transcribe(audioPath, fp16=False, language='English')



print(audioPath)

"""result = model.transcribe(audioPath, fp16=False, language='English')"""

print(result["text"])