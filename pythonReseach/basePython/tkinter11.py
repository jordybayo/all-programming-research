#coding:utf-8

from tkinter import *

class Interface(Frame):
    """Notre fenetre principlae. tous les widgets sont stockés comme attributs de cette fenetre."""
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.nb_clic = 0

        #création de nos widgets
        self.message = Label(self, text="vous n'avez pas cliqué sur le bouton.")
        self.message.pack()
        self.buton_quitter = Button(self, text="Qitter", command=self.quit)
        self.buton_quitter.pack(side="left")

        self.bouton_cliquer = Button(self, text="Cliquer ici", fg="red")
        self.bouton_cliquer.pack(side="right")

        def cliquer(self):
            """il ya eu un clic sur le bouton. on change la valeur du label message"""
            self.nb_clic += 1
            self.message["text"] = "Vous avez cl iqué {} fois".format(self.nb_clic)

fenetre = Tk()
interface = Interface(fenetre)
interface.mainloop()
interface.destroy()