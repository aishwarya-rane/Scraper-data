#libraries
pip install praw
or
conda install -c conda-forge praw

import praw
import pandas as pd

reddit = praw.Reddit(client_id='BCIjRj-ycxyYKw', client_secret='H4Y2kZK8ApPhID51VX6R83dHR4M', user_agent='Reddit Webscraper Bit')

posts = []
bitcoin_subreddit = reddit.subreddit('Bitcoin')
for post in bitcoin_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
#print(posts))

# get Bitcoin subreddit data
bitcoin_subreddit = reddit.subreddit('Bitcoin')
#print(bitcoin_subreddit.description)


# individual post
submission = reddit.submission(id="a3p0uq")

submission.comments.replace_more(limit=0)
for top_level_comment in submission.comments:
    print(top_level_comment.body)
