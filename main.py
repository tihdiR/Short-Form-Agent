from reddit.scraper import fetch_stories
from reddit.reddit_filter import is_story_interesting
from script_gen.script_generator import reddit_to_script


if __name__ == "__main__":
    print("🚀 Starting scraper...")

    stories = fetch_stories(limit=5)

    for i, story in enumerate(stories):
        print(f"\n📝 Story #{i+1}")
        # print(f"Title: {story['title']}")
        # print(f"Text: {story['text'] or '[No post text]'}\n")

        # if story['comments']:
        #     print("Top comments:")
        #     for j, comment in enumerate(story['comments']):
        #         print(f"  {j+1}. {comment}\n")
        # else:
        #     print("No comments available.\n")

        interesting, confidence = is_story_interesting(story['title'], story['text'])#, story['comments'])
        print("interesting: ", interesting)
        print("confidence: ", confidence)
        if interesting:
            print(reddit_to_script(story['title'], story['text']))
        else:
            print("NOT INTERESTING ENOUGH")

    
    