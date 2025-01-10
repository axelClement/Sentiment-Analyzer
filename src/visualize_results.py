import pandas as pd
import matplotlib.pyplot as plt

def visualize_combined_sentiment(input_file):
    """
    Visualise les tendances des sentiments combinés sous forme d'une seule courbe.
    """
    # Charger les données
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {input_file} est introuvable.")
        return

    # Attribuer des scores aux sentiments
    sentiment_scores = {"Positif": 1, "Neutre": 0, "Négatif": -1}
    data["Sentiment_Score"] = data["Sentiment"].map(sentiment_scores)

    # Calculer la somme des scores par date
    combined_sentiment = data.groupby("Date")["Sentiment_Score"].sum()

    # Tracer la courbe
    plt.figure(figsize=(12, 6))
    plt.plot(combined_sentiment.index, combined_sentiment.values, marker='o', linestyle='-', label="Score de sentiment combiné")

    # Ajouter des titres et des légendes
    plt.title("Tendances combinées des sentiments sur Reddit")
    plt.xlabel("Date")
    plt.ylabel("Score de sentiment")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Tester la fonction
if __name__ == "__main__":
    input_file = "data/sentiment_analysis_results.csv"
    visualize_combined_sentiment(input_file)
