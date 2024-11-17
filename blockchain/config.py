# config.py
from web3 import Web3


# Connexion au réseau Sepolia
w3 = Web3(Web3.HTTPProvider(SEPOLIA_URL))

# Vérification de la connexion à la blockchain
if not w3.is_connected():
    raise Exception("Connexion au réseau Sepolia échouée.")
print("Connecté à Sepolia :", w3.is_connected())



