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
            {
                "time": "09:41",
                "severity": "HIGH",
                "source": "SSH",
                "event": "5 tentatives de connexion échouées"
            },
            {
                "time": "09:45",
                "severity": "MEDIUM",
                "source": "VPN",
                "event": "Connexion depuis une IP inconnue"
            },
            {
                "time": "09:47",
                "severity": "INFO",
                "source": "ADMIN",
                "event": "Connexion administrateur réussie"
            }
        ])

    logs = list(collection.find())

    high = collection.count_documents({"severity": "HIGH"})
    medium = collection.count_documents({"severity": "MEDIUM"})
    info = collection.count_documents({"severity": "INFO"})

    return render_template(
    	"index.html",
    	logs=logs,
    	high=high,
    	medium=medium,
    	info=info
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
