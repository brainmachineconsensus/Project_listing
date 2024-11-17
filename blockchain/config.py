# config.py
from web3 import Web3
import os
from dotenv import load_dotenv

# Charger les variables depuis un fichier .env
load_dotenv()
# Connexion au réseau Sepolia
SEPOLIA_URL = os.getenv("SEPOLIA_URL")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
OWNER_ADDRESS = os.getenv("OWNER_ADDRESS")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
CRYPTOCOMPARE_API_KEY = os.getenv("CRYPTOCOMPARE_API_KEY")

# Vérifiez si SEPOLIA_URL est bien chargé
if not SEPOLIA_URL:
    raise ValueError("La variable SEPOLIA_URL n'est pas définie dans le fichier .env")

w3 = Web3(Web3.HTTPProvider(SEPOLIA_URL))
# Vérification de la connexion à la blockchain
if not w3.is_connected():
    raise Exception("Connexion au réseau Sepolia échouée.")
print("Connecté à Sepolia :", w3.is_connected())



