import praw
from praw.models import MoreComments
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

posts = subreddit.top(time_filter="month")
# Scraping the top posts of the current month

posts_dict = {"Title": [], "Post Text": [],
			"ID": [], "Score": [],
			"Total Comments": [], "Post URL": []
			}

for post in posts:
	# Title of each post
	posts_dict["Title"].append(post.title)
	
	# Text inside a post
	posts_dict["Post Text"].append(post.selftext)
	
	# Unique ID of each post
	posts_dict["ID"].append(post.id)
	
	# The score of a post
	posts_dict["Score"].append(post.score)
	
	# Total number of comments inside the post
	posts_dict["Total Comments"].append(post.num_comments)
	
	# URL of each post
	posts_dict["Post URL"].append(post.url)

# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
top_posts


# Get Posts
postUrl = "https://www.reddit.com/r/CollegeBasketball/comments/10p7u9m/ap_poll_week_13/"
 
# Creating a submission object
submission = reddit_read_only.submission(url=postUrl)

post_comments = []
 
for comment in submission.comments:
    if type(comment) == MoreComments:
        continue
 
    post_comments.append(comment.body)
 
# creating a dataframe
comments_df = pd.DataFrame(post_comments, columns=['comment'])
comments_df

