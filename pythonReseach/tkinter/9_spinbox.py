
import tkinter 
racine0=tkinter.Tk() 
retour0=tkinter.StringVar() 
retour0.set(37.2) 
spin0=tkinter.Spinbox(racine0, from_=35, to=43, increment=.2, width=4) 
spin0.config(textvariable=retour0, font="sans 24", justify="center") 
spin0.pack() 
racine0.mainloop()
