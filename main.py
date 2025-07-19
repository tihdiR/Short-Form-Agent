import base64

from reddit.scraper import fetch_stories
from reddit.reddit_filter import is_story_interesting
from script_gen.script_generator import reddit_to_script
from video_creator.tts import TTSClient
from video_creator.srt import convert_to_srt
from video_creator.srt import convert_to_srt_story
from video_creator.captions import caption_video
from video_creator.stitch_audio import add_audio  
from video_creator.title_image import draw_title_on_template, add_title_to_video
from video_creator.background_video import create_background_video

from pydub import AudioSegment



if __name__ == "__main__":
    print("🚀 Starting scraper...")

    stories = fetch_stories(limit=1)

    for i, story in enumerate(stories):

        interesting, confidence = is_story_interesting(story['title'], story['text'])

        if interesting:
            script = reddit_to_script(story['title'], story['text'])
        else:
            print("NOT INTERESTING ENOUGH")
        
        #UNCOMMENT-------------------------------
        # full_script = f"{script['title']}. {script['story']}"

        # tts = TTSClient()
        # result = tts.generate_audio_with_timing(full_script)
        # print("✅ Audio generated with timing data.")

        # audio_data = base64.b64decode(result.audio_base_64)
        # alignment = result.normalized_alignment
        # with open("output/output.wav", "wb") as f:
        #     f.write(audio_data)

        title_len = len(f"{script['title']}. ") 

        # # 2. Get the time the title ends
        #UNCOMMENT-------------------------------
        # offset_seconds = alignment.character_end_times_seconds[title_len] 
        offset_seconds = 3.37

        #UNCOMMENT-------------------------------
        # Save SRT subtitles from timing data
        # srt = convert_to_srt_story(script, alignment)

        # with open("output/output_srt.srt", "w") as f:
        #     f.write(srt)
    

        audio = AudioSegment.from_file("output/output.wav")

        duration = len(audio) / 1000  # seconds
        # print(f"🎵 Audio duration: {duration:.2f} seconds")
        # # Generate background video
        video_path = create_background_video(duration, offset_seconds, script['title'], category="minecraft_test",)
        
        print(f"✅ Video ready: {video_path}")


    
