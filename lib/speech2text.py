import vosk
import sys
import os
import wave
import subprocess
import sounddevice as sd
import numpy as np
import speech_recognition as sr
#model_path = "lib/models/vosk/vosk-model-small-fr-0.22/"
model_path = "lib/models/vosk/vosk-model-fr-0.22/"
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
sample_rate = 16000
recognizer = vosk.KaldiRecognizer(vosk.Model(model_path), sample_rate)
duration = 5  # Dur?e d'enregistrement en secondes
output_file = os.path.join(output_dir, "question.wav")
fs = 44100  # Fr?quence d'?chantillonnage
duration_signal = 0.2  # Dur?e du signal en secondes
t = np.linspace(0, duration_signal, int(duration_signal * fs), False)
start_signal = np.sin(2 * np.pi * 440 * t)  # Signal sonore pour le top d?part
end_signal = np.sin(2 * np.pi * 880 * t)  # Signal sonore pour le top fin
def play_signal(signal):
    sd.play(signal, samplerate=fs, blocking=True)
play_signal(start_signal)
arecord_cmd = f"arecord -f S16_LE -r {sample_rate} -c 1 -d {duration} {output_file}"
subprocess.call(arecord_cmd, shell=True)
play_signal(end_signal)
r = sr.Recognizer()
with sr.AudioFile(output_file) as audio_file:
    audio = r.record(audio_file)
text = r.recognize_google(audio, language="fr-FR")
print(text)
