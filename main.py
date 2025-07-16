from reddit_scraper.scraper import fetch_stories

if __name__ == "__main__":
    print("🚀 Starting scraper...")

    stories = fetch_stories(limit=5)

    print(f"Fetched {len(stories)} stories")

    for i, story in enumerate(stories):
        print(f"\n📝 Story #{i+1}")
        print(f"Title: {story['title']}")
        print(f"Text: {story['text'][:300]}...\n")

    print("✅ Done printing stories")