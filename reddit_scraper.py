import csv
from reddit_config import reddit
from generate_keywords import get_sp500_companies  # Importer la fonction de récupération des entreprises

# Générer le dictionnaire des entreprises du S&P 500
sp500_companies = get_sp500_companies()
keywords = list(sp500_companies.keys())  # Les mots-clés sont les symboles des entreprises

# Ajouter des mots-clés généraux
general_keywords = [
    "S&P 500", "500", "Standard and Poor's", "standard", "US", "stock market", "market crash", "market rally",
    "investing", "trading", "bull market", "bear market", "earnings report"
]
keywords.extend(general_keywords)

# Fonction de nettoyage des textes
def clean_text(text):
    """
    Nettoie les textes pour éviter les problèmes avec les caractères spéciaux.
    """
    text = text.replace('"', "'")
    text = text.replace("\n", " ").replace("\r", " ")
    return text.strip()

# Accès au subreddit
subreddit = reddit.subreddit("stocks")

# Ouvrir le fichier CSV pour enregistrer les résultats
with open("reddit_sp500_posts.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["ID", "Titre", "Score", "Mots-clés", "Commentaires"])  # En-têtes du CSV

    posts_found = 0

    for post in subreddit.new(limit=100):  # Parcourir les 100 posts les plus récents
        # Filtrer par mots-clés
        matched_keywords = [kw for kw in keywords if kw in post.title]
        if matched_keywords:
            posts_found += 1
            title = clean_text(post.title)

            # Charger et nettoyer les commentaires associés au post
            post.comments.replace_more(limit=0)
            comments = [clean_text(comment.body) for comment in post.comments.list()]
            comments_text = " | ".join(comments[:5])  # Prendre les 5 premiers commentaires

            # Sauvegarder dans le fichier CSV
            writer.writerow([post.id, title, post.score, ", ".join(matched_keywords), comments_text])
            # print(f"Écrit dans le CSV : {title} - Mots-clés : {matched_keywords}")

    if posts_found == 0:
        print("Aucun post correspondant aux mots-clés n'a été trouvé.")
    else:
        print(f"{posts_found} posts ont été écrits dans le fichier CSV.")
