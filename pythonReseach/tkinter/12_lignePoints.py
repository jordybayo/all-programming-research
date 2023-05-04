import tkinter 
racine0=tkinter.Tk() 
fond0=tkinter.Canvas(racine0, width=1000, height=1000, background='darkgray') 
fond0.pack()
line0=fond0.create_line(30, 50, 170, 50, dash=(7, 2, 2, 2), dashoff=2)
ligne=fond0.create_line(40, 190, 250, 110, 270, 170, 180, 120, smooth=True, capstyle=tkinter.ROUND, arrow=tkinter.LAST, arrowshape=(8, 10, 3), joinstyle=tkinter.ROUND)

ligne43=fond0.create_line(10, 10, 10, 380, 380, 380, 380, 10, smooth=True)
racine0.mainloop() 
