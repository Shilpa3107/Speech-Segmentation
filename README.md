# Speech Segmentation from Audio
## Project Overview

This project processes an audio file (or extracts audio from a video) and segments it into smaller clips based on speech activity. The main goal is to detect portions of the audio where speech occurs and save them as individual audio files.
It is implemented in Python using pydub for audio processing and basic amplitude/energy thresholding for speech detection.

## Features
1. Extract audio from a video file and convert it to a standard format:
   - Mono channel
   - 16 kHz sample rate
2. Detect speech segments based on audio amplitude:
   - Differentiates between speech and silence/background noise
   - Stores timestamps of speech segments in a JSON file
3. Segment and export continuous speech clips:
   - Each speech segment is saved as a separate .wav file
   - Files are named systematically (segment_01.wav, segment_02.wav, etc.)
4. Optional visualization:
   - Shows a waveform of the audio with detected speech segments highlighted

## Requirements
  - Python 3.12 or later
  - Python libraries:
```bash
pydub
numpy
matplotlib (optional, for visualization)
```
   - FFmpeg installed (required by pydub for some formats like mp4 or mp3)

## Setup and Usage
1. Install required libraries:
```bash
pip install pydub numpy matplotlib
```
2. Place your input video/audio file in the project folder.
3. Run the audio extraction script (if starting from a video):
```bash
python extractAudio.py
```
4. Run the speech detection script:
```bash
python detectSpeechSegments.py
```
5. Run the segmentation script to export speech clips:
```bash
python exportSegments.py
```
6. Output:
 - long_live.wav → extracted audio
 - speech_segments.json → timestamps of speech segments
 - segments/ → folder containing all speech clips

## File Structure
Speech-Segmentation/

│

├── extractAudio.py          # Extracts audio from video or converts audio

├── detectSpeechSegments.py  # Detects speech segments and saves JSON

├── exportSegments.py        # Splits audio into clips based on JSON

├── speech_segments.json     # Output JSON of detected speech timestamps

├── long_live.wav            # Extracted audio file

├── segments/                # Folder containing speech segment audio clips

└── README.md                # Project overview and instructions

## How it works
1. The audio is processed in small frames (e.g., 30 ms each).
2. Each frame's amplitude (volume) is measured.
3. Frames above a set threshold are marked as speech.
4. Consecutive speech frames are merged into continuous segments.
5. Each segment is exported as an individual audio file.

## Optional Visualization

- The waveform of the audio can be plotted using matplotlib.
- Gray waveform → represents the original audio signal.
- Red highlighted regions → represent the detected speech segments.
- This visualization helps verify the accuracy of speech detection.
