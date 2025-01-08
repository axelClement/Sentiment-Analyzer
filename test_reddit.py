from reddit_config import reddit

# Accéder à un subreddit
subreddit = reddit.subreddit("stocks")

# Récupérer les 5 posts les plus populaires
for post in subreddit.hot(limit=5):
    print(f"Titre : {post.title}")
    print(f"URL : {post.url}")
    print(f"Score : {post.score}")
    print()
