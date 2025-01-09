import requests
import csv
from io import StringIO

# Télécharger la liste des entreprises du S&P 500
def get_sp500_companies():
    """
    Récupère la liste des entreprises du S&P 500 depuis le nouveau CSV.
    Retourne un dictionnaire {symbol: security}.
    Filtre les symboles trop courts (moins de 2 caractères).
    """
    url = "https://datahub-next-new.vercel.app/core/s-and-p-500-companies/_r/-/data/constituents.csv"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            csv_data = StringIO(response.text)  # Charger le contenu CSV dans un flux
            reader = csv.DictReader(csv_data)
            companies = {
                row["Symbol"]: row["Security"]
                for row in reader
                if len(row["Symbol"]) > 2  # Filtrer les symboles de 1 caractère
            }
            return companies
        else:
            print(f"Erreur lors de la récupération des données : {response.status_code}")
            return {}
    except Exception as e:
        print(f"Erreur lors de la connexion : {e}")
        return {}


if __name__ == "__main__":
    companies = get_sp500_companies()
    if companies:
        print(f"Nombre d'entreprises récupérées : {len(companies)}")
        for symbol, name in list(companies.items())[:10]:  # Afficher les 10 premières entreprises
            print(f"{symbol}: {name}")
    else:
        print("Aucune donnée récupérée.")
