# 🔒 SOCket Dashboard - CyberFactory

## 📖 Présentation

SOCket Dashboard est une application web développée dans le cadre du projet CyberFactory.

L'objectif est de simuler un mini Security Operations Center (SOC) permettant de visualiser des alertes de sécurité stockées dans une base de données MongoDB.

L'application est développée avec Flask et déployée grâce à Docker Compose.

---

## 🏗 Architecture

```
Utilisateur
      │
      ▼
Flask (Dashboard)
      │
      ▼
MongoDB
```

Deux conteneurs Docker sont utilisés :

- Flask : interface web
- MongoDB : stockage des alertes

---

## 🚀 Technologies utilisées

- Python 3.11
- Flask
- MongoDB
- Docker
- Docker Compose
- Git
- GitHub

---

## ▶ Lancer le projet

Cloner le dépôt :

```bash
git clone git@github.com:diakhitee/projet-fil-rouge.git
```

Entrer dans le projet :

```bash
cd projet-fil-rouge
```

Lancer Docker :

```bash
docker compose up --build
```

Puis ouvrir :

```
http://localhost:5000
```

---

## 📊 Fonctionnalités

- Dashboard SOC
- Tableau des alertes
- Statistiques dynamiques
- Communication Flask ↔ MongoDB
- Déploiement Docker Compose

---

## 👥 Auteurs

Projet réalisé dans le cadre de CyberFactory.
