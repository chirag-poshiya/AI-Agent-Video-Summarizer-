import moviepy.editor as mp
from pytube import YouTube
import tempfile
import os
from PIL import Image
import io
import speech_recognition as sr

def process_video(video_input):
    """Process video file or URL and extract frames and audio text"""
    
    # Handle YouTube URL
    if isinstance(video_input, str):
        yt = YouTube(video_input)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_file:
            video_stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
            video_stream.download(filename=tmp_file.name)
            video_path = tmp_file.name
    else:
        # Handle uploaded file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_file:
            tmp_file.write(video_input.read())
            video_path = tmp_file.name

    # Load video
    video = mp.VideoFileClip(video_path)
    
    # Extract frames at intervals
    duration = video.duration
    frames = []
    for t in range(0, int(duration), max(1, int(duration/5))):  # Extract 5 frames
        frame = video.get_frame(t)
        img = Image.fromarray(frame)
        img.thumbnail((300, 300))  # Resize for efficiency
        frames.append(img)
    
    # Extract audio and convert to text
    audio = video.audio
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_audio:
        audio.write_audiofile(tmp_audio.name)
        # Use the speech_recognition library to transcribe audio
        recognizer = sr.Recognizer()
        with sr.AudioFile(tmp_audio.name) as source:
            audio_data = recognizer.record(source)
            try:
                audio_text = recognizer.recognize_google(audio_data)
            except sr.UnknownValueError:
                audio_text = "Audio unclear, could not transcribe."
            except sr.RequestError:
                audio_text = "Speech recognition service unavailable."
    
    # Cleanup
    video.close()
    os.unlink(video_path)
    
    return frames, audio_text 