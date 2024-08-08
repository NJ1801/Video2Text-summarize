import streamlit as st
from moviepy.editor import VideoFileClip
import speech_recognition as sr
import os

# Streamlit app
st.title('Video to Text Transcription')

# File uploader for the video
uploaded_video = st.file_uploader("Upload a video file", type=["mp4"])

if uploaded_video is not None:
    # Save the uploaded video to a file
    video_path = "Extracted_video.mp4"
    with open(video_path, "wb") as f:
        f.write(uploaded_video.read())

    # Extract audio from the video file
    audio_path = "Extracted_audio.wav"
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)

    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Open the audio file
    with sr.AudioFile(audio_path) as source:
        audio_text = r.record(source)

    # Recognize the speech in the audio
    try:
        text = r.recognize_google(audio_text, language='en-US')
        st.write("Transcription:")
        st.write(text)

        # Save transcription to a file
        file_name = "Extraction_Transcription.txt"
        with open(file_name, "w") as file:
            file.write(text)

        # Provide a download link for the transcription file
        st.download_button(label="Download Transcription", data=open(file_name, "rb").read(), file_name=file_name)

    except sr.UnknownValueError:
        st.error("Sorry, could not understand the audio")
    except sr.RequestError:
        st.error("Sorry, there was an error with the speech recognition service")
