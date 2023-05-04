import tkinter
def souris(evt0):  
    print ("X: %03d - Y: %03d" %(evt0.x_root, evt0.y_root) )
    print ("x: %03d - y: %03d" %(evt0.x, evt0.y)  )
    print (evt0.num, evt0.type, evt0.widget)
 
racine0=tkinter.Tk()
cadre0=tkinter.Frame(racine0, width=400, height=300) 
cadre0.bind("<Button-1>", souris) 
cadre0.pack()
racine0.mainloop()

#a revoir pour des evenements sur motion etc butoon release etc...