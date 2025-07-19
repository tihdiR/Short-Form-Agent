from moviepy import VideoFileClip, AudioFileClip

def add_audio(video_path, audio_path, output_path="video_with_audio.mp4"):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    video_with_audio = video.with_audio(audio)
    video_with_audio.write_videofile(output_path, codec="libx264", audio_codec="aac")