import whisper
import os
import sys

stdout_fileno = sys.stdout

sys.stdout = open('voicemails.txt','w')

model = whisper.load_model("tiny.en")

for file_name in os.listdir():
    if file_name.endswith('.wav'):
        print(file_name)
        audio = whisper.load_audio(file_name)
        result = model.transcribe(audio)
        print(result["text"])

sys.stdout.close()
sys.stdout = stdout_fileno


