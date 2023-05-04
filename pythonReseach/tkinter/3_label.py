import tkinter 
racine0=tkinter.Tk() 
mot0=tkinter.Label(racine0,text="Premier texte\ndans une fenetre") 
mot0.pack(side=tkinter.BOTTOM) 

dessin0=tkinter.PhotoImage(file="img.JPG")
etiquette0=tkinter.Label(image=dessin0) 
etiquette0.pack()

racine0.mainloop() 