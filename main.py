import streamlit as st
import librosa
import soundfile as sf
import numpy as np
from transformers import pipeline
from IPython.display import Audio, display

whisper = pipeline('automatic-speech-recognition', model = 'openai/whisper-medium')
audio_file = './wave_2.wav'
text = whisper(audio_file)
print(text)
# return text

from googletrans import Translator
translator = Translator()

langs = ['hi','ja','pa','mr','gu']

from gtts import gTTS

count = 0
for i in langs:
  res = translator.translate(text,dest=i)
  speech = gTTS(text = res.text)
  speech.save(f'{count}_{i}.mp3')
  count +=1
# def process_audio(audio_file):
#     # Read the audio file
#     audio_signal, sr = librosa.load(audio_file, sr=None)
#     text = whisper('/content/audio.wav')

#     # Example processing - Add some noise
#     # audio_with_noise = audio_signal + 0.1 * np.random.normal(size=len(audio_signal))

#     return text
# 5

# def process_audio(audio_file):

# def main():
#     st.title("Audio Processing App")

#     # File upload
#     audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

#     if audio_file is not None:
#         st.audio(audio_file, format='audio/{}'.format(audio_file.name.split('.')[-1]))

#         # Process audio
#         if st.button("Process Audio"):
#             audio_array, sr = process_audio(audio_file)
#             st.audio(audio_array, format='audio/wav', sample_rate=sr)

# if __name__ == "__main__":
#     main()
