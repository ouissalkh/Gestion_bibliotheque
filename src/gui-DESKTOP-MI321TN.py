import customtkinter as ctk
from tkinter import messagebox
from bibliotheque import Bibliotheque
from livre import Livre
from membre import Membre
from visualisations import diag_genres,histogramme_auteurs,courbe_emprunts_30j
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

#initialisation custmotkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

#creation d'une instance de la bibliotheque
biblio=Bibliotheque()
biblio.charger_data()

#fenetre principale
root=ctk.CTK()
root.title("Gestion de bibliothéque")
root.geometry("1000x600")

#color
colors ={
    'sidebafr':'#1e3a8a',
    'main_bg':'#f8f9fa',
    'btn_fg': 'white'
}

#Sidebar
sidebar = ctk.CTKFrame(root,width=220,fg_color=colors['sidebar'],corner_radius=0)
sidebar.pack(side="left",fill="y")

#Main content
main_content=ctk.CTKFrame(root, fg_color=colors['main_bg'])
main_content.pack(side="right",fill="both",expand=True)

def afficher_formulaire_ajout_livre():
    for widget in main_content.winfo_children():
        widget.destroy()
    titre=ctk.CTKLabel(main_content,text="Ajouter livre",font=("Seogoe UI",28,"bold"),text_color=colors['sidebar'])
    titre.pack(pady=(30,20))

    form_fram = ctk.Ctkframe(main_content, fg_color="e9ecef")
    form_fram.pack(padx=40,pady=10,fill='x')

    labels=["ISBN", "Titre" ,"Auteur" ,"Année","Genre"]
    entries={}

    for label_text in labels:
        line_frame=ctk.CTKFrame(form_fram,fg_color="#e9ecef")
        line_frame.pack(pady=8,fill='x')

        label = ctk.CTKLabel(line_frame,text=label_text + " :", font=("Segoe UI",14), text_color="black" , width=100)
        label.pack(side='left')

        entry = ctk.CTKEntry(line_frame, font=("Segoe UI",14))
        entry.pack(side='left', fill='x', expand=True, padx=(10,0))

        entries[label_text] = entry

        message_label = ctk.CTKLabel(main_content, text="", font=("Segoe UI",12))
        message_label.pack(pady=(10,0))

        def valider():
            isbn=entries["ISBN"].get().strip()
            titre_livre=entries["Titre"].get().strip()
            auteur=entries["Auteur"].get().strip()
            annee=entries["Année"].get().strip()
            genre=entries["Genre"].get().strip()

        if not all ([isbn, titre_livre, auteur,annee,genre]):
            message_label.congigure(text="Veuillez remplir tous les champs",text_color="red")
            return
        livre = Livre(isbn,titre_livre, auteur,annee,genre)
        biblio.ajouter_livre(livre)
        message_label.configure(text="Livre ajouté avec succès !",text_color="genre")

        for entry in entries.values():
            entry.delete(0,'end')

    ctk.CTKButton(main_content, text="Valider", command=valider,
                  fg_color=colors['sidebar'],hover_color="#3b66d1",
                  text_color=colors['btn_fg'], font=("Segoe UI",14)).pack(pady=30)

def ajouter_livre():
    afficher_formulaire_ajout_livre()

def afficher_formulaire_enregistrer_membre():
    for widget in main_content.winfo_children():
        widget.destroy()

    titre = ctk.CTKLabel(main_content, text="Enregister membre" , font=("Segoe UI",28,"bold"),text_color=colors['sidebar'])
    titre.pack(pady=(30,20))

    form_frame = ctk.CTKFrame(main_content, fg_color="#e9ecef")
    form_frame.pack(padx=40, pady=10, fill='x')

    labels = ["ID","Nom","Prenom"]
    entries={}
    
    for label_text in labels:
        line_frame =ctk.CTKFrame(form_frame, fg_color="#e9ecef")
        line_frame.pack(pady=8,fill='x')

        label = ctk.CTKLabel(line_frame, font=("Segoe UI",14),text_color="black",width=100)
        label.pack(side='left')

        entry= ctk.CTKEntry(line_frame, font =("Segoe Ui",14))
        entry.pack(side='left' , fill='x' expand=True, padx=(10,0))

        entries[label_text] = entry
    
    message_label = ctk.CTKLabel(main_content,text="", font=("Segoe UI",12))
    message_label.pack(apdy=(10,0))

    def valider():
        id=entries["ID"].get().strip()
        nom=entries["Nom"].get().strip()
        prenom=entries["Prenom"].get().strip()

        if not all([id,nom,prenom]):
            message_label.configure(text="Veuillez remplir tous les champs",text_color="red")
            return
        
        membre= Membre(id,nom,prenom)
        biblio.enregistrer_membre(membre)
        message_label.configure(text="Membre enregistré avec succès !",text_color="green")

        for entry in entries.values():
            entry.delete(0,'end')
    ctk.CTKButton(main_content ,text="Valider" ,command=valider,
                  fg_color=colors['sidebar'],hover_color="#3b66d1",
                  text_color=colors['btn_fg'], font=("Segoe UT", 14)).pack(pady=30)
    

