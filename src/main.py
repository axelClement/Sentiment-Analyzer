from reddit_scraper import scrape_reddit
from sentiment_analyzer import analyze_sentiment
from visualize_results import visualize_combined_sentiment

# Liste des subreddits à analyser
subreddits_to_scrape = ["stocks", "investing", "wallstreetbets", "finance", "cryptocurrency"]

# Étape 1 : Scraper les données de Reddit
input_file = "data/reddit_sp500_posts.csv"
print("Étape 1 : Scraping des données...")
scrape_reddit(output_file=input_file, post_limit=1000, subreddits=subreddits_to_scrape)

# Étape 2 : Analyser les sentiments
output_file = "data/sentiment_analysis_results.csv"
print("Étape 2 : Analyse des sentiments...")
analyze_sentiment(input_file, output_file)

# Étape 3 : Visualiser les résultats
print("Étape 3 : Visualisation des résultats...")
visualize_combined_sentiment(output_file)
