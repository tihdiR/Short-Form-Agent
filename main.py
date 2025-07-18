import base64

from reddit.scraper import fetch_stories
from reddit.reddit_filter import is_story_interesting
from script_gen.script_generator import reddit_to_script
from video_creator.tts import TTSClient
from video_creator.srt import convert_to_srt

from video_creator.background_video import prepare_background_video
from pydub import AudioSegment



if __name__ == "__main__":
    # print("🚀 Starting scraper...")

    # stories = fetch_stories(limit=1)

    # for i, story in enumerate(stories):
    #     print(f"\n📝 Story #{i+1}")

    #     # OLD
    #     # print(f"Title: {story['title']}")
    #     # print(f"Text: {story['text'] or '[No post text]'}\n")

    #     # if story['comments']:
    #     #     print("Top comments:")
    #     #     for j, comment in enumerate(story['comments']):
    #     #         print(f"  {j+1}. {comment}\n")
    #     # else:
    #     #     print("No comments available.\n")

    #     interesting, confidence = is_story_interesting(story['title'], story['text'])#, story['comments'])
    #     print("interesting: ", interesting)
    #     print("confidence: ", confidence)
    #     script = ""
    #     if interesting:
    #         script = reddit_to_script(story['title'], story['text'])
    #         print(script)
    #     else:
    #         print("NOT INTERESTING ENOUGH")
        
    #     # text = "Hello i am a test"
    #     tts = TTSClient()
    #     result = tts.generate_audio_with_timing(script)
    #     print("✅ Audio generated with timing data.")
    #     # print(result)
    #     # Save audio to file

    #     audio_data = base64.b64decode(result.audio_base_64)
    #     alignment = result.normalized_alignment
    #     print("-------------- ALIGNMENT: ", alignment)
    #     with open("output.wav", "wb") as f:
    #         f.write(audio_data)

        # alignment = {"characters":[' ', 'H', 'e', 'l', 'l', 'o', ' ', 'i', ' ', 'a', 'm', ' ', 'a', ' ', 't', 'e', 's', 't', ' '],
        #     "character_start_times_seconds":[0.0, 0.058, 0.093, 0.151, 0.186, 0.244, 0.395, 0.522, 0.58, 0.639, 0.685, 0.731, 0.778, 0.801, 0.859, 0.906, 1.022, 1.103, 1.149], 
        #     "character_end_times_seconds":[0.058, 0.093, 0.151, 0.186, 0.244, 0.395, 0.522, 0.58, 0.639, 0.685, 0.731, 0.778, 0.801, 0.859, 0.906, 1.022, 1.103, 1.149, 1.486]}
        # alignment = {
        #     "characters": [
        #         'T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'l', 'o', 'n', 'g', 'e', 'r', ' ', 
        #         'e', 'x', 'a', 'm', 'p', 'l', 'e', ' ', 
        #         's', 'e', 'n', 't', 'e', 'n', 'c', 'e', ' ', 
        #         'f', 'o', 'r', ' ', 
        #         's', 'u', 'b', 't', 'i', 't', 'l', 'e', ' ', 
        #         'a', 'l', 'i', 'g', 'n', 'm', 'e', 'n', 't', ' ', 
        #         't', 'e', 's', 't', 'i', 'n', 'g', '.'
        #     ],
        #     "character_start_times_seconds": [
        #         0.0, 0.04, 0.08, 0.12, 0.16, 0.20, 0.24, 0.28, 0.32, 0.36,
        #         0.40, 0.44, 0.48, 0.52, 0.56, 0.60, 0.64, 0.68, 0.72, 0.76,
        #         0.80, 0.84, 0.88, 0.92, 0.96, 1.00, 1.04, 1.08, 1.12, 1.16,
        #         1.20, 1.24, 1.28, 1.32, 1.36, 1.40, 1.44, 1.48, 1.52, 1.56,
        #         1.60, 1.64, 1.68, 1.72, 1.76, 1.80, 1.84, 1.88, 1.92, 1.96,
        #         2.00, 2.04, 2.08, 2.12, 2.16, 2.20, 2.24, 2.28, 2.32, 2.36,
        #         2.40, 2.44, 2.48, 2.52, 2.56, 2.60
        #     ],
        #     "character_end_times_seconds": [
        #         0.04, 0.08, 0.12, 0.16, 0.20, 0.24, 0.28, 0.32, 0.36, 0.40,
        #         0.44, 0.48, 0.52, 0.56, 0.60, 0.64, 0.68, 0.72, 0.76, 0.80,
        #         0.84, 0.88, 0.92, 0.96, 1.00, 1.04, 1.08, 1.12, 1.16, 1.20,
        #         1.24, 1.28, 1.32, 1.36, 1.40, 1.44, 1.48, 1.52, 1.56, 1.60,
        #         1.64, 1.68, 1.72, 1.76, 1.80, 1.84, 1.88, 1.92, 1.96, 2.00,
        #         2.04, 2.08, 2.12, 2.16, 2.20, 2.24, 2.28, 2.32, 2.36, 2.40,
        #         2.44, 2.48, 2.52, 2.56, 2.60, 2.64
        #     ]
        # }
        
        # Save SRT subtitles from timing data
        # srt = convert_to_srt(alignment)

        # with open("output.srt", "w") as f:
        #     f.write(srt)

        # print("✅ Audio and subtitles saved.")

        audio = AudioSegment.from_file("output.wav")
        duration = len(audio) / 1000  # seconds
        print(f"🎵 Audio duration: {duration:.2f} seconds")
        # Generate background video
        background_video_path = prepare_background_video(duration, category="minecraft_test")
        print(f"✅ Background video ready: {background_video_path}")
    
    