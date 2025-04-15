import tkinter as tk
import random as rd
from tkinter import messagebox
import webbrowser
from tkinter import simpledialog

nom_joueur1 = ""
nom_joueur2 = ""
zone_texte_joueur1=""
zone_texte_joueur2=""
grille1=[[None for _ in range(6)] for _ in range(7)]
grille2=[[None for _ in range(6)] for _ in range(7)]
grille3=[[None for _ in range(6)] for _ in range(7)]
grille =[[None for _ in range(6)] for _ in range(7)]
nom1="partie vide"
nom2="partie vide"
nom3="partie vide"

def manuel():
    webbrowser.open_new('https://ludikbazar.com/comment-maitriser-la-strategie-gagnante-du-puissance-4/')

def charger_grille():
    global bouton_grille4,bouton_grille5,bouton_grille6
    bouton_grille4=tk.Button(racine, text=nom1, command=lambda: charger_grille2(1), font=("helvetica", "30"))
    bouton_grille5=tk.Button(racine, text=nom2, command=lambda: charger_grille2(2), font=("helvetica", "30"))
    bouton_grille6=tk.Button(racine, text=nom3, command=lambda: charger_grille2(3), font=("helvetica", "30"))
    bouton_grille4.grid(row=1,column=100)
    bouton_grille5.grid(row=2,column=100)
    bouton_grille6.grid(row=3,column=100)

def charger_grille2(x):
    global grille, grille1, grille2, grille3
    if x == 1:
        grille = [row[:] for row in grille1]  # Charger l'état de la grille1
    if x == 2:
        grille = [row[:] for row in grille2]  # Charger l'état de la grille2
    if x == 3:
        grille = [row[:] for row in grille3]  # Charger l'état de la grille3
    bouton_grille4.destroy()
    bouton_grille5.destroy()
    bouton_grille6.destroy()
    historique_coups=[]
    dessiner_grille()  

def enregistrer_grille():
    global bouton_grille1,bouton_grille2,bouton_grille3
    bouton_grille1=tk.Button(racine, text=nom1, command=lambda: enregistrer_grille2(1), font=("helvetica", "30"))
    bouton_grille2=tk.Button(racine, text=nom2, command=lambda: enregistrer_grille2(2), font=("helvetica", "30"))
    bouton_grille3=tk.Button(racine, text=nom3, command=lambda: enregistrer_grille2(3), font=("helvetica", "30"))
    bouton_grille1.grid(row=1,column=100)
    bouton_grille2.grid(row=2,column=100)
    bouton_grille3.grid(row=3,column=100)
    
def enregistrer_grille2(x):
    global grille,grille1,grille2,grille3,nom1,nom2,nom3
    if x==1:
        nom1=simpledialog.askstring("Nom du joueur", "Entrez le nom de la partie :")
        grille1=[row[:] for row in grille]
    if x==2:
        nom2=simpledialog.askstring("Nom du joueur", "Entrez le nom de la partie :")
        grille2=[row[:] for row in grille]
    if x==3:
        nom3=simpledialog.askstring("Nom du joueur", "Entrez le nom de la partie :")
        grille3=[row[:] for row in grille]
    bouton_grille1.destroy()
    bouton_grille2.destroy()
    bouton_grille3.destroy()

def verifier_noms():
    """ Vérifie si les deux noms sont remplis pour activer le bouton du jeu """
    joueur1 = zone_texte_joueur1.get().strip()
    joueur2 = zone_texte_joueur2.get().strip()
    
    if joueur1 and joueur2:
        bouton_demarrer.config(state="normal")
    else:
        bouton_demarrer.config(state="disabled")
    
