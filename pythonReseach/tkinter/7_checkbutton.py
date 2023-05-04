import tkinter 
racine0=tkinter.Tk() 
retour0=tkinter.IntVar() # creation de variable-retour
bouton0=tkinter.Checkbutton(racine0, variable=retour0, text="Cochez-moi")
bouton0.pack() 
racine0.mainloop()
# recuperation de la valeur lors de la sortie de la boucle mainloop(): 
if retour0.get(): 
    # la variable 'retour0' = 1 si la case est cochee, 0 sinon  
    print ("Tilt!") 
else:  
    print ("Vide!") 