def enregistrer_membre():
    afficher_formulaire_enregistrer_membre()

def emprunter_livre():
    afficher_formulaire_emprunter_livre()
def afficher_formulaire_emprunter_livre():
    #vider la frame main_content
    for widget in main_content.winfo_children():
        widget.destroy()

    #titre
    titre =ctk.CTKLabel(main_content, text="Emprunter un livre",
                        font =ctk.CTKFont(size=28 ,weight="bold"),
                        text_color=colors['sidebar'])
    titre.pack(pady=(30,20))

    form_frame =ctk.CTKFrame(main_content,fg_color="#e9ecef")
    form_frame.pack(padx=40, pady=10, fill='x')

    #champs du formulaire
    labels = ["ID du membre", "ISBN du livre"]
    entries = {}

    for label_text in labels:
        line_frame = ctk.CTKFrame(form_frame, fg_color="#e9ecef")
        line_frame.pack(pady=8,fill='x')

        label = ctk.ctkLabel(linea, text=label_text + " :" , font=("Segoe UI",14),text_color="black",width=140)
        label.pack(side='left')

        entry = ctk.CTKEntry(line_frame ,font=("Segoe UI",14))
        entry.pack(side='left', fill='x', expand=True, padx=(10,0))

        entries[label_text] = entry 
    
    message_label = ctk.CTKLabel(main_content,text="", font=("Segoe UI",12))
    message_label.pack(pady=(10,0))

    def valider_emprunt():
        id_membre = entries["ID du membre"].get().strip()
        isbn_livre = entries["ISBN du livre"].get().strip()

        if not id_membre or not isbn_livre:
            message_label.configure(text="Veuillez remplir tous les champs",text_color="red")
            return
        try:
            biblio.emprunter_livre(id_membre,isbn_livre)
            message_label.configure(text="Livre emprunté avec succès !",text_color="green")
            for entry in entries.values():
                entry.delete(0,'end')
        except Exception as e:
            message_label.configure(text=f"Erreur:{str(e)}",text_color="red")
    
    ctk.CTKbButton(main_content ,text="Valider", command=valider_emprunt,
                   fg_color=colors['sidebar'],hover_color="#3b66d1",
                   text_color=colors['btn_fg'],font=("Segoe UI ,14")).pack(pady=30)
    
def retourner_livre():
    afficher_formulaire_retourner_livre()
