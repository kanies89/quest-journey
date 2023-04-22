"""
https://analyzingalpha.com/openai-whisper-python-tutorial

Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a
multitasking model that can perform multilingual speech recognition, speech translation, and language identification.

"""

import pyaudio
import webrtcvad
import whisper
import wave

# Constants
PATH = 'voices/command.wav'
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK_DURATION_MS = 30  # supports 10, 20 and 30 (ms)
PADDING_DURATION_MS = 1500  # 1.5 seconds
CHUNK_SIZE = int(RATE * CHUNK_DURATION_MS / 1000)  # chunk to read from mic
NUM_PADDING_CHUNKS = int(PADDING_DURATION_MS / CHUNK_DURATION_MS)
NUM_WINDOW_CHUNKS = int(240 / CHUNK_DURATION_MS)  # 240 ms VAD
NUM_VAD_CHUNKS = int(1500 / CHUNK_DURATION_MS)  # 1500 ms (1.5 sec) of utterance
MAX_SILENCE_DURATION_MS = 1000  # max duration of silence to wait for after end of utterance

# Create audio stream
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
                frames_per_buffer=CHUNK_SIZE)

# Create VAD object
vad = webrtcvad.Vad(3)


def save_to_wav(wav_data):
    # Open WAV file for writing
    with wave.open(PATH, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(wav_data)


def detect():
    # Variables for voice detection
    num_pad_chunks = NUM_PADDING_CHUNKS
    num_vad_chunks = 0
    voice_detected = False
    frames = []
    silence_duration = 0

    while True:
        # Read audio chunk from microphone
        audio_chunk = stream.read(CHUNK_SIZE)

        # Check for voice activity
        is_speech = vad.is_speech(audio_chunk, RATE)

        if not voice_detected:
            if is_speech:
                voice_detected = True
                num_pad_chunks = 0
                num_vad_chunks = 0
                frames = []
                silence_duration = 0
        else:
            if is_speech:
                num_vad_chunks += 1
                silence_duration = 0
            else:
                num_vad_chunks = 0
                num_pad_chunks += 1
                silence_duration += CHUNK_DURATION_MS

            # Record audio frames while voice is detected
            frames.append(audio_chunk)

            # End of utterance condition
            if num_vad_chunks >= NUM_VAD_CHUNKS or num_pad_chunks >= NUM_PADDING_CHUNKS:
                voice_detected = False
                if silence_duration < MAX_SILENCE_DURATION_MS:
                    continue
                wav_data = b''.join(frames)
                save_to_wav(wav_data)
                # Reset variables
                num_pad_chunks = NUM_PADDING_CHUNKS
                num_vad_chunks = 0
                frames = []
                silence_duration = 0

                break


def use_whisper() -> str:
    # Use whisper for audio to text
    model = whisper.load_model("base")
    result = model.transcribe(PATH, fp16=False, language='English')
    print(result["text"])
    return result["text"]
