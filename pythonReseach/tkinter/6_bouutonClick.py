import tkinter 

racine0=tkinter.Tk()
bouton0=tkinter.Button(racine0, text="Attention", bitmap="error", compound=tkinter.RIGHT,  command=racine0.quit) #BitmapIamge(image=)image personnel
bouton0.pack(side=tkinter.BOTTOM) 
racine0.mainloop()