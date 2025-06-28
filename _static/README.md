# Systeme de Gestion  de bibliothèque

## Réalisé par :
Ouissal Khfifi
Ensao - Génie Informatique GI3 - 2024/2025

## Description du projet:
Ce projet est une application Python complète permettent  de gérer une bibliotheque .
Il a été réalisé dans le cadre du module "Progmmation Avancée en Python".

### Fonctions principales:
-> Ajouter / Supprimer des **livres**
-> Enregistrer / Gérer des **membres**
-> Gérer les **emprunts** et les **retours**
-> Générer des **statistiques visuelles** avec Matplotlib 
-> Persistance des données avec des fichiers '.txt' /'.csv'
-> Interface graphique cinviviale avec **CustomTkinter**

## Technologies utilisées :
-> Python 3
-> Customtkinter
-> Matplotlib
-> Fichiers texte, Json, CSV

## Structure du projet :
bibliotheque_python_khfifi_ouissal/
├── assets/
│   ├── presentations.mp4
│   ├── stats_genres.png
│   ├── stats_auteurs.png
│   └── stats_emprunts.png
├── data/
│   ├── livres.txt
│   ├── membres.txt
│   └── historique.csv
├── docs/
│   └── rapport.pdf
├── src/
│   ├── bibliotheque.py
│   ├── livre.py
│   ├── membre.py
│   ├── gui.py
│   ├── main.py
│   └── visualisations.py
├── README.md
└── requirements.txt
## Installation :
1. Cloner le projet :
'''bash
git clone https://github.com/ton-utlisateur/nom-du ropo.git
cd nom-du repo
2. Installaer les dépendances:
pip install -r requiremets.txt
## Lancer l'application :
python src/gui.py
## Statisques générées:
*Diagramme cieculaire:%de livres par genre
*Histogramme :Top 10 auteurs
*Courbe : activité d'emprunt sur 30 jours
captures générées automatiquements et visibles dans le dossier "assets".
## Video de démonstation:
Fichier "presentations.mp4 situé dans le dossier "assets/".
## Rapport:
Fichier " rapport.pdf " situé dans le dossier "docs/"
## Auteur:
Projet individuel réalisé pour le module **Programmation Avancée en Python**
Université Mohammed Premier - Ensao -GI3

## Date limite:
28 juin 2025