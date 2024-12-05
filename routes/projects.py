
from flask import Blueprint, jsonify, request, render_template
from models import contract, w3
from datetime import datetime
import time
import os
from dotenv import load_dotenv
import logging

load_dotenv()

SEPOLIA_URL = os.getenv("SEPOLIA_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
OWNER_ADDRESS = os.getenv("OWNER_ADDRESS")

projects_bp = Blueprint('projects_bp', __name__)

logging.basicConfig(level=logging.INFO)

@projects_bp.route('/add', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        try:
            data = request.get_json()

            # Vérification des données reçues
            logging.info(f"Données reçues : {data}")

            if 'deadline' not in data:
                return jsonify({"error": "Le champ deadline est requis"}), 400

            try:
                deadline_seconds = int(data['deadline'])
                current_time = int(time.time())
                deadline = current_time + deadline_seconds
            except ValueError:
                return jsonify({"error": "Le champ deadline doit être un nombre entier"}), 400

            if deadline <= current_time:
                return jsonify({"error": "Le champ deadline doit être une date future"}), 400

            logging.info("Estimation du gaz requis pour la transaction...")

            # Estimation dynamique de la limite de gaz
            try:
                gas_estimate = contract.functions.addProject(
                    data['name'], data['description'], deadline
                ).estimate_gas({'from': OWNER_ADDRESS})
                logging.info(f"Estimation du gaz : {gas_estimate}")
            except Exception as e:
                logging.error(f"Erreur lors de l'estimation du gaz : {str(e)}", exc_info=True)
                return jsonify({"error": "Impossible d'estimer le gaz"}), 500

            # Construction de la transaction avec des paramètres ajustés
            transaction = contract.functions.addProject(
                data['name'], data['description'], deadline
            ).build_transaction({
                'from': OWNER_ADDRESS,
                'nonce': w3.eth.get_transaction_count(OWNER_ADDRESS),
                'gas': gas_estimate + 10000,  # Ajout d'une marge de sécurité
                'gasPrice': w3.to_wei('5', 'gwei')  # Réduction du prix du gaz
            })

            logging.info(f"Transaction construite : {transaction}")

            # Signature et envoi de la transaction
            signed_tx = w3.eth.account.sign_transaction(transaction, PRIVATE_KEY)
            logging.info(f"signed_tx contenu : {signed_tx}")

            tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
            receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

            logging.info(f"Transaction envoyée avec succès : {tx_hash.hex()}")

            return jsonify({"message": "Projet ajouté avec succès", "tx_hash": tx_hash.hex()}), 201

        except Exception as e:
            logging.error(f"Erreur lors du traitement : {str(e)}", exc_info=True)
            return jsonify({"error": f"Erreur interne : {str(e)}"}), 500

    return render_template('add_project.html')


@projects_bp.route('/list', methods=['GET'])
def list_projects():
    next_project_id = contract.functions.nextProjectId().call()
    projects = []
    for i in range(next_project_id):
        project = contract.functions.projects(i).call()
        projects.append({
            "id": project[0],
            "name": project[1],
            "description": project[2],
            "totalTokensSold": project[3],
            "votes": project[4],
            "isActive": project[5],
            "deadline": datetime.utcfromtimestamp(project[6]).strftime('%Y-%m-%d %H:%M:%S')  # Format lisible
        })
    return render_template('projects_list.html', projects=projects)

