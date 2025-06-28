import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#nombre de livre par genre
def diag_genres(ax):
    genres=[]
    with open("data/livres.txt","r",encoding="utf-8") as f:
        for line in f :
            parts=line.strip().split(";")
            if len(parts)>=5:
                genres.append(parts[4])
    genres_counts=Counter(genres) 
    #utilisation d'un graphe a barre
    ax.pie(genres_counts.values(),labels=genres_counts.keys(), autopct="%1.1f%%",startangle=140)
    ax.set_title("Nombres de livres par genres")
    ax.axis('equal')
   
    
#bar chart horizontal
def histogramme_auteurs(ax):
    auteurs=[]
    with open("data/livres.txt","r",encoding="utf-8") as f :
        for line in f:
            parts=line.strip().split(";")
            if len(parts)>=3:
                auteurs.append(parts[2])
    #compter les occurs des auteurs et recuperer les 10 plus frequenst
    top_auteurs=Counter(auteurs).most_common(10)
    #sparer les noms et leurs nombres pour les utiliser dans l'histogramme
    noms=[a[0]for a in top_auteurs]
    valeurs=[a[1] for a in top_auteurs]
    ax.barh(noms,valeurs,color="skyblue")
    ax.set_xlabel("Nombre de livres")
    ax.set_title("Top 10 des auteurs les plus populaires")
    ax.invert_yaxis()

#Courbe temporelle : Activité des emprunts (30 derniers jours)
import csv
from datetime import datetime,timedelta

def courbe_emprunts_30j(ax):
    #dict pour stocker le nbr d'emprunte par jour
    emprunts_par_jour={}
    #lecutre du fichier historique.csv
    with open("data/historique.csv","r",encoding="utf-8") as f :
        reader=csv.reader(f,delimiter=";") #lire CSV avec ';' comme separete
        for row in reader:
            if len(row)>=4 and row[3].strip().lower()=="emprunt":
                try:
                    #convertir al chaine en date 
                    date_obj=datetime.strptime(row[0],"%Y-%m-%d")
                    #on verifie si cette date est dans les 30 jours
                    if datetime.now() - date_obj<= timedelta(days=30):
                        jour=date_obj.date()#extraire la date sans heure
                        emprunts_par_jour[jour]=emprunts_par_jour.get(jour,0)+1 #incrementer
                except ValueError:
                    continue
#trie des dates
    dates=sorted(emprunts_par_jour.keys())
#extraire les valeurs coreepond
    valeurs=[emprunts_par_jour[d] for d in dates]

    ax.plot(dates,valeurs, marker="o", linestyle="-",color="green")
    ax.set_title("Activité des emprunts - 30 derniers jours")
    ax.set_xlabel("Date")
    ax.set_ylabel("Nombre d'emprunts")
    ax.grid(True)

    
def afficher_graphes(graph_container,enregistrer_images=True):
    for widget in graph_container.winfo_children():
        widget.destroy() 

    #creer une figure avec 3 sous_graphes
    fig,axs = plt.subplots(1,3,figsize=(18,5))

    diag_genres(axs[0])
    histogramme_auteurs(axs[1])
    courbe_emprunts_30j(axs[2])

    plt.tight_layout(pad=3)

    #sauvegarder images
    if enregistrer_images:
        fig.savefig("assets/stats_complet.png")

        for func,filename in [(diag_genres,"assets/stats_genres.png"),
                              (histogramme_auteurs,"assets/stats_auteurs.png"),
                              (courbe_emprunts_30j,"assets/stats_emprunts.png")]:
            fig_tmp,ax_tmp = plt.subplots()
            func(ax_tmp)
            fig_tmp.savefig(filename)
            plt.close(fig_tmp)
    
    canvas=FigureCanvasTkAgg(fig,master=graph_container)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both',expand=True,padx=10,pady=10)

        