import tkinter

def ecran(dummy):  
    print (choix0.get())

racine0=tkinter.Tk()
choix0=tkinter.StringVar(); 
choix0.set("Rouge") 
option0=tkinter.OptionMenu(racine0, choix0, "Rouge", "Vert", "Bleu", command=ecran) 
option0.pack()
racine0.mainloop()