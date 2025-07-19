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
from video_creator.background_video import prepare_background_video

from pydub import AudioSegment



if __name__ == "__main__":
    # print("🚀 Starting scraper...")

    # stories = fetch_stories(limit=1)

    # for i, story in enumerate(stories):
    #     print(f"\n📝 Story #{i+1}")

        # OLD
        # print(f"Title: {story['title']}")
        # print(f"Text: {story['text'] or '[No post text]'}\n")

        # if story['comments']:
        #     print("Top comments:")
        #     for j, comment in enumerate(story['comments']):
        #         print(f"  {j+1}. {comment}\n")
        # else:
        #     print("No comments available.\n")

        # interesting, confidence = is_story_interesting(story['title'], story['text'])#, story['comments'])
        # print("interesting: ", interesting)
        # print("confidence: ", confidence)
        # script = ""
        # if interesting:
        #     script = reddit_to_script(story['title'], story['text'])
        #     # print(script)
        #     print(script['title'])
        #     print(script['story'])
        # else:
        #     print("NOT INTERESTING ENOUGH")
        
        script = {"title": "Hello", "story": "i am a test"}
        # text = "Hello i am a test"
        full_script = f"{script['title']}. {script['story']}"
        print("Full script:", full_script)
        # tts = TTSClient()
        # result = tts.generate_audio_with_timing(full_script)
        # print("✅ Audio generated with timing data.")
        # print(result)
        # Save audio to file

        # audio_data = base64.b64decode(result.audio_base_64)
        # alignment = result.normalized_alignment
        # print("-------------- ALIGNMENT: ", alignment)
        # with open("output.wav", "wb") as f:
        #     f.write(audio_data)

        alignment = {"characters":[' ', 'H', 'e', 'l', 'l', 'o', ' ', 'i', ' ', 'a', 'm', ' ', 'a', ' ', 't', 'e', 's', 't', ' '],
            "character_start_times_seconds":[0.0, 0.058, 0.093, 0.151, 0.186, 0.244, 0.395, 0.522, 0.58, 0.639, 0.685, 0.731, 0.778, 0.801, 0.859, 0.906, 1.022, 1.103, 1.149], 
            "character_end_times_seconds":[0.058, 0.093, 0.151, 0.186, 0.244, 0.395, 0.522, 0.58, 0.639, 0.685, 0.731, 0.778, 0.801, 0.859, 0.906, 1.022, 1.103, 1.149, 1.486]}
        
        title_len = len(f"{script['title']}. ")  # Adjust as needed based on your formatting

        # # 2. Get the time the title ends
        offset_seconds = alignment['character_end_times_seconds'][title_len] 
        # print(f"Title ends at {offset_seconds:.2f} seconds")
        
        # # story_chars = alignment['characters'][title_len:]
        # # story_starts = alignment['character_start_times_seconds'][title_len:]
        # # story_ends = alignment['character_end_times_seconds'][title_len:]

        # story_align = alignment.copy()
        # story_align['characters'] = story_align['characters'][title_len:]
        # story_align['character_start_times_seconds'] = story_align['character_start_times_seconds'][title_len:]
        # story_align['character_end_times_seconds'] = story_align['character_end_times_seconds'][title_len:]

        # print(story_align)

        # Save SRT subtitles from timing data
        # srt = convert_to_srt(alignment)

        # with open("output_new.srt", "w") as f:
        #     f.write(srt)

        # srt = convert_to_srt_story(script, alignment)

        # with open("output_new.srt", "w") as f:
        #     f.write(srt)

       

        # audio = AudioSegment.from_file("output/output.wav")

        # duration = 10 #len(audio) / 1000  # seconds
        # print(f"🎵 Audio duration: {duration:.2f} seconds")
        # # Generate background video
        # background_video_path = prepare_background_video(duration, category="minecraft_test")
        # print(f"✅ Background video ready: {background_video_path}")

        caption_video("output/background_minecraft_test.mp4", "output/output_new.srt", "output/subtitled_video.mp4")

        add_title_to_video(
            video_path="output/subtitled_video.mp4",
            title_frame="output/title_frame.png",
            output_path="output/subtitled_video.mp4",
            duration = offset_seconds
        )

        add_audio("output/subtitled_video.mp4", "output/output.wav", "output/final_video.mp4")
        # print("✅ Audio and subtitles saved.")

        # draw_title_on_template(
        #     # template_path="assets/reddit_title_template.png",
        #     template_path="assets/title_template2.png",
        #     title_text=script['title'],
        #     output_path="output/title_frame.png",
        # )


    
