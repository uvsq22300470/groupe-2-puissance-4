import tkinter as tk
import random as rd
from tkinter import messagebox

racine = tk.Tk()
racine.title("Puissance 4")

liste=[]
joueur_act=0
grille =[[None for _ in range(6)] for _ in range(7)]



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

largeur_case = CANVAS_WIDTH//7
hauteur_case = CANVAS_HEIGHT//6
for i in range(7):
    for j in range(6):
        mon_canvas.create_oval((25+i*largeur_case, 25+j*hauteur_case),((i+1)*largeur_case-25, (j+1)*hauteur_case-25), fill="white",outline="blue")

def placer_jeton(x):
    global joueur_act
    colonne = x - 1  # Adapter pour la grille (de 0 à 6)
    
    if grille[colonne][0] is not None:
        messagebox.showwarning("Erreur", "Cette colonne est pleine, choisissez une autre colonne")
        return

    for row in range(5, -1, -1):
        if grille[colonne][row] is None:
            couleur = "red" if joueur_act == 0 else "yellow"
            mon_canvas.create_oval((25 + colonne * largeur_case, 25 + row * hauteur_case),
                                   ((colonne + 1) * largeur_case - 25, (row + 1) * hauteur_case - 25), 
                                   fill=couleur, outline=couleur)

            grille[colonne][row] = couleur
            joueur_act = 1 - joueur_act
            break


bouton_1.grid(row=0,column=2)
bouton_2.grid(row=0,column=3)
bouton_3.grid(row=0,column=4)
bouton_4.grid(row=0,column=5)
bouton_5.grid(row=0,column=6)
bouton_6.grid(row=0,column=7)
bouton_7.grid(row=0,column=8)
mon_canvas.grid(row=1, column=2, rowspan=6 , columnspan=7)

racine.mainloop()
