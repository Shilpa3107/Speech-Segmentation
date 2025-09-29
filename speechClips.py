from pydub import AudioSegment
import json
import os

# Load audio
audio = AudioSegment.from_wav("long_live.wav")

# Load speech segments
with open("speech_segments.json") as f:
    segments = json.load(f)

# Create output folder if it doesn't exist
output_folder = "segments"
os.makedirs(output_folder, exist_ok=True)

# Export each segment
for idx, seg in enumerate(segments, start=1):
    start_ms = int(seg["start"] * 1000)  # convert seconds to ms
    end_ms = int(seg["end"] * 1000)
    clip = audio[start_ms:end_ms]
    filename = os.path.join(output_folder, f"segment_{idx:02d}.wav")
    clip.export(filename, format="wav")
    print(f"Saved {filename}")

print("All segments exported successfully!")
