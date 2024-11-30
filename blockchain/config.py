from web3 import Web3
import os
from dotenv import load_dotenv

# Charger les variables depuis .env
load_dotenv()

# Récupérer les variables d'environnement
SEPOLIA_URL = os.getenv("SEPOLIA_URL")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
OWNER_ADDRESS = os.getenv("OWNER_ADDRESS")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
CRYPTOCOMPARE_API_KEY = os.getenv("CRYPTOCOMPARE_API_KEY")

# Vérifiez si l'URL de Sepolia est définie
if not SEPOLIA_URL:
    raise ValueError("La variable SEPOLIA_URL est manquante dans le fichier .env")

# Connexion à Sepolia
w3 = Web3(Web3.HTTPProvider(SEPOLIA_URL))

# Vérifiez la connexion au réseau Sepolia
if not w3.is_connected():
    raise Exception("Échec de connexion au réseau Sepolia.")
print("Connecté à Sepolia :", w3.is_connected())
