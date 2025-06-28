from livre import Livre
from membre import Membre
from exceptions import LivreIntrouvableError,LivreNomDisponibleError,MembreIntrouvableError,livreNonEmprunterError
import os
class Bibliotheque:
    def __init__(self):
        self.livres=[]
        self.membres=[]
    #la fonction ajouter
    def ajouter_livre(self,livre):
        self.livres.append(livre)

    #la fonction supprimer
    def supprimer_livre(self,isbn):
        livre_a_supprimer=None
        for livre in self.livres:
            if livre.isbn==isbn:
                livre_a_supprimer=livre
        if livre_a_supprimer:
            self.livres.remove(livre_a_supprimer)
            return True
        return False
    def enregistrer_membre(self,membre):
        self.membres.append(membre)

    def emprunter_livre(self,id_membre,isbn):
        membre=next((m for m in self.membres if m.id==id_membre), None)
        if not membre:
            raise MembreIntrouvableError(f"Membre ID '{id_membre}'introuvable")
        #chercher le livre
        livre=next((l for l in self.livres if l.isbn ==isbn), None)
        if not livre:
            raise LivreIntrouvableError(f"Livre ISBN '{isbn}'intouvable")
        if not membre.emprunter_livre(livre):
            raise livreNonEmprunterError(f"le livre '{livre.titre}' est deja emprunte")
        return True
    
    def retourner_livre(self,id_membre,isbn):
        membre=next((m for m in self.membres if m.id==id_membre), None)
        if not membre:
            raise MembreIntrouvableError(f"Membre ID '{id_membre}'introuvable")
        livre=next((l for l in self.livres if l.isbn==isbn), None)
        if not livre:
            raise LivreIntrouvableError(f"Livre ISBN '{isbn}'intouvable")
        if not membre.retourner_livre(livre):
            raise livreNonEmprunterError(f"le livre '{livre.titre}' n'est pas emprunte")
        return True
    
    def sauvegarder_data(self):
        with open("data/livres.txt", "w", encoding="utf-8") as f:
            for livre in self.livres:
                ligne = f"{livre.isbn};{livre.titre};{livre.auteur};{livre.annee};{livre.genre};{livre.statut}\n"
                f.write(ligne)

        with open("data/membres.txt", "w", encoding="utf-8") as f:
            for membre in self.membres:
                livres_ids = ",".join([livre.isbn for livre in membre.livres_empruntes])
                ligne = f"{membre.id};{membre.nom};{membre.prenom};{livres_ids}\n"
                f.write(ligne)

    def charger_data(self):
        self.livres.clear()
        self.membres.clear()
        #charger les livre

        try:
            with open("data/livres.txt","r", encoding="utf-8") as f:
                for ligne in f:
                    parts = ligne.strip().split(";")
                    if len(parts) != 6:
                        print("Ligne livre mal forméé ignorée:", repr(ligne))
                        continue
                    isbn, titre, auteur, annee,genre,statut=parts
                    self.livres.append(Livre(isbn, titre, auteur, annee, genre, statut))
            print(f"{len(self.livres)} livres chargés")
        except FileNotFoundError:
            print("Fichier livre.txt  non trouvé")
        
        #charger les membres
        try:
            with open("data/membres.txt","r",encoding="Utf-8")as f:
                for i , ligne in enumerate(f,1):
                    parts = ligne.strip().split(";")
                    print(f"[ligne {i} split] : {parts}")

                    if len(parts) < 3:
                        print(f"[ligne {i}] ignorée ")
                        continue
                    id_membre, nom ,prenom=parts[0],parts[1],parts[2]
                    livres_str = parts[3] if len(parts) >= 4 else ""

                    print(f"[Ligne {i} données] id={id_membre}, nom={nom}, prenom={prenom},livres={livres_str}")
                    membre =Membre(id_membre,nom,prenom)

                    if livres_str:
                        isbn_empruntes =[isbn.strip() for isbn in livres_str.split(",") if isbn.strip()]
                        for isbn in isbn_empruntes:
                            livre=next((l for l in self.livres if l.isbn == isbn),None)
                            if livre and livre not in membre.livres_empruntes:
                                membre.livres_empruntes.append(livre)
                                livre.statut = "emprunte"
                    self.membres.append(membre)
            print(f"{len(self.membres)} membres chargés")
        except FileNotFoundError:
            print("Fichier membres.txt nom trouvé")

    