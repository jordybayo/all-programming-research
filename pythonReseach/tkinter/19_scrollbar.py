import tkinter
fenetre0=tkinter.Tk()
ascenseur0=tkinter.Scrollbar(fenetre0) 
ascenseur0.pack(side=tkinter.RIGHT, fill=tkinter.Y)


ascenseur0= tkinter.Scrollbar(fenetre0, orient=tkinter.HORIZONTAL)
ascenseur0.pack(side=tkinter.TOP, fill=tkinter.X)

texte0=tkinter.Text(fenetre0, yscrollcommand=ascenseur0.set) 
texte0.insert(tkinter.END, "bla bla bla "*443) 
texte0.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
ascenseur0.config(command=texte0.yview)
fenetre0.mainloop()