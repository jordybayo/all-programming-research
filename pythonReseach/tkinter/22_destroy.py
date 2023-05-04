import tkinter 
racine0=tkinter.Tk() 
def detruire():  
    bouton0.destroy()  
    texte0=tkinter.Label(racine0, text="Destruction accomplie")  
    texte0.pack() 
bouton0=tkinter.Button(racine0, text="Autodestruction", command=detruire) 
bouton0.pack() 
racine0.mainloop()
#cette fonction destroy permet de completement detruire un widget es plus mieux a faire avant de quitter