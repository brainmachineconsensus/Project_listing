from flask import Flask, render_template
from routes.projects import projects_bp
from routes.votes import votes_bp
from flask_cors import CORS
from blockchain.config import w3
import requests
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuration de l'application
app.config['SEPOLIA_URL'] = os.getenv('SEPOLIA_URL')
app.config['CONTRACT_ADDRESS'] = os.getenv('CONTRACT_ADDRESS')
app.config['OWNER_ADDRESS'] = os.getenv('OWNER_ADDRESS')
app.config['PRIVATE_KEY'] = os.getenv('PRIVATE_KEY')

# Enregistrement des blueprints
app.register_blueprint(projects_bp, url_prefix='/projects')
app.register_blueprint(votes_bp, url_prefix='/votes')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/blockchain-news")
def blockchain_news():
    from models import get_crypto_news
    news_data = get_crypto_news()
    return render_template("blockchain_news.html", news=news_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
