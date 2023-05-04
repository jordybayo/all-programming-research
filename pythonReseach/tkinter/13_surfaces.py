import tkinter 
racine0=tkinter.Tk() 
fond0=tkinter.Canvas(racine0, width=350, height=200, background='darkgray') 
rectangle0=fond0.create_rectangle(50, 40, 300, 90) 
ellipse0=fond0.create_oval(30, 120, 150, 180)
quartier0=fond0.create_arc(160, 130, 230, 200, start=30, extent=120, style=tkinter.PIESLICE) 
arc0=fond0.create_arc(250, 130, 320, 200, start=30, extent=120, style=tkinter.CHORD) 
polygone0=fond0.create_polygon(35, 105, 120, 85, 95, 25, 80, 75, 25, 60, 65, 30, fill="cyan", width=5, outline='black') 

fond0.pack() 
racine0.mainloop()