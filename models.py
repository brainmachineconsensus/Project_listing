
from blockchain import config
import requests
from web3 import Web3
import os
import json
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Récupérer les variables d'environnement
SEPOLIA_URL = os.getenv("SEPOLIA_URL")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
OWNER_ADDRESS = os.getenv("OWNER_ADDRESS")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

# Vérification des variables essentielles
if not SEPOLIA_URL:
    raise ValueError("La variable SEPOLIA_URL est manquante dans le fichier .env")
if not CONTRACT_ADDRESS:
    raise ValueError("La variable CONTRACT_ADDRESS est manquante dans le fichier .env")
if not OWNER_ADDRESS:
    raise ValueError("La variable OWNER_ADDRESS est manquante dans le fichier .env")
if not PRIVATE_KEY:
    raise ValueError("La variable PRIVATE_KEY est manquante dans le fichier .env")

# Connexion au réseau Sepolia
w3 = Web3(Web3.HTTPProvider(SEPOLIA_URL))
if not w3.is_connected():
    raise ConnectionError("Échec de connexion au réseau Sepolia.")
print("Connecté à Sepolia.")

# Charger l'ABI
try:
    with open("build/contracts/ProjectListing.json") as f:
        contract_abi = json.load(f)["abi"]
except (FileNotFoundError, KeyError) as e:
    raise Exception("Erreur lors du chargement de l'ABI : ", e)

# Vérifier et convertir l'adresse du contrat
if not w3.is_address(CONTRACT_ADDRESS):
    raise ValueError("L'adresse du contrat n'est pas valide.")
contract_address = w3.to_checksum_address(CONTRACT_ADDRESS)

# Instance du contrat
contract = w3.eth.contract(address=contract_address, abi=contract_abi)
print("Contrat chargé avec succès.")

# Récupérer les actualités CryptoCompare
def get_crypto_news():
    url = "https://min-api.cryptocompare.com/data/v2/news/"
    headers = {"authorization": f"Apikey {config.CRYPTOCOMPARE_API_KEY}"}
    params = {"lang": "FR"}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json().get("Data", [])
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des actualités : {e}")
        return []

# Exemple d'utilisation
if __name__ == "__main__":
    print(get_crypto_news())
