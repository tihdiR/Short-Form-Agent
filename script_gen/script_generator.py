from llm import LLMClient

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

        Respond with ONLY the script in this format with the text formatted to be input into a text to speech system.
        Put a @ after the title as a special marker:
        "[Edited title here]@
        [Edited story here]"
    """

    result = llm.generate(prompt, temperature=0.8, max_tokens=750)
    return result.strip()