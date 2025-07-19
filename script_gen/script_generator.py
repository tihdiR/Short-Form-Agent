from llm import LLMClient
import json

llm = LLMClient()

def reddit_to_script(title: str, text: str) -> str:#, comments: list[str]) -> str:
    prompt = f"""
        You are an editor for Reddit stories for TikTok and YouTube Shorts.

        Here is a Reddit story:

        Title: {title}

        Text: {text}

        Edit the story and title so that:
        - The first sentence be the hook to grab the viewer's attention, it should be a simple one sentence line
          That makes the reader intrigued. It is not necessary to change the provided title, but it should be engaging.
        - Dosn't add any unnecessary fluff, the text should read smoothly and be focused on the main story.
        - Cuts any fluff from the post that doesn't add to the story 
        - Lasts at least 1 minute (minimum 150–200 words)
        - If there is not enough content to reach 1 minute, add additional context or details to flesh it out
        
        Output your response as JSON with two keys: "title" and "story".
        Respond with ONLY the script in this format with the title and story text formatted to be input into a text to speech system.

        Expected format:
        {{
          "title": "title of the story",
          "story": "story text"
        }}
       
    """

    result = llm.generate(prompt, temperature=0.8, max_tokens=750)
    clean_result = result.replace("```json", "").replace("```", "").strip()
    # print("LLM result:", result)
    json_result = json.loads(clean_result)
    return json_result
    # return result.strip()
