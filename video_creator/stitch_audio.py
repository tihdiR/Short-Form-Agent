from moviepy import VideoFileClip, AudioFileClip

def add_audio(video, audio_path):
    audio = AudioFileClip(audio_path)
    video_with_audio = video.with_audio(audio)

    return video_with_audio