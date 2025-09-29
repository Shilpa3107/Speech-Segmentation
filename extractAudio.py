from pydub import AudioSegment

video_file =r"files\long_live.mp4"
audio_output = "long_live.wav"

# Load the file
audio = AudioSegment.from_file(video_file)  # pydub detects mp4 or mp3

# Convert to mono and 16 kHz
audio = audio.set_channels(1)        
audio = audio.set_frame_rate(16000)  

# Export as WAV
audio.export(audio_output, format="wav")

print(f"Audio extracted and saved as {audio_output}")