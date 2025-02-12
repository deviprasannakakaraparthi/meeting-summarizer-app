import speech_recognition as sr

def convert_audio_to_text(audio_file):
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Save the uploaded audio file as a temporary WAV file
    audio_path = "temp_audio.wav"
    with open(audio_path, "wb") as f:
        f.write(audio_file.getbuffer())
    
    # Perform speech recognition on the audio file
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Audio could not be understood."
        except sr.RequestError:
            return "Request failed, please check your internet connection."

