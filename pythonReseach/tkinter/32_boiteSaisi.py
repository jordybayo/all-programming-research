import tkinter, tkSimpleDialog
racine0=tkinter.Tk() 
texte0="???" 
etiquette0=tkinter.Label(text=texte0) 
etiquette0.pack() 
texte0=tkSimpleDialog.askstring("Espace de parole", "Exprimez-vous!") 
etiquette0.config(text=texte0) 
racine0.mainloop() 