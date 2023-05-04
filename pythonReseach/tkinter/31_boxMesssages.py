"""
title="" donne un titre à la boîte de message ou de choix
 message="" définit le message en gras, à l'intérieur de la boîte 
 detail="" permet un message secondaire, dans une fonte de plus petite taille 
 default="no" ou default="cancel" redéfinit le bouton par défaut 
 icon et type : voir Reconfiguration des boîtes """

import tkMessageBox
tkMessageBox.showinfo(title="Information", message="There's spam") 
tkMessageBox.showwarning(title="Avertissement", message="There's no spam") 
tkMessageBox.showerror(title="Erreur", message="There's no spam") 