def afficher_accueil():
    global nom_joueur1, nom_joueur2, zone_texte_joueur1, zone_texte_joueur2,bouton_demarrer
    accueil = tk.Tk()
    accueil.title("Page d'Accueil - Puissance 4")
    accueil.geometry("1000x700")
    accueil.minsize(1000,700)
    accueil.config(background="#041a40")
    
    frame= tk.Frame(accueil, background="#041a40")
    frame.pack(fill="both", expand=True)
    
    texte= tk.Label(frame, text="Bienvenue dans Puissance 4", font = ("Arial",30), bg="#0b52cf", fg="#dcff00")
    texte.pack(side="top", pady=10) 

    # Bouton pour commencer la partie
    bouton_demarrer = tk.Button(frame, text="Commencer la partie", command=lambda: demarrer_partie(accueil), font=("Helvetica", 40))
    bouton_demarrer.pack(expand=True)
    
    frame_pseudos = tk.Frame(frame, background="#041a40")
    frame_pseudos.pack(pady=20)

    tk.Label(frame_pseudos, text="Nom du Joueur 1 :", font=("Helvetica", 15), fg="red", bg="#041a40").pack(pady=5)
    zone_texte_joueur1 = tk.Entry(frame_pseudos, font=("Helvetica", 15), fg="red")
    zone_texte_joueur1.pack(pady=5)
    zone_texte_joueur1.bind("<KeyRelease>", lambda : verifier_noms())

    tk.Label(frame_pseudos, text="Nom du Joueur 2 :", font=("Helvetica", 15), fg="yellow", bg="#041a40").pack(pady=5)
    zone_texte_joueur2 = tk.Entry(frame_pseudos, font=("Helvetica", 15), fg="yellow")
    zone_texte_joueur2.pack(pady=5)
    zone_texte_joueur2.bind("<KeyRelease>", lambda : verifier_noms())

    bouton_manuel= tk.Button(frame, text="guide des stratégies", command=manuel,  font=("Helvetica", 15))
    bouton_manuel.pack(side="bottom", pady=10)
    
    bouton_quitter = tk.Button(frame, text="Quitter", command=accueil.destroy, font=("Helvetica", 20))
    bouton_quitter.pack(side="bottom", pady=10)

    accueil.mainloop()

def demarrer_partie(accueil):
    global Joueur1, Joueur2
    Joueur1 = zone_texte_joueur1.get().strip()
    Joueur2 = zone_texte_joueur2.get().strip()

    if Joueur1 and Joueur2:
        accueil.destroy()
        jeu()
        racine.deiconify()

        label_nom_joueur1.config(text=f"Joueur 1 : {Joueur1}")
        label_nom_joueur2.config(text=f"Joueur 2 : {Joueur2}")
    else:
        messagebox.showwarning("Erreur", "Veuillez entrer les noms des deux joueurs !")
  
def jeu():
    global joueur_act, grille, historique_coups
    joueur_act = 0
    grille = [[None for _ in range(6)] for _ in range(7)]
    historique_coups = []
    dessiner_grille()
    
def retour_accueil():
    racine.withdraw()
    reinitialiser_jeu()
    afficher_accueil()

def dessiner_grille():
    # Supprimer uniquement les cercles existants (structure de la grille)
    mon_canvas.delete("grille")  
    
    # Redessiner les cases de la grille (cercles blancs)
    for i in range(7):
        for j in range(6):
            mon_canvas.create_oval(
                (i * largeur_case + 25, j * hauteur_case + 25),
                ((i + 1) * largeur_case - 25, (j + 1) * hauteur_case - 25),
                fill="white", outline="blue", tags="grille"
            )

    # Redessiner les jetons déjà placés
    for col in range(7):
        for row in range(6):
            if grille[col][row] is not None:
                couleur = grille[col][row]
                mon_canvas.create_oval(
                    (col * largeur_case + 25, row * hauteur_case + 25),
                    ((col + 1) * largeur_case - 25, (row + 1) * hauteur_case - 25),
                    fill=couleur, outline=couleur, tags="jeton"
                )


