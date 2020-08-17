#imported libraries
import praw
import pandas as pd

reddit = praw.Reddit(client_id='BCIjRj-ycxyYKw', client_secret='H4Y2kZK8ApPhID51VX6R83dHR4M', user_agent='Reddit Webscraper Bit')

posts = []

#gets top 10 posts from Bitcoin subreddit
bitcoin_subreddit = reddit.subreddit('Bitcoin')
for post in bitcoin_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])

# get Bitcoin subreddit description
bitcoin_subreddit = reddit.subreddit('Bitcoin')
description = bitcoin_subreddit.description

#gathers comments for each post into individual csv's
submissions = []
id_list = posts["id"]
for post_id in id_list:
  submissions.append(reddit.submission(id= post_id))

def all_comments(submission):
  post_commments = []
  submission.comments.replace_more(limit=0)
  for comment in submission.comments.list():
      post_commments.append(comment.body)
  post_commments = pd.DataFrame(post_commments, columns = ["comments"])
  return post_commments


for submission in submissions:
  sheet = all_comments(submission)
  sheet.to_csv("subreddit_post_commments.csv")
