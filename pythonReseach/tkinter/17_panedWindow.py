import tkinter 


racine0=tkinter.Tk() 
racine0.geometry("400x300") 
division0=tkinter.PanedWindow(orient=tkinter.VERTICAL) 
division0.pack(expand="yes", fill="both") 
haut0=tkinter.Label(division0, text="Panneau du haut") 
division0.add(haut0) 
milieu0=tkinter.Label(division0, text="Panneau du milieu") 
division0.add(milieu0) 
bas0=tkinter.PanedWindow(orient=tkinter.HORIZONTAL) # nouvelle division 
bas0.pack(expand="yes", fill="both") 
gauche=tkinter.Label(bas0, text="Panneau bas-gauche") 
bas0.add(gauche) 
droit=tkinter.Label(bas0, text="Panneau bas-droit") 
bas0.add(droit) 
division0.add(bas0) # on acheve la declaration du panneau 
racine0.mainloop()