def afficher_formulaire_retourner_livre():
    #vider la frame main_content
    #vider la frame main_content
    for widget in main_content.winfo_children():
        widget.destroy()

    #titre
    titre =ctk.CTKLabel(main_content, text="Retourner un livre",
                        font =ctk.CTKFont(size=28 ,weight="bold"),
                        text_color=colors['sidebar'])
    titre.pack(pady=(30,20))

    form_frame =ctk.CTKFrame(main_content,fg_color="#e9ecef")
    form_frame.pack(padx=40, pady=10, fill='x')

    #champs du formulaire
    labels = ["ID du membre", "ISBN du livre"]
    entries = {}

    for label_text in labels:
        line_frame = ctk.CTKFrame(form_frame, fg_color="#e9ecef")
        line_frame.pack(pady=8,fill='x')

        label = ctk.ctkLabel(linea, text=label_text + " :" , font=("Segoe UI",14),text_color="black",width=140)
        label.pack(side='left')

        entry = ctk.CTKEntry(line_frame ,font=("Segoe UI",14))
        entry.pack(side='left', fill='x', expand=True, padx=(10,0))

        entries[label_text] = entry 
    
    message_label = ctk.CTKLabel(main_content,text="", font=("Segoe UI",12))
    message_label.pack(pady=(10,0))

    def valider_retour():
        id_membre = entries["ID du membre"].get().strip()
        isbn_livre = entries["ISBN du livre"].get().strip()

        if not id_membre or not isbn_livre:
            message_label.configure(text="Veuillez remplir tous les champs",text_color="red")
            return
        try:
            biblio.retourner_livre_livre(id_membre,isbn_livre)
            message_label.configure(text="Livre retourné avec succès !",text_color="green")
            for entry in entries.values():
                entry.delete(0,'end')
        except Exception as e:
            message_label.configure(text=f"Erreur:{str(e)}",text_color="red")
    
    ctk.CTKbButton(main_content ,text="Valider", command=valider_retour,
                   fg_color=colors['sidebar'],hover_color="#3b66d1",
                   text_color=colors['btn_fg'],font=("Segoe UI ,14")).pack(pady=30)
    
def afficher_livre():
    for widget in main_content.winfo_children():
        widget.destroy() 

    #titre
    titre =ctk.CTKLabel(main_content, text="Liste des livres",
                        font =ctk.CTKFont(size=26 ,weight="bold"),
                        text_color=colors['sidebar'])
    titre.pack(pady=(20,10))

    if not biblio.livres:
        no_data_label = ctk.CTKLabel(main_content, text="Auncun livre disponible.", text_color="red", font=ctk.CTKFont(size=16))
        no_data_label.pack()
        return
    columns=("ISBN", "Titre", "Auteur", "Année", "Genre")
    tree_frame = ctk.CTKLabel(main_content, fg_color="white")
    tree_frame.pack(padx=0, pady=10, fill="both", expand=True)

    style = ttk.Style()
    style.theme_use('calm') #Important pour appliqher les couleurs
    style.configure("Treeview",
                    background="#f5f5f5",
                    foreground="black",
                    rowheight=35,
                    font=("Segoe Ui ,13"))
    style.configure("Treeview.Heading",
                    font=("Segoe UI",14,"bold"),
                    foreground="white",
                    background="#1e3a8a")
    style.map("Treeview.Heading",
              backgound=[('active','#3b66d1'),('!active','#1e3a8a')])
    tree = ttk.Treeview(tree_frame , columns=columns ,show='headings', height=10)

    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(side="left", fill="both",expand=True)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    for livre in biblio.livres:
        tree.insert("", "end", values=(livre.isbn, livre.titre, livre.auteur, livre.annee, livre.genre))
    
def afficher_membre():
    for widget in main_content.winfo_children():
        widget.destroy() 

    #titre
    titre =ctk.CTKLabel(main_content, text="Liste des membres",
                        font =ctk.CTKFont(size=28 ,weight="bold"),
                        text_color=colors['sidebar'])
    titre.pack(pady=(30,20))

    columns=("ID", "Nom", "Prenom", "Nb Livres empruntés")
    tree_frame = ctk.CTKLabel(main_content, fg_color="white",corner_raduis=10)
    tree_frame.pack(padx=40, pady=10, fill="both", expand=True)

    style = ttk.Style()
    style.theme_use('calm') #Important pour appliqher les couleurs
    style.configure("Treeview",
                    background="#f5f5f5",
                    foreground="black",
                    rowheight=35,
                    font=("Segoe Ui ,13"))
    style.configure("Treeview.Heading",
                    font=("Segoe UI",14,"bold"),
                    foreground="white",
                    background="#1e3a8a")
    style.map("Treeview.Heading",
              backgound=[('active','#3b66d1'),('!active','#1e3a8a')])
    tree = ttk.Treeview(tree_frame , columns=columns ,show='headings', height=10)

    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(side="left", fill="both",expand=True)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    for livre in biblio.membres:
        tree.insert("", "end", values=(membre.id, membre.nom, membre.prenom, len(membre.livres_empruntes) if hasattr(membre, 'livre_empruntes')else 0))

    
