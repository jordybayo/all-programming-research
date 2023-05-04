import tkinter
def colorer():  
    texte0.config(text="Ce texte change et prend de la couleur", fg="blue", bg="red")
racine0=tkinter.Tk()
texte0=tkinter.Label(racine0, text="Ceci est un texte en noir et blanc") 
texte0.pack()
bouton0=tkinter.Button(racine0, text="Colorer le texte", command=colorer) 
bouton0.pack()
racine0.mainloop()
#Cela peut être utilisé pour basculer de l'état DISABLED d'un widget à son état ACTIVE . 
#ce module peut m'aider dans un chagement de temperature a changer de celsius a farhenreit ou de farhenreit a celsius