from pydub import AudioSegment
import matplotlib.pyplot as plt
import json
import numpy as np

# Load audio
audio = AudioSegment.from_wav("long_live.wav")
samples = np.array(audio.get_array_of_samples())

# Time axis in seconds
time = np.linspace(0, len(audio)/1000, num=len(samples))

# Plot waveform
plt.figure(figsize=(15,4))
plt.plot(time, samples, color='lightgray')
plt.title("Audio Waveform with Speech Segments")

# Load speech segments
with open("speech_segments.json") as f:
    segments = json.load(f)

# Overlay segments
for seg in segments:
    plt.axvspan(seg["start"], seg["end"], color='red', alpha=0.3)

plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
