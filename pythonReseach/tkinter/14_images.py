import tkinter 
racine0=tkinter.Tk() 
photo0=tkinter.PhotoImage(file="img.gif")  # ouverture du fichier GIF 
largeur=photo0.width(); hauteur=photo0.height() # determination des dimensions 
racine0.geometry(str(largeur+2)+"x"+str(hauteur+2)) 
fond0=tkinter.Canvas(racine0, bg='gray') 
fond0.pack() 
image0=fond0.create_image(largeur//2+1, hauteur//2+1, image=photo0) # image a centrer racine0.mainloop() 