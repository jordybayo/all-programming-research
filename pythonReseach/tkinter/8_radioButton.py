
import tkinter 
racine0=tkinter.Tk() 
retour0=tkinter.IntVar() # cree une variable entiere pour recevoir la valeur retour 
retour0.set(2) # le bouton [Bof] mis par defaut (value=2) 
bouton1=tkinter.Radiobutton(racine0, text="Oui", variable=retour0, value=1, bd=2) 
bouton2=tkinter.Radiobutton(racine0, text="Bof", variable=retour0, value=2, bd=3) 
bouton3=tkinter.Radiobutton(racine0, text="Non", variable=retour0, value=3, bd=3) 
bouton1.grid(row=0, column=0) 
bouton2.grid(row=0, column=1) 
bouton3.grid(row=0, column=2) 
bouton3.indicatoron=0 
bouton3.border=2
racine0.mainloop()