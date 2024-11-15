# projects_listing
# Project Listing - Gestion de Projets sur Blockchain

Ce projet est une application web intégrée à un smart contract sur la blockchain pour gérer la liste de projets. Les utilisateurs peuvent ajouter des projets, voter en achetant des tokens, et obtenir des remboursements pour les projets qui ne remplissent pas certaines conditions.

## Fonctionnalités

1. **Ajout de projets** : Les utilisateurs peuvent soumettre de nouveaux projets avec un nom, une description, et une date limite.
2. **Vote pour les projets** : Les utilisateurs votent en achetant des tokens pour les projets qui les intéressent.
3. **Remboursement** : Les projets dont la date limite est atteinte et qui ont reçu moins de 100 votes sont remboursés, et leurs tokens ainsi que leurs votes sont réinitialisés.
4. **Intégration de MetaMask** : Les utilisateurs peuvent se connecter avec MetaMask pour effectuer des transactions sécurisées sur la blockchain.

## Structure du Projet

### Fichiers et Dossiers Principaux

- `app.py` : Point d'entrée de l'application Flask.
- `routes/` : Contient les différentes routes pour les fonctionnalités (ajout de projet, vote, remboursement).
- `static/` : Fichiers statiques comme les images et les fichiers CSS/JavaScript.
- `templates/` : Modèles HTML pour les pages.
- `blockchain/contract.py` : Contient le code pour interagir avec le smart contract via Web3.
- `config.py` : Fichier de configuration (contient des informations comme la clé API CryptoCompare).

### Dépendances

- [Flask](https://flask.palletsprojects.com/) : Framework web pour construire l'interface et les routes.
- [Web3.py](https://web3py.readthedocs.io/) : Bibliothèque pour interagir avec la blockchain.
- [MetaMask](https://metamask.io/) : Extension de navigateur pour la gestion de portefeuille.
- [CryptoCompare](https://min-api.cryptocompare.com/) : API pour obtenir les dernières nouvelles sur la blockchain (clé API nécessaire).

## Installation et Configuration

### Prérequis

1. **Node.js et npm** pour gérer les dépendances front-end.
2. **Python 3** avec `venv` pour créer un environnement virtuel.
3. **MetaMask** pour connecter l'application à un portefeuille blockchain.
4. **Ganache** ou une autre solution pour un réseau local de blockchain pour le développement.

### Étapes d'Installation

1. **Cloner le dépôt** :
   ```bash
   git clone <url_du_dépôt>
   cd project_listing


## Créer un environnement virtuel et installer les dépendances :

'''bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Configurer Ganache :

Ouvrir Ganache et créer un projet avec les paramètres de connexion nécessaires.
Ajouter le réseau local à MetaMask (utiliser le Chain ID 1337).
Configurer config.py :

## Créer un fichier config.py dans le répertoire principal avec :
python

CONTRACT_ADDRESS = 'adresse_du_contrat'
CRYPTOCOMPARE_API_KEY = 'votre_clé_api'
Déployer le Smart Contract :

Compiler et déployer le smart contract sur Ganache via un IDE blockchain comme Remix.
Copier l'adresse du contrat déployé dans config.py.

## Démarrer l'application :
'''bash
python app.py

## Utilisation
Accéder à l'application à l'adresse http://127.0.0.1:5000 dans un navigateur.
Se connecter avec MetaMask pour utiliser les fonctionnalités de l'application.
Naviguer dans les différentes pages pour ajouter des projets, voter, ou demander un remboursement.
Description du Smart Contract
Le smart contract ProjectListing.sol inclut les fonctionnalités suivantes :

addProject : Permet l’ajout d’un nouveau projet avec un nom, une description, et une date limite.
vote : Permet aux utilisateurs d’acheter des tokens pour voter pour un projet spécifique.
refund : Rembourse les projets qui n’ont pas atteint 100 votes avant la date limite. Cette fonction réinitialise également les tokens et votes pour ces projets.
API d'Actualités (CryptoCompare)
L'application récupère les dernières actualités sur la blockchain via l'API CryptoCompare. Pour activer cette fonctionnalité, une clé API doit être ajoutée dans le fichier config.py.

Débogage et Messages d'Erreur
Projets remboursés : Les tokens et votes devraient être réinitialisés après chaque remboursement.
Connexion MetaMask : Vérifier que le réseau local (Ganache) est configuré avec le bon Chain ID (1337).
API CryptoCompare : Assurez-vous que la clé API est correcte et vérifiez le format JSON des réponses.