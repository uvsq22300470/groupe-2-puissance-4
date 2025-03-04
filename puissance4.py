import tkinter as tk
import random as rd

racine = tk.Tk()
racine.title("Puissance 4")

def placer_jeton(x):
    print(x)

#def creer_grille():
#    mon_canvas.create_rectangle(500,500,500,500,fill="white")

bouton_1 = tk.Button(racine,text="1",command=placer_jeton(1))
bouton_2 = tk.Button(racine,text="2",command=placer_jeton(2))
bouton_3 = tk.Button(racine,text="3",command=placer_jeton(3))
bouton_4 = tk.Button(racine,text="4",command=placer_jeton(4))
bouton_5 = tk.Button(racine,text="5",command=placer_jeton(5))
bouton_6 = tk.Button(racine,text="6",command=placer_jeton(6))
bouton_7 = tk.Button(racine,text="7",command=placer_jeton(7))


CANVAS_WIDTH = 900
CANVAS_HEIGHT = 775
mon_canvas = tk.Canvas(racine, background="blue", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
#creer_grille()

bouton_1.grid(row=0,column=1)
bouton_2.grid(row=0,column=2)
bouton_3.grid(row=0,column=3)
bouton_4.grid(row=0,column=4)
bouton_5.grid(row=0,column=5)
bouton_6.grid(row=0,column=6)
bouton_7.grid(row=0,column=7)
mon_canvas.grid(row=1, column=1, rowspan=6 , columnspan=7)

racine.mainloop()
