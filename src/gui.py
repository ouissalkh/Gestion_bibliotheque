import customtkinter as ctk
from tkinter import messagebox
from bibliotheque import Bibliotheque
from livre import Livre
from membre import Membre
from visualisations import afficher_graphes
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
root = ctk.CTk()
root.title("Gestion de bibliothèque")
root.geometry("1000x600")

#color
colors ={
    'sidebar':'#1e3a8a',
    'main_bg':'#f8f9fa',
    'btn_fg': 'white'
}

#Sidebar
sidebar = ctk.CTkFrame(root,width=220,fg_color=colors['sidebar'],corner_radius=0)
sidebar.pack(side="left",fill="y")

#Main content
main_content=ctk.CTkFrame(root, fg_color=colors['main_bg'])
main_content.pack(side="right",fill="both",expand=True)

def afficher_formulaire_ajout_livre():
    for widget in main_content.winfo_children():
        widget.destroy()
    titre=ctk.CTkLabel(main_content,text="Ajouter livre",font=("Segoe UI",28,"bold"),text_color=colors['sidebar'])
    titre.pack(pady=(30,20))

    form_frame = ctk.CTkFrame(main_content, fg_color="#e9ecef")
    form_frame.pack(padx=40,pady=10,fill='x')

    labels=["ISBN", "Titre" ,"Auteur" ,"Année","Genre"]
    entries={}

    for label_text in labels:
        line_frame=ctk.CTkFrame(form_frame,fg_color="#e9ecef")
        line_frame.pack(pady=8,fill='x')

        label = ctk.CTkLabel(line_frame,text=label_text + " :", font=("Segoe UI",14), text_color="black" , width=100)
        label.pack(side='left')

        entry = ctk.CTkEntry(line_frame, font=("Segoe UI",14))
        entry.pack(side='left', fill='x', expand=True, padx=(10,0))

        entries[label_text] = entry

    message_label = ctk.CTkLabel(main_content, text="", font=("Segoe UI",12))
    message_label.pack(pady=(10,0))

    def valider():
        isbn=entries["ISBN"].get().strip()
        titre_livre=entries["Titre"].get().strip()
        auteur=entries["Auteur"].get().strip()
        annee=entries["Année"].get().strip()
        genre=entries["Genre"].get().strip()

        if not all ([isbn, titre_livre, auteur,annee,genre]):
            message_label.configure(text="Veuillez remplir tous les champs",text_color="red")
            return
        livre = Livre(isbn,titre_livre, auteur,annee,genre)
        biblio.ajouter_livre(livre)
        message_label.configure(text="Livre ajouté avec succès !",text_color="green")

        for entry in entries.values():
            entry.delete(0,'end')

    ctk.CTkButton(main_content, text="Valider", command=valider,
                  fg_color=colors['sidebar'],hover_color="#3b66d1",
                  text_color=colors['btn_fg'], font=("Segoe UI",14)).pack(pady=30)

def ajouter_livre():
    afficher_formulaire_ajout_livre()

def afficher_formulaire_enregistrer_membre():
    for widget in main_content.winfo_children():
        widget.destroy()

    titre = ctk.CTkLabel(main_content, text="Enregister membre" , font=("Segoe UI",28,"bold"),text_color=colors['sidebar'])
    titre.pack(pady=(30,20))

    form_frame = ctk.CTkFrame(main_content, fg_color="#e9ecef")
    form_frame.pack(padx=40, pady=10, fill='x')

    labels = ["ID","Nom","Prenom"]
    entries={}
    
    for label_text in labels:
        line_frame =ctk.CTkFrame(form_frame, fg_color="#e9ecef")
        line_frame.pack(pady=8,fill='x')

        label = ctk.CTkLabel(line_frame, text=label_text + " : " ,font=("Segoe UI",14),text_color="black",width=100)
        label.pack(side='left')

        entry= ctk.CTkEntry(line_frame, font =("Segoe UI",14))
        entry.pack(side='left' , fill='x' ,expand=True, padx=(10,0))

        entries[label_text] = entry
    
    message_label = ctk.CTkLabel(main_content,text="", font=("Segoe UI",12))
    message_label.pack(pady=(10,0))

    def valider():
        id=entries["ID"].get().strip()
        nom=entries["Nom"].get().strip()
        prenom=entries["Prenom"].get().strip()

        if not all([id,nom,prenom]):
            message_label.configure(text="Veuillez remplir tous les champs",text_color="red")
            return
        
        membre= Membre(id,nom,prenom)
        biblio.enregistrer_membre(membre)
        biblio.sauvegarder_data()
        message_label.configure(text="Membre enregistré avec succès !",text_color="green")

        for entry in entries.values():
            entry.delete(0,'end')
    ctk.CTkButton(main_content ,text="Valider" ,command=valider,
                  fg_color=colors['sidebar'],hover_color="#3b66d1",
                  text_color=colors['btn_fg'], font=("Segoe UI", 14)).pack(pady=30)
    