def afficher_statistique():
    for widget in main_content.winfo_children():
        widget.destroy() 

    #titre
    titre =ctk.CTKLabel(main_content, text="Statistiques de la bibliothèque",
                        font =ctk.CTKFont(size=28 ,weight="bold"),
                        text_color=colors['sidebar'])
    titre.pack(pady=(20,20))

    #conteneur des graphes 
    graph_container = ctk.ctkFrame(main_content ,fg_color="#ffffff",corner_radius=15)
    graph_container.pack(fill='both', expand=True, padx=30 , pady=10)

    #creation figire matplotlib
    fig , axs= plt.subplots(3,1,figsize=(8,10))
    fig.patch.set_facecolor('#ffffff')

    data_genres = [10,5,7]
'''import customtkinter as ctk
from tkinter import messagebox
from bibliotheque import Bibliotheque
from livre import Livre
from membre import Membre
from visualisations import diag_genres, histogramme_auteurs, courbe_emprunts_30j
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

# Initialiser customtkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Créer l'instance de la bibliothèque
biblio = Bibliotheque()
biblio.charger_data()

# Fenêtre principale
root = ctk.CTk()
root.title("Gestion de bibliothèque")
root.geometry("1000x600")

# Couleurs
colors = {
    'sidebar': '#1e3a8a',
    'main_bg': '#f8f9fa',
    'btn_fg': 'white'
}

# Sidebar
sidebar = ctk.CTkFrame(root, width=220, fg_color=colors['sidebar'], corner_radius=0)
sidebar.pack(side="left", fill="y")

# Main content
main_content = ctk.CTkFrame(root, fg_color=colors['main_bg'])
main_content.pack(side="right", fill="both", expand=True)

def afficher_formulaire_ajout_livre():
    for widget in main_content.winfo_children():
        widget.destroy()

    titre = ctk.CTkLabel(main_content, text="Ajouter livre", font=("Segoe UI", 28, "bold"), text_color=colors['sidebar'])
    titre.pack(pady=(30, 20))

    form_frame = ctk.CTkFrame(main_content, fg_color="#e9ecef")
    form_frame.pack(padx=40, pady=10, fill='x')

    labels = ["ISBN", "Titre", "Auteur", "Année", "Genre"]
    entries = {}

    for label_text in labels:
        line_frame = ctk.CTkFrame(form_frame, fg_color="#e9ecef")
        line_frame.pack(pady=8, fill='x')

        label = ctk.CTkLabel(line_frame, text=label_text + " :", font=("Segoe UI", 14), text_color="black", width=100)
        label.pack(side='left')

        entry = ctk.CTkEntry(line_frame, font=("Segoe UI", 14))
        entry.pack(side='left', fill='x', expand=True, padx=(10,0))

        entries[label_text] = entry

    message_label = ctk.CTkLabel(main_content, text="", font=("Segoe UI", 12))
    message_label.pack(pady=(10, 0))

    def valider():
        isbn = entries["ISBN"].get().strip()
        titre_livre = entries["Titre"].get().strip()
        auteur = entries["Auteur"].get().strip()
        annee = entries["Année"].get().strip()
        genre = entries["Genre"].get().strip()

        if not all([isbn, titre_livre, auteur, annee, genre]):
            message_label.configure(text="Veuillez remplir tous les champs", text_color="red")
            return

        livre = Livre(isbn, titre_livre, auteur, annee, genre)
        biblio.ajouter_livre(livre)
        message_label.configure(text="Livre ajouté avec succès !", text_color="green")

        for entry in entries.values():
            entry.delete(0, 'end')

    ctk.CTkButton(main_content, text="Valider", command=valider,
                  fg_color=colors['sidebar'], hover_color="#3b66d1",
                  text_color=colors['btn_fg'], font=("Segoe UI", 14)).pack(pady=30)

def ajouter_livre():
    afficher_formulaire_ajout_livre()

def enregistrer_membre():
    afficher_formulaire_enregistrer_membre()

def afficher_formulaire_enregistrer_membre():
    for widget in main_content.winfo_children():
        widget.destroy()

    titre = ctk.CTkLabel(main_content, text="Enregistrer membre", font=("Segoe UI", 28, "bold"), text_color=colors['sidebar'])
    titre.pack(pady=(30, 20))

    form_frame = ctk.CTkFrame(main_content, fg_color="#e9ecef")
    form_frame.pack(padx=40, pady=10, fill='x')

    labels = ["ID", "Nom", "Prenom"]
    entries = {}

    for label_text in labels:
        line_frame = ctk.CTkFrame(form_frame, fg_color="#e9ecef")
        line_frame.pack(pady=8, fill='x')

        label = ctk.CTkLabel(line_frame, text=label_text + " :", font=("Segoe UI", 14), text_color="black", width=100)
        label.pack(side='left')

        entry = ctk.CTkEntry(line_frame, font=("Segoe UI", 14))
        entry.pack(side='left', fill='x', expand=True, padx=(10,0))

        entries[label_text] = entry

    message_label = ctk.CTkLabel(main_content, text="", font=("Segoe UI", 12))
    message_label.pack(pady=(10, 0))

    def valider():
        id = entries["ID"].get().strip()
        nom = entries["Nom"].get().strip()
        prenom = entries["Prenom"].get().strip()

        if not all([id, nom, prenom]):
            message_label.configure(text="Veuillez remplir tous les champs", text_color="red")
            return

        membre = Membre(id, nom, prenom)
        biblio.enregistrer_membre(membre)
        message_label.configure(text="Membre enregistré avec succès !", text_color="green")

        for entry in entries.values():
            entry.delete(0, 'end')

    ctk.CTkButton(main_content, text="Valider", command=valider,
                  fg_color=colors['sidebar'], hover_color="#3b66d1",
                  text_color=colors['btn_fg'], font=("Segoe UI", 14)).pack(pady=30)

def emprunter_livre():
    afficher_formulaire_emprunter_livre()
def afficher_formulaire_emprunter_livre():
    # Vider la frame main_content
    for widget in main_content.winfo_children():
        widget.destroy()

    # Titre
    titre = ctk.CTkLabel(main_content, text="Emprunter un livre", 
                         font=ctk.CTkFont(size=28, weight="bold"), 
                         text_color=colors['sidebar'])
    titre.pack(pady=(30, 20))

    form_frame = ctk.CTkFrame(main_content, fg_color="#e9ecef")
    form_frame.pack(padx=40, pady=10, fill='x')

    # Champs du formulaire
    labels = ["ID du membre", "ISBN du livre"]
    entries = {}

    for label_text in labels:
        line_frame = ctk.CTkFrame(form_frame, fg_color="#e9ecef")
        line_frame.pack(pady=8, fill='x')

        label = ctk.CTkLabel(line_frame, text=label_text + " :", font=("Segoe UI", 14), text_color="black", width=140)
        label.pack(side='left')

        entry = ctk.CTkEntry(line_frame, font=("Segoe UI", 14))
        entry.pack(side='left', fill='x', expand=True, padx=(10, 0))

        entries[label_text] = entry

    message_label = ctk.CTkLabel(main_content, text="", font=("Segoe UI", 12))
    message_label.pack(pady=(10, 0))

    def valider_emprunt():
        id_membre = entries["ID du membre"].get().strip()
        isbn_livre = entries["ISBN du livre"].get().strip()

        if not id_membre or not isbn_livre:
            message_label.configure(text="Veuillez remplir tous les champs", text_color="red")
            return

        try:
            biblio.emprunter_livre(id_membre, isbn_livre)
            message_label.configure(text="Livre emprunté avec succès !", text_color="green")
            for entry in entries.values():
                entry.delete(0, 'end')
        except Exception as e:
            message_label.configure(text=f"Erreur : {str(e)}", text_color="red")

    ctk.CTkButton(main_content, text="Valider", command=valider_emprunt,
                  fg_color=colors['sidebar'], hover_color="#3b66d1",
                  text_color=colors['btn_fg'], font=("Segoe UI", 14)).pack(pady=30)

def retourner_livre():
    afficher_formulaire_retourner_livre()

def afficher_formulaire_retourner_livre():
    # Vider la frame main_content
    for widget in main_content.winfo_children():
        widget.destroy()

    # Titre
    titre = ctk.CTkLabel(main_content, text="Retourner un livre", 
                         font=ctk.CTkFont(size=28, weight="bold"), 
                         text_color=colors['sidebar'])
    titre.pack(pady=(30, 20))

    form_frame = ctk.CTkFrame(main_content, fg_color="#e9ecef")
    form_frame.pack(padx=40, pady=10, fill='x')

    # Champs du formulaire
    labels = ["ID du membre", "ISBN du livre"]
    entries = {}

    for label_text in labels:
        line_frame = ctk.CTkFrame(form_frame, fg_color="#e9ecef")
        line_frame.pack(pady=8, fill='x')

        label = ctk.CTkLabel(line_frame, text=label_text + " :", font=("Segoe UI", 14), text_color="black", width=140)
        label.pack(side='left')

        entry = ctk.CTkEntry(line_frame, font=("Segoe UI", 14))
        entry.pack(side='left', fill='x', expand=True, padx=(10, 0))

        entries[label_text] = entry

    message_label = ctk.CTkLabel(main_content, text="", font=("Segoe UI", 12))
    message_label.pack(pady=(10, 0))

    def valider_retour():
        id_membre = entries["ID du membre"].get().strip()
        isbn_livre = entries["ISBN du livre"].get().strip()

        if not id_membre or not isbn_livre:
            message_label.configure(text="Veuillez remplir tous les champs", text_color="red")
            return

        try:
            biblio.retourner_livre(id_membre, isbn_livre)
            message_label.configure(text="Livre retourné avec succès !", text_color="green")
            for entry in entries.values():
                entry.delete(0, 'end')
        except Exception as e:
            message_label.configure(text=f"Erreur : {str(e)}", text_color="red")

    ctk.CTkButton(main_content, text="Valider", command=valider_retour,
                  fg_color=colors['sidebar'], hover_color="#3b66d1",
                  text_color=colors['btn_fg'], font=("Segoe UI", 14)).pack(pady=30)


def afficher_livre():
    for widget in main_content.winfo_children():
        widget.destroy()

    titre = ctk.CTkLabel(main_content, text="Liste des Livres", font=ctk.CTkFont(size=26, weight="bold"), text_color=colors['sidebar'])
    titre.pack(pady=(20, 10))

    if not biblio.livres:
        no_data_label = ctk.CTkLabel(main_content, text="Aucun livre disponible.", text_color="red", font=ctk.CTkFont(size=16))
        no_data_label.pack()
        return

    columns = ("ISBN", "Titre", "Auteur", "Année", "Genre")
    tree_frame = ctk.CTkFrame(main_content, fg_color="white")
    tree_frame.pack(padx=20, pady=10, fill="both", expand=True)

    style = ttk.Style()
    style.theme_use('clam')  # Important pour appliquer les couleurs
    style.configure("Treeview",
                    background="#f5f5f5",
                    foreground="black",
                    rowheight=35,
                    font=("Segoe UI", 13))
    style.configure("Treeview.Heading",
                    font=("Segoe UI", 14, "bold"),
                    foreground="white",
                    background="#1e3a8a")
    style.map("Treeview.Heading",
              background=[('active', '#3b66d1'), ('!active', '#1e3a8a')])

    tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=10)

    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(side="left", fill="both", expand=True)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    for livre in biblio.livres:
        tree.insert("", "end", values=(livre.isbn, livre.titre, livre.auteur, livre.annee, livre.genre))

def afficher_membre():
    for widget in main_content.winfo_children():
        widget.destroy()

    titre = ctk.CTkLabel(main_content, text="Liste des membres", font=ctk.CTkFont(size=28, weight="bold"))
    titre.pack(pady=(30, 20))

    tree_frame = ctk.CTkFrame(main_content, fg_color="white", corner_radius=10)
    tree_frame.pack(padx=40, pady=10, fill='both', expand=True)

    columns = ("ID", "Nom", "Prénom", "Nb Livres empruntés")

    style = ttk.Style()
    style.theme_use('clam')  # Important pour appliquer les couleurs
    style.configure("Treeview",
                    background="#f5f5f5",
                    foreground="black",
                    rowheight=35,
                    font=("Segoe UI", 13))
    style.configure("Treeview.Heading",
                    font=("Segoe UI", 14, "bold"),
                    foreground="white",
                    background="#1e3a8a")
    style.map("Treeview.Heading",
              background=[('active', '#3b66d1'), ('!active', '#1e3a8a')])

    tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=10)

    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(side="left", fill="both", expand=True)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    for membre in biblio.membres:
        tree.insert('', 'end', values=(
            membre.id,
            membre.nom,
            membre.prenom,
            len(membre.livres_empruntes) if hasattr(membre, 'livres_empruntes') else 0
        ))

def afficher_statistique():
    # Vider la frame main_content avant d'afficher les stats
    for widget in main_content.winfo_children():
        widget.destroy()

    # Titre de la page
    titre = ctk.CTkLabel(main_content, text="Statistiques de la bibliothèque", 
                         font=ctk.CTkFont(size=28, weight="bold"), 
                         text_color=colors['sidebar'])
    titre.pack(pady=(20, 20))

    # Conteneur des graphiques avec un padding interne
    graph_container = ctk.CTkFrame(main_content, fg_color="#ffffff", corner_radius=15)
    graph_container.pack(fill='both', expand=True, padx=30, pady=10)

    # Création figure matplotlib
    fig, axs = plt.subplots(3, 1, figsize=(8, 10))
    fig.patch.set_facecolor('#ffffff')  # Fond blanc pour bien intégrer

    # 1) Diagramme circulaire des genres
    data_genres = [10, 5, 7]
    labels_genres = ["Roman", "Science", "Histoire"]
    colors_genres = ['#4a90e2', '#50e3c2', '#f5a623']
    axs[0].pie(data_genres, labels=labels_genres, autopct='%1.1f%%', startangle=90, colors=colors_genres)
    axs[0].set_title("Répartition des Genres", fontsize=16, fontweight='bold', color=colors['sidebar'])
    axs[0].axis('equal')  # Cercle parfait

    # 2) Histogramme des auteurs
    auteurs = ["Auteur A", "Auteur B", "Auteur C"]
    emprunts = [4, 7, 5]
    axs[1].bar(auteurs, emprunts, color='#3b66d1', edgecolor='black')
    axs[1].set_title("Emprunts par Auteur", fontsize=16, fontweight='bold', color=colors['sidebar'])
    axs[1].set_ylabel("Nombre d'emprunts")
    axs[1].grid(axis='y', linestyle='--', alpha=0.6)

    # 3) Courbe des emprunts sur 30 jours
    jours = list(range(1, 31))
    emprunts_30j = [i*0.5 for i in jours]
    axs[2].plot(jours, emprunts_30j, color='#50e3c2', linewidth=3, marker='o')
    axs[2].set_title("Emprunts sur 30 jours", fontsize=16, fontweight='bold', color=colors['sidebar'])
    axs[2].set_xlabel("Jour")
    axs[2].set_ylabel("Nombre d'emprunts")
    axs[2].grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout(pad=3)

    # Intégrer la figure matplotlib dans la frame customtkinter
    canvas = FigureCanvasTkAgg(fig, master=graph_container)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True, padx=10, pady=10)

# Titre Sidebar
ctk.CTkLabel(sidebar, text="Menu", font=("Segoe UI", 20, "bold"), text_color="white").pack(pady=20)

button_options = {
    "fg_color": colors['sidebar'],
    "hover_color": "#3b66d1",
    "text_color": "white",
    "width": 200,
    "anchor": "w",
    "font": ("Segoe UI Emoji", 14)
}

ctk.CTkButton(sidebar, text="📚  Ajouter un livre", command=ajouter_livre, **button_options).pack(pady=5)
ctk.CTkButton(sidebar, text="👤  Enregistrer un membre", command=enregistrer_membre, **button_options).pack(pady=5)
ctk.CTkButton(sidebar, text="📖  Emprunter un livre", command=emprunter_livre, **button_options).pack(pady=5)
ctk.CTkButton(sidebar, text="↩️  Retourner un livre", command=retourner_livre, **button_options).pack(pady=5)
ctk.CTkButton(sidebar, text="📋  Afficher livres", command=afficher_livre, **button_options).pack(pady=5)
ctk.CTkButton(sidebar, text="👥  Afficher membres", command=afficher_membre, **button_options).pack(pady=5)
ctk.CTkButton(sidebar, text="📊  Statistiques", command=afficher_statistique, **button_options).pack(pady=5)

root.mainloop()

biblio.sauvegarder_data()
'''