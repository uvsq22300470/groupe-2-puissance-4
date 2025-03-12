import tkinter as tk
import random as rd
from tkinter import messagebox

racine = tk.Tk()
racine.title("Puissance 4")

joueur_act=0
grille =[[None for _ in range(6)] for _ in range(7)]
historique_coups = []  # Liste pour enregistrer les coups (colonne, ligne, couleur)

bouton_1 = tk.Button(racine, text="1", command=lambda: placer_jeton(1), font=("helvetica", "30"))
bouton_2 = tk.Button(racine, text="2", command=lambda: placer_jeton(2), font=("helvetica", "30"))
bouton_3 = tk.Button(racine, text="3", command=lambda: placer_jeton(3), font=("helvetica", "30"))
bouton_4 = tk.Button(racine, text="4", command=lambda: placer_jeton(4), font=("helvetica", "30"))
bouton_5 = tk.Button(racine, text="5", command=lambda: placer_jeton(5), font=("helvetica", "30"))
bouton_6 = tk.Button(racine, text="6", command=lambda: placer_jeton(6), font=("helvetica", "30"))
bouton_7 = tk.Button(racine, text="7", command=lambda: placer_jeton(7), font=("helvetica", "30"))


CANVAS_WIDTH = 700
CANVAS_HEIGHT = 600
mon_canvas = tk.Canvas(racine, background="blue", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

mon_canvas.grid(row=1, column=0, rowspan=6, columnspan=7)

largeur_case = CANVAS_WIDTH//7
hauteur_case = CANVAS_HEIGHT//6
for i in range(7):
    for j in range(6):
        mon_canvas.create_oval((25+i*largeur_case, 25+j*hauteur_case),((i+1)*largeur_case-25, (j+1)*hauteur_case-25), fill="white",outline="blue")


def placer_jeton(x):
    global joueur_act
    colonne = x - 1  #  pour la grille (de 0 à 6)
    
    if grille[colonne][0] is not None:
        messagebox.showwarning("Erreur", "Cette colonne est pleine, choisissez une autre colonne")
        return

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
                messagebox.showinfo("Félicitations!", f"Le joueur {couleur} a gagné !")
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

def dessiner_grille():
    for i in range(7):
        for j in range(6):
            mon_canvas.create_oval(
                (i * largeur_case + 25, j * hauteur_case + 25),
                ((i + 1) * largeur_case - 25, (j + 1) * hauteur_case - 25),
                fill="white", outline="blue")

def reinitialiser_jeu():
    global grille, joueur_act
    joueur_act = rd.choice([0, 1])  
    
    grille = [[None for _ in range(6)] for _ in range(7)]
    
    mon_canvas.delete("jeton")
   
    dessiner_grille()  

    couleur = "Rouge" if joueur_act == 0 else "Jaune"
    label_joueur.config(text=f"C'est au Joueur {joueur_act + 1} ({couleur}) de commencer")



bouton_1.grid(row=0,column=2)
bouton_2.grid(row=0,column=3)
bouton_3.grid(row=0,column=4)
bouton_4.grid(row=0,column=5)
bouton_5.grid(row=0,column=6)
bouton_6.grid(row=0,column=7)
bouton_7.grid(row=0,column=8)
mon_canvas.grid(row=1, column=2, rowspan=6 , columnspan=7)

frame_bas = tk.Frame(racine)  
frame_bas.grid(row=7, column=2, columnspan=7, pady=10)  

bouton_annuler = tk.Button(frame_bas, text="Annuler le dernier coup", command=annuler_coup, font=("helvetica", "12"))
bouton_annuler.grid(row=0, column=0, padx=10)

bouton_reset = tk.Button(frame_bas, text="Nouvelle Partie", command=reinitialiser_jeu, font=("helvetica", "12"))
bouton_reset.grid(row=0, column=1, padx=10)

label_joueur = tk.Label(frame_bas, text="", font=("helvetica", "12"))
label_joueur.grid(row=0, column=2, padx=10)




reinitialiser_jeu()  

racine.mainloop()
