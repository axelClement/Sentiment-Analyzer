import pandas as pd
import matplotlib.pyplot as plt

def visualize_sentiments(input_file):
    """
    Visualise les tendances des sentiments sur une période donnée.
    """
    # Charger les données
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {input_file} est introuvable.")
        return

    # Compter les sentiments par date
    sentiment_counts = data.groupby(["Date", "Sentiment"]).size().unstack(fill_value=0)

    # Créer le graphique
    sentiment_counts.plot(kind="bar", stacked=True, figsize=(12, 6))
    plt.title("Tendances des sentiments sur Reddit")
    plt.xlabel("Date")
    plt.ylabel("Nombre de posts")
    plt.xticks(rotation=45)
    plt.legend(title="Sentiment")
    plt.tight_layout()
    plt.show()

# Tester la fonction
if __name__ == "__main__":
    input_file = "data/sentiment_analysis_results.csv"
    visualize_sentiments(input_file)
