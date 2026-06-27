from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connexion à MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client["soc_db"]
collection = db["logs"]


@app.route("/")
def home():

    # Ajouter des données si la collection est vide
    if collection.count_documents({}) == 0:
        collection.insert_many([
            {"event": "Connexion VPN réussie"},
            {"event": "Tentative SSH échouée"},
            {"event": "Utilisateur admin connecté"}
        ])

    logs = list(collection.find())

    return render_template("index.html", logs=logs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
