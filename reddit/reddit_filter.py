from llm import LLMClient

llm = LLMClient()

def reddit_interest_prompt(title: str, text: str) -> str:#,comments: list[str]) -> str:
    # comments_text = "\n".join(comments) if comments else "[No comments]"
    return f"""
        You are a helpful assistant that evaluates Reddit stories for their potential to be good TikTok/Instagram/Shorts videos.
        You must determine if the provided content is interesting enough to be made into a short video. If a story is provided, evaluate it based on the title, text, and top comments.
        if the story is interesting. If a post has no text, look at the title and commments and evaluate if they are interesting enough to be made into a short video.
        By interesting I mean funny, engaging, or thought-provoking content that would capture viewers' attention. The inital title of the post
        should have a hook in the first sentence that will grab the viewer's attention. A story is not interesting if it doesn't have a good hook or any drama.
        Also avoid sexual stories or other overly vulgar stories. The target audience for the stories should be as general as possible but should appeal to younger people. The content of the 
        posts should be relatively neutral and not offensive to any group of people. Avoid political posts.

        Here are some examples of posts that are interesting:
        
        Story title: "I went to the wrong funeral. I stayed. Now her grandma sends me birthday cards."

        Story text: "I was in a new city. A week in, I got a text from a number I didn't recognize:

            “Hey, service is at 3. Wear something dark, she hated bright colors. I know you didn't know her well, but it would mean a lot if you came.”

            I stared at it. I wasn't sure who it was meant for. But it felt… urgent. Like maybe they really needed someone there. And I had nothing else to do.

            So, I went.

            I pulled up to the church a few minutes early. Sat in the back. No one questioned me. I figured maybe it was a distant coworker or a college friend. I kept waiting for someone to say, “Wait, who are you?” But they didn't.

            The woman who had passed her name was Marion had the kindest smile I've ever seen. I learned about her love for jazz, her cat named Newton, and how she never let anyone leave her house without taking a cookie. I sat through every eulogy like I'd known her forever.

            Afterward, during the gathering, her grandmother approached me.

            “You were her friend from art class, weren't you?” she asked.

            I froze. “No, I think I got the wrong text.”

            She laughed. Actually laughed. “So you're just… here? For a stranger?”

            I nodded. “Didn't want her to have an empty room.”

            She grabbed my hand and said, “Then you're exactly the kind of person she would've liked.”

            We sat together for hours. Talking about Marion. About grief. About weird coincidences. Before I left, her grandma gave me a small velvet pouch.

            “Take this,” she said. “Marion would've insisted you didn't leave empty-handed.”

            Inside was a single sugar cookie, shaped like a heart.

            A year later, her grandmother still sends me a birthday card. Always with a cookie recipe inside. I send her a handwritten thank you every time.

            I don't know why I went that day. But I'm glad I did.

            Sometimes the wrong funeral is exactly where you're meant to be."

        Answer: "YES 0.85"

        Story title: "What is the American equivalent to breaking Spaghetti in front of Italians?"

        Comments: "There was a guy on TikTok visiting from the UK and they went to a Mexican restaurant and poured the salsa over the chips in the basket. That did me in.",
                "Ketchup on your prime rib!",
                "I watched a guy feom NJ roll a NY style pizza from tip to crust and eat it like a burrito. I saw a NY guy watch that, and I saw his soul leave his body that day."

        Answer: "YES 0.75"

        Story title: "My boyfriend used a hidden camera to prove I was “Faking” my period pain"    

        Story text: "I (25F) have PCOS and get brutal, irregular periods. My boyfriend (28M) has always been weird about it. He acts like I'm exaggerating when I can't get out of bed, or when I cancel plans because I'm curled up in pain.

        Last month, he told me he thought I was “being dramatic.” He even said he read online that women “milk it” for attention.

        Cue me being furious.

        But this month? It got worse.

        He confessed,while laughing that he set up a small motion-activated camera in our living room to prove I was “moving around fine” when I said I was too sick to meet his family for dinner.

        When I confronted him, he said he deleted the footage (I don't believe him) and said I was “violating his trust by overreacting.”

        I packed a bag and left that night. Guess who's now single and filing a report."

        Answer: YES 0.95

        
        Story title: "Why do people sneeze?"
        Story text: ""
        Comments: ["It’s biology.", "Dust?", "Google it."]
        Answer: "NO 0.95"

        Story title: "I finally cleaned out my fridge"
        Story text: "Spent all Saturday morning tossing out expired stuff. Found pickles from 2020. Gross."
        Comments: [""Good for you!","That’s adulting for ya", "I did that last week too lol"]
       
        Answer: "NO 0.90"

    
        Based on what I have told you and the examples above, please evaluate the following story:

        Story title:
        {title}

        Story text:
        {text if text else '[No post text]'}

        Question: Based on the above, answer with "YES" if this story would be interesting enough to make a short TikTok video, or "NO" if it wouldn't.
        Only reply with YES or NO and with a confidence score from 0 to 1. The output should look like this: "YES 0.95" or "NO 0.83".
        """

def is_story_interesting(title: str, text: str) -> bool:#, comments: list[str]) -> bool:
    prompt = reddit_interest_prompt(title, text)#, comments)
    response = llm.generate(prompt, temperature=0.7, max_tokens=50)
    parts = response.strip().split()

    if len(parts) != 2:
        print("⚠️ Unexpected format from LLM:", response)
        return False, 0.0

    decision = parts[0].upper()
    try:
        confidence = float(parts[1])
    except ValueError:
        print("⚠️ Could not parse confidence value:", parts[1])
        return False, 0.0

    return decision == "YES", confidence