def placer_jeton(x):
    global joueur_act
    colonne = x - 1  #  pour la grille (de 0 à 6)
    
    if grille[colonne][0] is not None:
        return messagebox.showwarning("Erreur", "Cette colonne est pleine, choisissez une autre colonne")

    for row in range(5, -1, -1):
        if grille[colonne][row] is None:
            couleur = "red" if joueur_act == 0 else "yellow"
            mon_canvas.create_oval((25 + colonne * largeur_case, 25 + row * hauteur_case),
                                   ((colonne + 1) * largeur_case - 25, (row + 1) * hauteur_case - 25), 
                                   fill=couleur, outline=couleur, tags="jeton")

            grille[colonne][row] = couleur
            historique_coups.append((colonne, row, couleur))  
            print(historique_coups)  
            label_joueur.config(text="")  

            if verifier_victoire(couleur):
                if couleur == "red":
                    messagebox.showinfo("Félicitations!", f"Bravo {Joueur1}, tu as gagné !")
                else : 
                    messagebox.showinfo("Félicitations!", f"Bravo {Joueur2}, tu as gagné !")
                return  # on sort ici si y’a un gagnant

            # Ajoute cette vérification juste après la victoire
            if all(grille[c][0] is not None for c in range(7)):
                messagebox.showinfo("Match nul", "La partie est terminée sans gagnant !")
                return

            joueur_act = 1 - joueur_act
            break

def verifier_victoire(couleur):
    #  horizontale
    for col in range(7):
        for row in range(6):
            if col < 4:  #
                if (grille[col][row] == couleur and
                    grille[col + 1][row] == couleur and
                    grille[col + 2][row] == couleur and
                    grille[col + 3][row] == couleur):
                    return True

    #  verticale
    for col in range(7):
        for row in range(6):
            if row < 3:  
                if (grille[col][row] == couleur and
                    grille[col][row + 1] == couleur and
                    grille[col][row + 2] == couleur and
                    grille[col][row + 3] == couleur):
                    return True

    #  diagonale (\)
    for col in range(7):
        for row in range(6):
            if col < 4 and row < 3:  
                if (grille[col][row] == couleur and
                    grille[col + 1][row + 1] == couleur and
                    grille[col + 2][row + 2] == couleur and
                    grille[col + 3][row + 3] == couleur):
                    return True

    # diagonale (/)
    for col in range(7):
        for row in range(6):
            if col >= 3 and row < 3:  
                if (grille[col][row] == couleur and
                    grille[col - 1][row + 1] == couleur and
                    grille[col - 2][row + 2] == couleur and
                    grille[col - 3][row + 3] == couleur):
                    return True

    return False

def annuler_coup():
    global joueur_act
    if len(historique_coups) == 0:  
        messagebox.showwarning("Erreur", "Aucun coup à annuler")
        return

    dernier_coup = historique_coups.pop() 
    colonne, ligne, couleur = dernier_coup

    mon_canvas.create_oval((25 + colonne * largeur_case, 25 + ligne * hauteur_case),
                           ((colonne + 1) * largeur_case - 25, (ligne + 1) * hauteur_case - 25), 
                           fill="white", outline="blue")

    grille[colonne][ligne] = None  

    joueur_act = 1 - joueur_act

def reinitialiser_jeu():
    global grille, joueur_act
    joueur_act = rd.choice([0, 1])  
    
    grille = [[None for _ in range(6)] for _ in range(7)]
    
    mon_canvas.delete("jeton")
   
    dessiner_grille()  

    couleur = "Rouge" if joueur_act == 0 else "Jaune"
    label_joueur.config(text="C'est au Joueur " + str(joueur_act + 1) + " (" + couleur + ") de commencer")

racine = tk.Tk()
racine.title("Puissance 4")
racine.withdraw()

