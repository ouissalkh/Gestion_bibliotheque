class Membre:
    def __init__(self,id,nom,prenom):
        self.id=id
        self.nom=nom
        self.prenom=prenom
        self.livres_empruntes =[]

    def emprunter_livre(self,livre):
        if livre.statut == "disponible":
            self.livres_empruntes.append(livre)
            livre.statut = "emprunte"
            return True
        else:
            return False
    
    def retourner_livre(self,livre):
        if livre in self.livres_empruntes:
            self.livres_empruntes.remove(livre)
            livre.statut = "disponible"
            return True 
        else:
            return False
    def __str__(self):
        titres=[livre.titre for livre in self.livres_empruntes]
        return f"{self.id} - {self.nom} en {self.prenom} - Livres empruntés:{titres}"
    