# config.py
from web3 import Web3

from web3 import Web3

# URL RPC de Sepolia
SEPOLIA_URL = "https://rpc.sepolia.org"

# Adresse du contrat sur Sepolia (remplacez par l'adresse obtenue après déploiement)
CONTRACT_ADDRESS = "0x95C2e8f7eE90002CF9834033F7584B6bA3EE46AE"

# Adresse du propriétaire du contrat
OWNER_ADDRESS = "0x0217E58A04AC0BD8E33b53013B21b2F9eeCD2EB9"

# Clé privée pour signer les transactions
PRIVATE_KEY = "77efb44d9e900cf84d8cacaf634a9e010951e62416b1db83d404ffdcd652ebc9"  

# Connexion au réseau Sepolia
w3 = Web3(Web3.HTTPProvider(SEPOLIA_URL))

# Vérification de la connexion à la blockchain
if not w3.is_connected():
    raise Exception("Connexion au réseau Sepolia échouée.")
print("Connecté à Sepolia :", w3.is_connected())



CRYPTOCOMPARE_API_KEY = "162e3b64f2b558673829f4b0899f7964bfafcfe4a212130389afd08150113be7"
