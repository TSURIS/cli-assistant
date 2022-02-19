import os
from pocketsphinx import LiveSpeech, Pocketsphinx, get_model_path, get_data_path

model_path = get_model_path()
data_path = get_data_path()

for phrase in LiveSpeech(audio_device='plughw:1,0',):
    #print(phrase, end=' ')
    print(f'Said: {phrase}')
else:
    print("Sphinx cannot recognize")