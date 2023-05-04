import tkinter 
racine0=tkinter.Tk()
liste0=tkinter.Listbox(racine0, width=10, selectmode=tkinter.BROWSE) 
liste0.pack()
bouton0=tkinter.Button(racine0, text='Confirmer') 
bouton0.pack()
texte0=tkinter.Text(racine0, width=10) 
texte0.pack()
for element in ["Monthy", "Python", "Flying", "Circus"]:
      liste0.insert(tkinter.END, element)
def clic(inutile):
      for i in liste0.curselection():
              texte0.insert(tkinter.INSERT, liste0.get(i)+" ")
bouton0.bind('<Button-1>', clic)
racine0.mainloop() 
"""
permet de selectionner sans cliquer sur le bouton
import tkinter
racine0=tkinter.Tk() 
liste0=tkinter.Listbox(racine0, width=10) 
liste0.pack() 
texte0=tkinter.Text(racine0, width=10) 
texte0.pack()
for element in ["Monthy", "Python", "Flying", "Circus"]:
      liste0.insert(tkinter.END, element) 
      def clic(inutile):
            texte0.insert(tkinter.INSERT, liste0.get(liste0.curselection())+" ")
liste0.bind('<Double-1>', clic) 
racine0.mainloop()
"""