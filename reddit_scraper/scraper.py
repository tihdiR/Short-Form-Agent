# reddit_scraper/scraper.py

import praw
import os

def fetch_stories(limit=5):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
    )

    subreddit = reddit.subreddit("AskReddit")
    posts = subreddit.hot(limit=limit)

    stories = []
    for post in posts:
        stories.append({
            "title": post.title,
            "text": post.selftext,
        })

    return stories