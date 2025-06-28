class Livre:
    def __init__(self,isbn,titre,auteur, annee, genre, statut="disponible"):
        self.isbn=isbn
        self.titre=titre
        self.auteur=auteur
        self.genre=genre
        self.statut=statut

    def __str__(self):
        return f"{self.titre} est écrit par {self.auteur} en {self.annee}:{self.statut}"
    
    def emprunter(self):
        if self.statut == "disponible":
            self.statut= "emprunte"
            return True
        return False
    
    def retourner_livre(self):
        self.statut = "disponible"