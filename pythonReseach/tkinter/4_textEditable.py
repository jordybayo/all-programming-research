import tkinter 



racine0=tkinter.Tk() 

texte0=tkinter.Text(racine0, width=3, height=1) 
texte0.insert("end", "")
texte0.config(state=tkinter.NORMAL ,font="sans 11", width=4, height=1)
texte0.pack(side=tkinter.TOP) 


texte0.tag_add("accent", '1.13', '1.18') 
texte0.tag_add("accent", '2.7', '2.11') 
texte0.tag_add("accent", '3.7', '3.10') 
texte0.tag_config("accent", font="monospace 12 underline", foreground="#aa0055")














racine0.mainloop()
