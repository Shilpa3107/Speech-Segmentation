from pydub import AudioSegment
import json

audio = AudioSegment.from_wav("long_live.wav")

# Parameters
frame_duration_ms = 30  # 30 ms frames
threshold = -40  # in dBFS, adjust as needed

segments = []
start_time = None

for i in range(0, len(audio), frame_duration_ms):
    frame = audio[i:i+frame_duration_ms]
    if frame.dBFS > threshold:
        if start_time is None:
            start_time = i / 1000  # convert ms to seconds
    else:
        if start_time is not None:
            end_time = i / 1000
            segments.append({"start": start_time, "end": end_time})
            start_time = None

# Handle case where audio ends with speech
if start_time is not None:
    segments.append({"start": start_time, "end": len(audio)/1000})

# Save to JSON
with open("speech_segments.json", "w") as f:
    json.dump(segments, f, indent=2)

print("Speech segments detected and saved in speech_segments.json")
