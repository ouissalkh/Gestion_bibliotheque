from bibliotheque import Bibliotheque
from livre import Livre
from membre import Membre
from exceptions import livreNonEmprunterError,LivreIntrouvableError,MembreIntrouvableError,LivreNomDisponnibleError
def menu():
    print("Gestion de bibliotheque")
    print("1.ajouter un livre")
    print("2.Enregister un membre")
    print("3.Emprunter un livre")
    print("4.Retourner un livre")
    print("5.Afficher les livres")
    print("6.Afficher les membres")
    print("7.Statistiques")
    print("0.Exit")
def main():
    #creation d'une instance vide
    biblio=Bibliotheque()
    biblio.charger_data()
    #boucle infinie
    while True:
        menu() #pour afficher menu
        choix=input("choisiseez un nombre de 0 a 7:")
        if choix=="1":
            #l'ajout d'un livre
            isbn=input("ISBN:")
            titre=input("Titre:")
            auteur=input("Auteur:")
            annee=input("Annee:")
            genre=input("Genre:")
            #creation d'un objet livre
            livre=Livre(isbn,titre,auteur,annee,genre)
            #l'ajout du livre dans la bibliotheque
            biblio.ajouter_livre(livre)
            print("livre ajouter")
        elif choix == "2":
            #enregistrement d'un membre
            id_membre=input("ID du membre:")
            nom=input("Nom:")
            prenom=input("Prenom:")
            #creation d'un objet membre
            membre=Membre(id_membre,nom,prenom)
            #l'ajout du membre dans la bibliotheque
            biblio.enregistrer_membre(membre)
            print("Membre enregister")
        elif choix == "3":
            #emprunter un livre 
            id_membre = input("ID du membre")
            isbn = input("ISBN du livre:")
            try:
                #essayer d'empruter un livre
                biblio.emprunter_livre(id_membre,isbn)
                print("livre emrunter avec succes")
            except MembreIntrouvableError as e :
                print(f"erreur livre:{e}")
            except LivreIntrouvableError as e :
                print(f"erreur livre:{e}")
            except LivreNomDisponnibleError as e :
                print(f"erreur livre:{e}")
                

        elif choix == "4":
            #retourner un livre
            id_membre=input("ID du membre:")
            isbn=input("ISBN du livre:")
            try:
            #essayer de retourner le livre 

                biblio.retourner_livre(id_membre,isbn)
                print("livrer retourner")
            except MembreIntrouvableError as e :
                print(f"erreur livre:{e}")
            except LivreIntrouvableError as e :
                print(f"erreur livre:{e}")
            except LivreNomDisponnibleError as e :
                print(f"erreur livre:{e}")


        elif choix == "5":
            #afficher la liste des livres
            print("listes des livres:")
            for livre in biblio.livres:
                print("-",livre)
        elif choix=="6":
            #affiche rla liste des membres
            print("listes des membres:")
            for membre in biblio.membres:
                print("-",membre)
        elif choix=="7":
            from visualisations import  diag_genres ,histogramme_auteurs,courbe_emprunts_30j
            diag_genres()
            histogramme_auteurs()
            courbe_emprunts_30j()
        elif choix == "0":
            biblio.sauvegarder_data()
            break
        else:
            print("entrer un nombre de 0 a 7")
if __name__ =="__main__":
    main()