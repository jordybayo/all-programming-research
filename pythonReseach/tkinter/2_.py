# -*- encoding:utf-8 -*-


import tkinter 

racine0 = tkinter.Tk()
racine0.geometry("400x300")
cadre0=tkinter.Frame(racine0)


button1=tkinter.Button(cadre0, text="Button 1")
button1.pack(side=tkinter.LEFT)
button2 = tkinter.Button(cadre0, text="Boutton 2")
button2.pack(padx=(20), pady=(20))

button3 = tkinter.Button(cadre0, text="button 3")
button3.pack()

cadre0=tkinter.LabelFrame(racine0, text="the title")
tkinter.Frame(racine0, bg="red", border=50, relief=tkinter.GROOVE) 
cadre0.pack()
cadre0.mainloop()