def enregistrer_membre():
    afficher_formulaire_enregistrer_membre()

def emprunter_livre():
    afficher_formulaire_emprunter_livre()

def afficher_formulaire_emprunter_livre():
    #vider la frame main_content
    for widget in main_content.winfo_children():
        widget.destroy()

    #titre
    titre =ctk.CTkLabel(main_content, text="Emprunter un livre",
                        font =ctk.CTkFont(size=28 ,weight="bold"),
                        text_color=colors['sidebar'])
    titre.pack(pady=(30,20))

    form_frame =ctk.CTkFrame(main_content,fg_color="#e9ecef")
    form_frame.pack(padx=40, pady=10, fill='x')

    #champs du formulaire
    labels = ["ID du membre", "ISBN du livre"]
    entries = {}

    for label_text in labels:
        line_frame = ctk.CTkFrame(form_frame, fg_color="#e9ecef")
        line_frame.pack(pady=8,fill='x')

        label = ctk.CTkLabel(line_frame, text=label_text + " :" , font=("Segoe UI",14),text_color="black",width=140)
        label.pack(side='left')

        entry = ctk.CTkEntry(line_frame ,font=("Segoe UI",14))
        entry.pack(side='left', fill='x', expand=True, padx=(10,0))

        entries[label_text] = entry 
    
    message_label = ctk.CTkLabel(main_content,text="", font=("Segoe UI",12))
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
    
    ctk.CTkButton(main_content ,text="Valider", command=valider_emprunt,
                   fg_color=colors['sidebar'],hover_color="#3b66d1",
                   text_color=colors['btn_fg'],font=("Segoe UI" ,14)).pack(pady=30)
    
def retourner_livre():
    afficher_formulaire_retourner_livre()

def afficher_formulaire_retourner_livre():
    #vider la frame main_content
    
    for widget in main_content.winfo_children():
        widget.destroy()

    #titre
    titre =ctk.CTkLabel(main_content, text="Retourner un livre",
                        font =ctk.CTkFont(size=28 ,weight="bold"),
                        text_color=colors['sidebar'])
    titre.pack(pady=(30,20))

    form_frame =ctk.CTkFrame(main_content,fg_color="#e9ecef")
    form_frame.pack(padx=40, pady=10, fill='x')

    #champs du formulaire
    labels = ["ID du membre", "ISBN du livre"]
    entries = {}

    for label_text in labels:
        line_frame = ctk.CTkFrame(form_frame, fg_color="#e9ecef")
        line_frame.pack(pady=8,fill='x')

        label = ctk.CTkLabel(line_frame, text=label_text + " :" , font=("Segoe UI",14),text_color="black",width=140)
        label.pack(side='left')

        entry = ctk.CTkEntry(line_frame ,font=("Segoe UI",14))
        entry.pack(side='left', fill='x', expand=True, padx=(10,0))

        entries[label_text] = entry 
    
    message_label = ctk.CTkLabel(main_content,text="", font=("Segoe UI",12))
    message_label.pack(pady=(10,0))

    def valider_retour():
        id_membre = entries["ID du membre"].get().strip()
        isbn_livre = entries["ISBN du livre"].get().strip()

        if not id_membre or not isbn_livre:
            message_label.configure(text="Veuillez remplir tous les champs",text_color="red")
            return
        try:
            biblio.retourner_livre(id_membre,isbn_livre)
            message_label.configure(text="Livre retourné avec succès !",text_color="green")
            for entry in entries.values():
                entry.delete(0,'end')
        except Exception as e:
            message_label.configure(text=f"Erreur:{str(e)}",text_color="red")
    
    ctk.CTkButton(main_content ,text="Valider", command=valider_retour,
                   fg_color=colors['sidebar'],hover_color="#3b66d1",
                   text_color=colors['btn_fg'],font=("Segoe UI" ,14)).pack(pady=30)
    
