import base64

from reddit.scraper import fetch_stories
from reddit.reddit_filter import is_story_interesting
from script_gen.script_generator import reddit_to_script
from script_gen.script_generator import clean_text
from script_gen.script_generator import text_to_ssml    
from video_creator.tts import TTSClient
from video_creator.srt import convert_to_srt
from video_creator.srt import convert_to_srt_story
from video_creator.captions import caption_video
from video_creator.stitch_audio import add_audio  
from video_creator.title_image import draw_title_on_template, add_title_to_video
from video_creator.background_video import create_background_video

from pydub import AudioSegment



if __name__ == "__main__":
    # print("🚀 Starting scraper...")

    stories = fetch_stories(limit=1)

    for i, story in enumerate(stories):

        interesting, confidence = is_story_interesting(story['title'], story['text'])

        if interesting:
            story_title = clean_text(story['title'])
            story_text = clean_text(story['text'])
            script = reddit_to_script(story_title, story_text)
            print("script: ", script)
        else:
            print("NOT INTERESTING ENOUGH")

        # script = {
        #     "title": "I crashed my car into a tree and survived",
        #     "story": '''
        #             <speak>
        #             <prosody rate="125%">
        #                 this is one sentence <break time="0ms"/>this is another without pause <break time="0ms"/>and I like to write a lot
        #             </prosody>
        #             </speak>
        #             '''
        # }
        
        #UNCOMMENT-------------------------------
        full_script = f"{text_to_ssml(script['title'] + " " +  script['story'])}"
        # # print("full_script:", full_script)

        tts = TTSClient()
        result = tts.generate_audio_with_timing(full_script)
        # print("✅ Audio generated with timing data.")

        audio_data = base64.b64decode(result.audio_base_64)
        alignment = result.normalized_alignment
        with open("output/test_output2.wav", "wb") as f:
            f.write(audio_data)

        title_len = len(f"{script['title']} ") 

        # # 2. Get the time the title ends
        #UNCOMMENT-------------------------------
        offset_seconds = alignment.character_end_times_seconds[title_len] 
        print("OFFSET ", offset_seconds)
        # offset_seconds = 3.37

        #UNCOMMENT-------------------------------
        # Save SRT subtitles from timing data
        srt = convert_to_srt_story(script, alignment)

        with open("output/output_srt.srt", "w") as f:
            f.write(srt)
    

        audio = AudioSegment.from_file("output/test_output2.wav")

        duration = len(audio) / 1000  # seconds
        # print(f"🎵 Audio duration: {duration:.2f} seconds")
        # # Generate background video
        video_path = create_background_video(duration, offset_seconds, script['title'], category="gta-crash",)

        print(f"✅ Video ready: {video_path}")


    
