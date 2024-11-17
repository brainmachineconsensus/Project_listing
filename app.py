from flask import Flask, render_template
from routes.projects import projects_bp
from routes.votes import votes_bp
from blockchain.config import w3
from blockchain.contract import contract
from flask_cors import CORS
import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

app = Flask(__name__)
CORS(app)

load_dotenv()
# Récupérer la clé API
CRYPTOCOMPARE_API_KEY = os.getenv("CRYPTOCOMPARE_API_KEY")
# Configuration de l'application
app.config['SEPOLIA_URL'] = os.getenv('SEPOLIA_URL')
app.config['CONTRACT_ADDRESS'] = os.getenv('CONTRACT_ADDRESS')
app.config['OWNER_ADDRESS'] = os.getenv('OWNER_ADDRESS')
app.config['PRIVATE_KEY'] = os.getenv('PRIVATE_KEY')
app.config['CRYPTOCOMPARE_API_KEY'] = os.getenv('CRYPTOCOMPARE_API_KEY')

# Assurez-vous que les variables d'environnement sont correctement chargées
print(f"SEPOLIA_URL: {app.config['SEPOLIA_URL']}")
print(f"CONTRACT_ADDRESS: {app.config['CONTRACT_ADDRESS']}")

# Enregistrement des blueprints avec des préfixes uniques
app.register_blueprint(projects_bp, url_prefix='/projects')
app.register_blueprint(votes_bp, url_prefix='/votes')

# Route d'accueil pour vérifier que l'application fonctionne
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_project', methods=['GET'])
def add_project():
    return render_template('add_project.html')

@app.route("/blockchain-news")
def blockchain_news():
    url = "https://min-api.cryptocompare.com/data/v2/news/"
    headers = {
        "authorization": f"Apikey {CRYPTOCOMPARE_API_KEY}"
    }
    params = {
        "lang": "FR"  # Spécifie la langue française
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        news_data = response.json().get("Data", [])  # Utilise .get() pour éviter les erreurs
    else:
        print(f"Erreur lors de la récupération des actualités: {response.status_code}")
        news_data = []  # Retourne une liste vide en cas d'erreur

    return render_template("blockchain_news.html", news=news_data)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Utilisation du port dynamique fourni par Render
    app.run(debug=True, host="0.0.0.0", port=port)
