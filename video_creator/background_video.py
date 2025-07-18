import os
import json
import random
import yt_dlp
from moviepy import VideoFileClip
from pathlib import Path

# TikTok resolution
TIKTOK_WIDTH = 1080
TIKTOK_HEIGHT = 1920

# Load background options from JSON file
def load_background_sources(json_path="utils/background_videos.json"):
    with open(json_path, "r") as f:
        return json.load(f)

def download_video(uri: str, filename: str, output_dir="output/backgrounds") -> str:
    """
    Downloads the background video using yt_dlp and returns the full file path.
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    if os.path.exists(output_path):
        print(f"✅ Video already exists: {output_path}")
        return output_path
    
    print(f"   URL: {uri}")
    print(f"   Saving to: {output_dir}")

    ydl_opts = {
        "format": "bestvideo[height<=1080][ext=mp4]",
        "outtmpl": output_path,
        "retries": 10,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([uri])

    print(f"🎉 Downloaded background video: {output_path}")
    return output_path

# Trim and crop video to TikTok dimensions
def process_background_video(input_path, output_path, target_duration):
    print(f"✂️ Trimming and cropping to {target_duration}s...")
    clip = VideoFileClip(input_path)

    if target_duration > clip.duration:
        raise ValueError(f"Target duration ({target_duration}s) is longer than video ({clip.duration}s)")

    # Random start time
    max_start = clip.duration - target_duration
    start_time = random.uniform(0, max_start)
    end_time = start_time + target_duration
    print(f"🎯 Selected interval: {start_time:.2f}s to {end_time:.2f}s")

    # Trim to random interval
    trimmed = clip.subclipped(start_time, end_time)#.resized(height=TIKTOK_WIDTH, width =TIKTOK_HEIGHT)
    trimmed = trimmed.resized(height=1920)

    # Now crop the width to 1080 center
    trimmed = trimmed.cropped(width=1080, x_center=trimmed.w/2)

    # width, height = trimmed.size
    # print(f"Video dimensions: {width}x{height}")

    trimmed.write_videofile(output_path, codec="libx264", audio=False, fps=30)

    print(f"🎥 Processed and saved: {output_path}")

# Main runner
def prepare_background_video(duration_seconds, category=None):
    backgrounds = load_background_sources()
    keys = list(backgrounds.keys())

    if category and category in backgrounds:
        key = category
    else:
        key = random.choice(keys)

    url, filename, author, format = backgrounds[key]
    input_path = download_video(url, filename)
    output_path = f"output/background_{key}.mp4"

    process_background_video(input_path, output_path, duration_seconds)
    return output_path
