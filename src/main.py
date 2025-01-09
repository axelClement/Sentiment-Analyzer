from reddit_scraper import scrape_reddit
from sentiment_analyzer import analyze_sentiment

# Étape 1 : Scraper les données de Reddit
input_file = "data/reddit_sp500_posts.csv"
scrape_reddit(output_file=input_file, post_limit=100)

# Étape 2 : Analyser les sentiments
output_file = "data/sentiment_analysis_results.csv"
analyze_sentiment(input_file, output_file)
