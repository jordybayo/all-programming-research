#coding:utf-8

from tkinter import *


fenetre  = Tk()

champ_label = Label(fenetre, text="salut young devs tu evolue en progr !")
champ_label.pack()

print(champ_label["text"])
champ_label["text"]  = "bonsoir young devps tu evolue en info!"
print(champ_label["text"])

champ_label_saisi= Label(fenetre, text="Nom: ")
champ_label_saisi.pack()
var_texte = StringVar()
ligne_texte  =  Entry(fenetre, textvariable=var_texte , width="30")
ligne_texte.pack()


var_case = IntVar()
case  = Checkbutton(fenetre, text="ne plus poser cette question", variable=var_case)
case.pack()
var_texte.get()
if (var_texte == '1'):
    print("c'est bon")
elif(var_texte=='0'):
    print("c'est pas bon")
else:print("invalide")


var_choix = StringVar
choix_rouge = Radiobutton(fenetre , text="rouge" , variable=var_choix,  value="rouge")
choix_vert= Radiobutton(fenetre , text="vert" , variable=var_choix,  value="vert")
choix_bleu= Radiobutton(fenetre , text="bleu" , variable=var_choix,  value="bleu")
choix_rouge.pack()
choix_vert.pack()
choix_bleu.pack()



liste = Listbox(fenetre)
liste.pack()
liste.insert(END, "pierre")
liste.insert(END,"feuille")
liste.insert(END,"ciseau")
print(liste.curselection())

var_choix = Frame(fenetre, width=768, height=576 , borderwidth=78)
var_choix.pack(fill=BOTH)
message = Label(var_choix, text="Notre fenetre")
message.pack(side="top" , fill=X)


boutton_quitter = Button(fenetre , text="quitter ?", command=fenetre.quit)
boutton_quitter.pack()









fenetre.mainloop()


