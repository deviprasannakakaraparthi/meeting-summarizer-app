import moviepy.editor as mp

def convert_video_to_audio(video_path):
    # Convert video to audio
    video_clip = mp.VideoFileClip(video_path)
    audio_path = "temp_audio_from_video.wav"
    video_clip.audio.write_audiofile(audio_path)
    return audio_path

