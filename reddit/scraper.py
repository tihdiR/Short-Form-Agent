# reddit_scraper/scraper.py
import os
import praw
from dotenv import load_dotenv

load_dotenv() 

def fetch_stories(limit=5, comments_limit=3):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
    )

    subreddit = reddit.subreddit("TwoHotTakes")
    posts = subreddit.top(time_filter="day", limit=limit)

    stories = []
    for post in posts:
        # Post text (can be empty string)
        post_text = post.selftext.strip()

        # Get top comments if any
        # post.comments.replace_more(limit=0)
        # top_comments = post.comments[:comments_limit]
        # comments_texts = [comment.body for comment in top_comments]

        stories.append({
            "title": post.title,
            "text": post_text,
            # "comments": comments_texts,
        })

    return stories
