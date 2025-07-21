from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont
from moviepy import VideoFileClip, ImageClip, CompositeVideoClip
import os
import textwrap

def getsize(font, text):
    left, top, right, bottom = font.getbbox(text)
    width = right - left
    height = bottom - top
    return width, height


def getheight(font, text):
    _, height = getsize(font, text)
    return height

def draw_title_on_template(template_path, title_text, output_path, font_size=47, padding=5, wrap=35):
    # Load image
    img = Image.open(template_path).convert("RGBA")

    font = ImageFont.truetype("assets/fonts/roberto_2/Roberto-bold.ttf", font_size)

    image_width, image_height = img.size

    lines = textwrap.wrap(title_text, width=wrap)

    y = (
        (image_height / 2)
        - (((getheight(font, title_text) + (len(lines) * padding) / len(lines)) * len(lines)) / 2)
        + 30
    )

    draw = ImageDraw.Draw(img)

    username_font = ImageFont.truetype("assets/fonts/roberto_2/Roberto-bold.ttf", 30)
    draw.text(
        (205, 825),
        "u/redditboy",
        font=username_font,
        fill="black",
        align="left",
    )

    if len(lines) == 3:
        lines = textwrap.wrap(title_text, width=wrap + 10)
        font_title_size = 40
        font = ImageFont.truetype("assets/fonts/roberto_2/Roberto-bold.ttf", font_title_size)
        y = (
            (image_height / 2)
            - (((getheight(font, title_text) + (len(lines) * padding) / len(lines)) * len(lines)) / 2)
            + 35
        )
    elif len(lines) == 4:
        lines = textwrap.wrap(title_text, width=wrap + 10)
        font_title_size = 35
        font = ImageFont.truetype("assets/fonts/roberto_2/Roberto-bold.ttf", font_title_size)
        y = (
            (image_height / 2)
            - (((getheight(font, title_text) + (len(lines) * padding) / len(lines)) * len(lines)) / 2)
            + 40
        )
    elif len(lines) > 4:
        lines = textwrap.wrap(title_text, width=wrap + 10)
        font_title_size = 30
        font = ImageFont.truetype("assets/fonts/roberto_2/Roberto-bold.ttf", font_title_size)
        y = (
            (image_height / 2)
            - (((getheight(font, title_text) + (len(lines) * padding) / len(lines)) * len(lines)) / 2)
            + 30
        )

    for line in lines:
        draw.text((120, y), line, font=font, fill="black", align="left")
        y += getheight(font, line) + padding

    img.save(output_path)


def add_title_to_video(video, title_frame, duration):

    title_clip = ImageClip(title_frame, duration = duration)

    # title_clip = title_clip.set_duration(3)
    # title_clip = title_clip.set_position(("center", "center"))

    final = CompositeVideoClip([video, title_clip])

    return final