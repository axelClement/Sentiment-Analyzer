import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialiser l'analyseur de sentiment
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(input_file, output_file):
    """
    Effectue une analyse de sentiment sur les titres et enregistre les résultats dans un nouveau fichier.
    
    :param input_file: Chemin vers le fichier CSV contenant les posts Reddit.
    :param output_file: Chemin vers le fichier CSV où enregistrer les résultats.
    """
    # Charger les données depuis le fichier CSV
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {input_file} est introuvable.")
        return

    # Ajouter une nouvelle colonne pour le score de sentiment
    sentiments = []

    for title in data["Titre"]:
        # Analyse de sentiment pour chaque titre
        sentiment_scores = analyzer.polarity_scores(str(title))
        compound_score = sentiment_scores["compound"]

        # Déterminer le sentiment basé sur le score compound
        if compound_score > 0.05:
            sentiments.append("Positif")
        elif compound_score < -0.05:
            sentiments.append("Négatif")
        else:
            sentiments.append("Neutre")

    # Ajouter la colonne Sentiment aux données
    data["Sentiment"] = sentiments

    # Enregistrer les résultats dans un nouveau fichier CSV
    data.to_csv(output_file, index=False, encoding="utf-8")
    print(f"Analyse de sentiment terminée. Résultats enregistrés dans {output_file}")


# Tester la fonction si ce fichier est exécuté directement
if __name__ == "__main__":
    input_file = "data/reddit_sp500_posts.csv"
    output_file = "data/sentiment_analysis_results.csv"
    analyze_sentiment(input_file, output_file)
