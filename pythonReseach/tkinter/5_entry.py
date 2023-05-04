import tkinter 
racine0=tkinter.Tk() 
invite0=tkinter.Label(racine0, text='Cliquer et saisir:', width=20, height=3, fg="navy") 
invite0.pack() 
texte0=tkinter.StringVar()  # definition d'une variable-chaine pour recevoir la saisie d'un texte 
texte0.set("Sans commentaire")  # facultatif: assigne une valeur à la variable
saisie0=tkinter.Entry(textvariable=texte0, width=30) 
saisie0.pack() 
racine0.mainloop() 
nb1 = texte0.get()
nb1 = int(nb1)
print (nb1)# affiche le texte saisi à la fermeture de la fenêtre