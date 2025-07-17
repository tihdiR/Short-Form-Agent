# from datetime import timedelta

# def format_srt_time(seconds):
#     td = timedelta(seconds=seconds)
#     total_seconds = int(td.total_seconds())
#     ms = int((td.total_seconds() - total_seconds) * 1000)
#     return f"{str(td)}".zfill(8).replace('.', ',')[:-3] + f",{ms:03d}"

# def convert_to_srt(alignment_data, max_words_per_caption=8):
#     chars = alignment_data['characters']
#     starts = alignment_data['character_start_times_seconds']
#     ends = alignment_data['character_end_times_seconds']

#     words = []
#     current_word = ""
#     current_start = None
#     current_end = None

#     for i, char in enumerate(chars):
#         if current_word == "":
#             current_start = starts[i]

#         current_word += char
#         current_end = ends[i]

#         if char in " \n.,;!?":  # Treat punctuation as word end
#             words.append({
#                 "text": current_word.strip(),
#                 "start": current_start,
#                 "end": current_end
#             })
#             current_word = ""

#     # Group into captions
#     captions = []
#     current_caption = []
#     for word in words:
#         current_caption.append(word)
#         if len(current_caption) >= max_words_per_caption:
#             captions.append(current_caption)
#             current_caption = []

#     if current_caption:
#         captions.append(current_caption)

#     # Create SRT
#     srt = ""
#     for i, caption in enumerate(captions):
#         start = format_srt_time(caption[0]['start'])
#         end = format_srt_time(caption[-1]['end'])
#         text = ' '.join([w['text'] for w in caption])

#         srt += f"{i+1}\n{start} --> {end}\n{text.strip()}\n\n"

#     return srt

from datetime import timedelta

def format_srt_time(seconds):
    """
    Formats a given number of seconds into the SRT time format (HH:MM:SS,ms).

    Args:
        seconds (float): The total number of seconds.

    Returns:
        str: The formatted time string (e.g., "00:00:01,880").
    """
    # Ensure seconds is non-negative
    seconds = max(0, seconds)

    # Calculate hours, minutes, seconds, and milliseconds
    total_milliseconds = int(seconds * 1000)
    ms = total_milliseconds % 1000
    total_seconds_int = total_milliseconds // 1000
    s = total_seconds_int % 60
    m = (total_seconds_int // 60) % 60
    h = total_seconds_int // 3600

    # Format as HH:MM:SS,ms with leading zeros
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def convert_to_srt(alignment_data, max_words_per_caption=8):
    """
    Converts character-level alignment data into an SRT subtitle string.

    Args:
        alignment_data (dict): A dictionary containing:
            - 'characters' (list of str): List of individual characters.
            - 'character_start_times_seconds' (list of float): Start time for each character.
            - 'character_end_times_seconds' (list of float): End time for each character.
        max_words_per_caption (int): The maximum number of words allowed per subtitle caption.

    Returns:
        str: The generated SRT subtitle string.
    """
    chars = alignment_data['characters']
    starts = alignment_data['character_start_times_seconds']
    ends = alignment_data['character_end_times_seconds']

    words = []
    current_word = ""
    current_start = None
    current_end = None

    # Iterate through characters to extract words and their timings
    for i, char in enumerate(chars):
        # If starting a new word, record its start time
        if current_word == "":
            current_start = starts[i]

        current_word += char
        # Always update current_end to the end time of the last character processed.
        # This means the end time of a word will include any trailing punctuation's duration.
        current_end = ends[i]

        # If the current character is a delimiter, it marks the end of a word
        if char in " \n.,;!?":
            # Only append if current_word has actual text (after stripping delimiters)
            if current_word.strip():
                words.append({
                    "text": current_word.strip(),
                    "start": current_start,
                    "end": current_end # End time includes the delimiter's duration
                })
            current_word = "" # Reset for the next word

    # Handle any remaining word after the loop (e.g., if the text doesn't end with a delimiter)
    if current_word.strip():
        words.append({
            "text": current_word.strip(),
            "start": current_start,
            "end": current_end
        })

    # Group words into captions based on max_words_per_caption
    captions = []
    current_caption = []
    for word in words:
        current_caption.append(word)
        # If the current caption reaches the max word limit, finalize it
        if len(current_caption) == max_words_per_caption:
            captions.append(current_caption)
            current_caption = [] # Start a new caption

    # Add any remaining words as the last caption
    if current_caption:
        captions.append(current_caption)

    # Generate the final SRT string
    srt = ""
    for i, caption in enumerate(captions):
        # The start time of the caption is the start time of its first word
        start_time_str = format_srt_time(caption[0]['start'])
        # The end time of the caption is the end time of its last word
        end_time_str = format_srt_time(caption[-1]['end'])
        # Join all word texts to form the caption text
        caption_text = ' '.join([w['text'] for w in caption])

        # Append the SRT entry with the correct format
        srt += f"{i+1}\n{start_time_str} --> {end_time_str}\n{caption_text.strip()}\n\n"

    return srt