bouton_1 = tk.Button(racine, text="1", command=lambda: placer_jeton(1), font=("helvetica", "30"))
bouton_2 = tk.Button(racine, text="2", command=lambda: placer_jeton(2), font=("helvetica", "30"))
bouton_3 = tk.Button(racine, text="3", command=lambda: placer_jeton(3), font=("helvetica", "30"))
bouton_4 = tk.Button(racine, text="4", command=lambda: placer_jeton(4), font=("helvetica", "30"))
bouton_5 = tk.Button(racine, text="5", command=lambda: placer_jeton(5), font=("helvetica", "30"))
bouton_6 = tk.Button(racine, text="6", command=lambda: placer_jeton(6), font=("helvetica", "30"))
bouton_7 = tk.Button(racine, text="7", command=lambda: placer_jeton(7), font=("helvetica", "30"))
bouton_1.grid(row=0,column=2)
bouton_2.grid(row=0,column=3)
bouton_3.grid(row=0,column=4)
bouton_4.grid(row=0,column=5)
bouton_5.grid(row=0,column=6)
bouton_6.grid(row=0,column=7)
bouton_7.grid(row=0,column=8)

CANVAS_WIDTH = 700
CANVAS_HEIGHT = 600
mon_canvas = tk.Canvas(racine, background="blue", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
mon_canvas.grid(row=1, column=2, rowspan=6 , columnspan=7)

largeur_case = CANVAS_WIDTH//7
hauteur_case = CANVAS_HEIGHT//6

frame_bas = tk.Frame(racine)  
frame_bas.grid(row=7, column=2, columnspan=7, pady=10)  

frame_nom = tk.Frame(racine, background="#041a40")
frame_nom.grid(row=8, column=2, columnspan=7, pady=10)

bouton_annuler = tk.Button(frame_bas, text="Annuler le dernier coup", command=annuler_coup, font=("helvetica", "12"))
bouton_annuler.grid(row=0, column=0, padx=10)

bouton_reset = tk.Button(frame_bas, text="Nouvelle Partie", command=reinitialiser_jeu, font=("helvetica", "12"))
bouton_reset.grid(row=0, column=1, padx=10)

label_joueur = tk.Label(frame_bas, text="", font=("helvetica", "12"))
label_joueur.grid(row=0, column=2, padx=10)

bouton_acccueil = tk.Button(frame_bas, text="retourner à l'acceuil", command= retour_accueil,font=("helvetica", "12") )
bouton_acccueil.grid(row=0, column=3, padx=10)

label_nom_joueur1 = tk.Label(frame_bas, text="Joueur 1 : ", font=("Helvetica", 15), fg="red", bg="#041a40")
label_nom_joueur1.grid(row=2, column=0, columnspan=7, pady=10)

label_nom_joueur2 = tk.Label(frame_bas, text="Joueur 2 : ", font=("Helvetica", 15), fg="yellow", bg="#041a40")
label_nom_joueur2.grid(row=2, column=2, columnspan=7, pady=10)

bouton_charger=tk.Button(frame_bas, text="charger", command=lambda: charger_grille(), font=("helvetica", "12"))
bouton_charger.grid(row=0,column=4)

bouton_enregistrer=tk.Button(frame_bas, text="enregistrer", command=lambda: enregistrer_grille(), font=("helvetica", "12"))
bouton_enregistrer.grid(row=0, column=6)

afficher_accueil()
reinitialiser_jeu()  
racine.mainloop()
print("hellooo")



# debut modification apres le premier controle 





def modifier_taille_grille(n_colonnes, n_lignes):
    
    global grille, largeur_case, hauteur_case, CANVAS_WIDTH, CANVAS_HEIGHT
   
    CANVAS_WIDTH = n_colonnes * 100  
    CANVAS_HEIGHT = n_lignes * 100   
   
    grille = [[None for _ in range(n_lignes)] for _ in range(n_colonnes)]
    largeur_case = CANVAS_WIDTH // n_colonnes
    hauteur_case = CANVAS_HEIGHT // n_lignes
   
    mon_canvas.config(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    dessiner_grille()


def cree_bouton(n_colonnes):
    for i in range(n_colonnes)
        bouton = tk.button(racine, text=str(i+1), command=lambda x=i+1: placer_jeton(x), font=("helvetica", "30"))
        bouton.grid(row=0, column=i+2, padx=5, pady=5)