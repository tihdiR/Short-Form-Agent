from llm import LLMClient
import json
import re
from cleantext import clean

llm = LLMClient()

def clean_text(text):
    regex_urls = r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"

    result = re.sub(regex_urls, " ", text)

    # note: not removing apostrophes
    regex_expr = r"\s['|’]|['|’]\s|[\^_~@!&;#:\-%—“”‘\"%\*/{}\[\]\(\)\\|<>=+]"
    result = re.sub(regex_expr, " ", result)
    result = result.replace("+", "plus").replace("&", "and")

    # remove extra whitespace
    result = " ".join(result.split())
    
    return result

def text_to_ssml(text, rate="125%"):
    # Split text into sentences (basic version using punctuation)
    sentences = re.split(r'(?<=[.?!])\s+', text.strip())

    # Filter empty sentences and join with 0ms break
    ssml_body = '<break time="0ms"/>'.join(sentence.strip() for sentence in sentences if sentence.strip())

    # Wrap in <speak> and optional prosody (rate control)
    ssml = f'<speak><prosody rate="{rate}">{ssml_body}</prosody></speak>'
    return ssml

def reddit_to_script(title: str, text: str) -> str:#, comments: list[str]) -> str:
    prompt = f"""
        You are an editor for Reddit stories for TikTok and YouTube Shorts.

        Here is a Reddit story:

        Title: {title}

        Text: {text}

        Edit the story and title so that:
        - The title sentence be the hook to grab the viewer's attention, it should be a simple one sentence line
          That makes the reader intrigued. It is not necessary to change the provided title, but it should be engaging.
        - Doesn't not repeat the title at the start of the story.
        - Doesn't add any unnecessary fluff, the text should read smoothly and be focused on the main story.
        - Cuts any fluff from the post that doesn't add to the story 
        - Lasts at least 1 minute (minimum 150–200 words)
        - If there is not enough content to reach 1 minute, add additional context or details to flesh it out
        - Write it so that that it is dircet and concise but still has a natural flow
        - Format it for a text-to-speech system where there are less pauses or breaks.
          Don't use complicated sentence structure.
        
        Output your response as JSON with two keys: "title" and "story".
        Respond with ONLY the script in this format with the title and story text formatted to be input into a text to speech system with no newlines.

        Expected format:
        {{
          "title": "title of the story",
          "story": "story text"
        }}
       
    """

    result = llm.generate(prompt, temperature=0.8, max_tokens=750)

    clean_result = result.replace("```json", "").replace("```", "").strip()
    # # print("LLM result:", result)
    # def escape_unescaped_newlines(match):
    #     return match.group(0).replace("\n", "\\n")
    
    # clean = re.sub(r'".*?(?<!\\)"', escape_unescaped_newlines, clean_result, flags=re.DOTALL)

    json_result = json.loads(clean_result)

    # json_result["story"] = text_to_ssml(json_result["story"])


    return json_result
    # return result.strip()
