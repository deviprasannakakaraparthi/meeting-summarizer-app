import streamlit as st
from audio_processing.audio_to_text import convert_audio_to_text
from audio_processing.video_to_audio import convert_video_to_audio
from utils.summarizer import summarize_text

# Set the title of the app
st.title("Automated Meeting Summarizer")
st.markdown("Upload your meeting audio or video file to get a summarized report!")

# File upload section
uploaded_file = st.file_uploader("Choose an audio/video file", type=["mp4", "mp3", "wav"])

if uploaded_file is not None:
    file_extension = uploaded_file.name.split('.')[-1]
    
    # Handle audio files
    if file_extension in ["mp3", "wav"]:
        st.audio(uploaded_file, format='audio/wav')
        text = convert_audio_to_text(uploaded_file)
        summary = summarize_text(text)
        st.write("Summary:")
        st.write(summary)
    
    # Handle video files
    elif file_extension == "mp4":
        video_path = "uploaded_video.mp4"
        with open(video_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        audio_path = convert_video_to_audio(video_path)
        text = convert_audio_to_text(audio_path)
        summary = summarize_text(text)
        st.write("Summary:")
        st.write(summary)

