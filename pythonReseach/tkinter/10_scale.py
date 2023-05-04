import tkinter 
racine0=tkinter.Tk() 
retour0=tkinter.IntVar() 
retour0.set(43) 
echelle0=tkinter.Scale(racine0, variable=retour0, from_=100, to_=1, resolution=1, length=101, width=12, sliderlength=20, repeatinterval=400) 
echelle0.pack() 
racine0.mainloop()