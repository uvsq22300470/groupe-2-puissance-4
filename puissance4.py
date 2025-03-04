import tkinter as tk
import random as rd

racine = tk.Tk()
racine.title("Puissance 4")

liste=[]

def placer_jeton(x):
    global liste
    liste.append(x)
    print(x)


bouton_1 = tk.Button(racine,text="1",command=placer_jeton(1),font=("helvetica", "30"))
bouton_2 = tk.Button(racine,text="2",command=placer_jeton(2),font=("helvetica", "30"))
bouton_3 = tk.Button(racine,text="3",command=placer_jeton(3),font=("helvetica", "30"))
bouton_4 = tk.Button(racine,text="4",command=placer_jeton(4),font=("helvetica", "30"))
bouton_5 = tk.Button(racine,text="5",command=placer_jeton(5),font=("helvetica", "30"))
bouton_6 = tk.Button(racine,text="6",command=placer_jeton(6),font=("helvetica", "30"))
bouton_7 = tk.Button(racine,text="7",command=placer_jeton(7),font=("helvetica", "30"))


CANVAS_WIDTH = 700
CANVAS_HEIGHT = 600
mon_canvas = tk.Canvas(racine, background="blue", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

largeur_case = CANVAS_WIDTH//7
hauteur_case = CANVAS_HEIGHT//6
for i in range(7):
    for j in range(6):
        mon_canvas.create_oval((25+i*largeur_case, 25+j*hauteur_case),((i+1)*largeur_case, (j+1)*hauteur_case), fill="white")

bouton_1.grid(row=0,column=2)
bouton_2.grid(row=0,column=3)
bouton_3.grid(row=0,column=4)
bouton_4.grid(row=0,column=5)
bouton_5.grid(row=0,column=6)
bouton_6.grid(row=0,column=7)
bouton_7.grid(row=0,column=8)
mon_canvas.grid(row=1, column=2, rowspan=6 , columnspan=7)

racine.mainloop()
