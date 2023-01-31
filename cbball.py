import praw
import pandas as pd

reddit_read_only = praw.Reddit(client_id="p4z_mKkeYGFykkmRw0wvhg",
							client_secret="CK3ERy7reJCKPSpGVxinMXWpIIEamw",
							user_agent="CBBall Stats",
							)

subreddit = reddit_read_only.subreddit("CollegeBasketball")

# Display the name of the Subreddit
print("Display Name:", subreddit.display_name)

# Display the title of the Subreddit
print("Title:", subreddit.title)

# Display the description of the Subreddit
print("Description:", subreddit.description)

for post in subreddit.hot(limit=5):
    print(post.title)
    print()