def afficher_livre():
    for widget in main_content.winfo_children():
        widget.destroy() 

    #titre
    titre =ctk.CTkLabel(main_content, text="Liste des livres",
                        font =ctk.CTkFont(size=26 ,weight="bold"),
                        text_color=colors['sidebar'])
    titre.pack(pady=(20,10))

    if not biblio.livres:
        no_data_label = ctk.CTkLabel(main_content, text="Auncun livre disponible.", text_color="red", font=ctk.CTkFont(size=16))
        no_data_label.pack()
        return
    columns=("ISBN", "Titre", "Auteur", "Année", "Genre")
    tree_frame = ctk.CTkFrame(main_content, fg_color="white")
    tree_frame.pack(padx=0, pady=10, fill="both", expand=True)

    style = ttk.Style()
    style.theme_use('clam') #Important pour appliqher les couleurs
    style.configure("Treeview",
                    background="#f5f5f5",
                    foreground="black",
                    rowheight=35,
                    font=("Segoe UI" ,13))
    style.configure("Treeview.Heading",
                    font=("Segoe UI",14,"bold"),
                    foreground="white",
                    background="#1e3a8a")
    style.map("Treeview.Heading",
              background=[('active','#3b66d1'),('!active','#1e3a8a')])
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
    
def afficher_membre(biblio):
    for widget in main_content.winfo_children():
        widget.destroy() 

    #titre
    titre =ctk.CTkLabel(main_content, text="Liste des membres",
                        font =ctk.CTkFont(size=28 ,weight="bold"),
                        text_color=colors['sidebar'])
    titre.pack(pady=(30,20))

    if not biblio.membres:
        no_data_label = ctk.CTkLabel(main_content, text="Aucun membre enregistré",
                                     text_color="red",font=ctk.CTkFont(size=16))
        no_data_label.pack()
        return
    
    columns=("ID", "Nom", "Prenom", "Nb Livres empruntés")
    tree_frame = ctk.CTkFrame(main_content, fg_color="white",corner_radius=10)
    tree_frame.pack(padx=40, pady=10, fill="both", expand=True)

    style = ttk.Style()
    style.theme_use('clam') #Important pour appliqher les couleurs
    style.configure("Treeview",
                    background="#f5f5f5",
                    foreground="black",
                    rowheight=35,
                    font=("Segoe UI" ,13))
    style.configure("Treeview.Heading",
                    font=("Segoe UI",14,"bold"),
                    foreground="white",
                    background="#1e3a8a")
    style.map("Treeview.Heading",
              background=[('active','#3b66d1'),('!active','#1e3a8a')])
    tree = ttk.Treeview(tree_frame , columns=columns ,show='headings', height=10)

    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(side="left", fill="both",expand=True)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    for membre in biblio.membres:
        tree.insert("", "end", values=(membre.id, membre.nom, membre.prenom, len(membre.livres_empruntes) if hasattr(membre, 'livres_empruntes')else 0))

def on_clic_statistiques():
    afficher_graphes(main_content)
    

ctk.CTkLabel(sidebar, text="Menu" , font=("Segoe UI",20,"bold"), text_color="white").pack(pady=20)

button_options={
    "fg_color":colors['sidebar'],
    "hover_color":"#3b66d1",
    "text_color":"white",
    "width":200,
    "anchor":"w",
    "font":("Segoe UI Emoji",14)
}

#les bouton
ctk.CTkButton(sidebar, text="📚 Ajouter un livre", command=ajouter_livre, **button_options).pack(pady=5)
ctk.CTkButton(sidebar, text="👤 Enregistrer un membre", command=enregistrer_membre, **button_options).pack(pady=5)
ctk.CTkButton(sidebar, text="📖 Emprunter un livre", command=emprunter_livre, **button_options).pack(pady=5)
ctk.CTkButton(sidebar, text="↩️ Retourner un livre", command=retourner_livre, **button_options).pack(pady=5)
ctk.CTkButton(sidebar, text="📋 Afficher livres", command=afficher_livre, **button_options).pack(pady=5)
ctk.CTkButton(sidebar, text="👥 Afficher membres", command=lambda: afficher_membre(biblio), **button_options).pack(pady=5)
ctk.CTkButton(sidebar, text="📊 Statistiques", command=on_clic_statistiques, **button_options).pack(pady=5)
root.mainloop()