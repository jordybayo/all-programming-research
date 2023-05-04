import tkinter
def activer():  
    bouton0.config(state=tkinter.ACTIVE)
racine0=tkinter.Tk()
bouton0=tkinter.Button(racine0, text="Quitter", state=tkinter.DISABLED, command=racine0.quit) 
bouton0.pack()
bouton1=tkinter.Button(racine0, text="Activer", command=activer) 
bouton1.pack()
racine0.mainloop()