#! /usr/bin/python 
import tkinter
racine0=tkinter.Tk() 
racine0.geometry("300x200")
canevas0=tkinter.Canvas(racine0, width=300, height=200) 

rectangle0=canevas0.create_rectangle(50, 50, 150, 100, fill="red") 
ellipse0=canevas0.create_oval(75, 75, 150, 125, fill="blue") # se place au-dessus 
canevas0.tag_lower(ellipse0) # replace le rectangle devant l'ellipse
canevas0.itemconfigure(rectangle0, fill="green")
canevas0.move(rectangle0, 20, -10) 
canevas0.tag_raise(rectangle0)
canevas0.pack() 
racine0.mainloop()