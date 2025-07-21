from moviepy import VideoFileClip, CompositeVideoClip, TextClip
from moviepy.video.tools.subtitles import SubtitlesClip


def caption_video(video, srt_path: str):#, output_path: str = "subtitled_video.mp4"):
    # Load video

    # Create subtitle generator function
    generator = lambda txt: TextClip(
        "Impact",
        txt,     
        font_size=110,
        color="white",
        method="caption",
        size=(video.w, video.h), 
        stroke_color="black",
        stroke_width=10,
    )

    # Load subtitles from SRT
    subtitles = SubtitlesClip(srt_path, make_textclip=generator)#, encoding="utf-8")

    # print("After subtitles")

    # Overlay subtitles on the video
    video_with_subs = CompositeVideoClip([video, subtitles])

    return video_with_subs

    # Write final output
    # video_with_subs.write_videofile(output_path, codec="libx264", audio_codec="aac")
    # print(f"Saved video with subtitles to: {output_path}")