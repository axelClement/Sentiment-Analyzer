import csv
from datetime import datetime  # Pour convertir les timestamps
from reddit_config import reddit
from generate_keywords import get_sp500_companies

def scrape_reddit(output_file="data/reddit_sp500_posts.csv", post_limit=100):
    """
    Scrape les données du subreddit 'stocks' et les enregistre dans un fichier CSV.

    :param output_file: Chemin vers le fichier CSV où enregistrer les résultats.
    :param post_limit: Nombre de posts à parcourir.
    """
    sp500_companies = get_sp500_companies()
    keywords = list(sp500_companies.keys())  # Les mots-clés sont les symboles des entreprises

    general_keywords = [
        "S&P 500", "500", "Standard and Poor's", "stock market", "market crash",
        "market rally", "investing", "trading", "bull market", "bear market", "earnings report"
    ]
    keywords.extend(general_keywords)

    def clean_text(text):
        text = text.replace('"', "'")
        text = text.replace("\n", " ").replace("\r", " ")
        return text.strip()

    subreddit = reddit.subreddit("stocks")

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["ID", "Titre", "Score", "Date", "Mots-clés", "Commentaires"])  # Ajout de "Date"

        posts_found = 0
        print("Chargement", end="", flush=True)
        for post in subreddit.new(limit=post_limit):
            matched_keywords = [kw for kw in keywords if kw in post.title]
            if matched_keywords:
                posts_found += 1
                title = clean_text(post.title)
                date = datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d')  # Convertir la date
                post.comments.replace_more(limit=0)
                comments = [clean_text(comment.body) for comment in post.comments.list()]
                comments_text = " | ".join(comments[:5])

                writer.writerow([post.id, title, post.score, date, ", ".join(matched_keywords), comments_text])
                print(".", end="", flush=True)

        print(" Terminé!", end="\n")
        if posts_found == 0:
            print("Aucun post correspondant aux mots-clés n'a été trouvé.")
        else:
            print(f"{posts_found} posts ont été écrits dans le fichier CSV.", end="\n")

if __name__ == "__main__":
    scrape_reddit()
