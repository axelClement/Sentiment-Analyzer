import csv
from reddit_config import reddit

# Mots-clés pour filtrer les posts
keywords = ["TSLA", "Tesla", "Meta", "Facebook", "AAPL", "Apple", "AMZN", "Amazon", "GOOGL", "Google", "MSFT", "Microsoft"]

# Fonction de nettoyage des textes
def clean_text(text):
    """
    Nettoie les textes pour éviter les problèmes avec les caractères spéciaux.
    - Remplace les guillemets doubles par des simples.
    - Supprime les retours à la ligne et les caractères invisibles.
    """
    text = text.replace('"', "'")  # Remplace les guillemets doubles par des simples
    text = text.replace("\n", " ").replace("\r", " ")  # Supprime les retours à la ligne
    return text.strip()  # Supprime les espaces superflus en début/fin de texte


# Accès au subreddit
subreddit = reddit.subreddit("stocks")

# Ouvrir le fichier CSV pour enregistrer les résultats
with open("reddit_stocks_posts.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)  # Gestion des guillemets automatiques
    writer.writerow(["ID", "Titre", "Score", "Commentaires"])  # En-têtes du CSV avec ID

    # Compteur pour vérifier les posts trouvés
    posts_found = 0

    # Parcourir les 50 posts les plus récents
    for post in subreddit.new(limit=50):
        if any(keyword in post.title for keyword in keywords):  # Filtrer par mots-clés
            posts_found += 1  # Incrémenter le compteur
            print(f"Titre trouvé : {post.title}")
            print(f"Score : {post.score}")
            print(f"ID : {post.id}")  # Affiche l'ID pour vérification

            # Nettoyer le titre du post
            title = clean_text(post.title)

            # Charger et nettoyer les commentaires associés au post
            post.comments.replace_more(limit=0)  # Charger tous les commentaires
            comments = [clean_text(comment.body) for comment in post.comments.list()]  # Nettoyer les commentaires
            comments_text = " | ".join(comments[:5])  # Combiner les 5 premiers commentaires avec un séparateur

            # Sauvegarder dans le fichier CSV
            writer.writerow([post.id, title, post.score, comments_text])
            print(f"Écrit dans le CSV : {title}")

    # Vérification finale
    if posts_found == 0:
        print("Aucun post correspondant aux mots-clés n'a été trouvé.")
    else:
        print(f"{posts_found} posts ont été écrits dans le fichier CSV.")
