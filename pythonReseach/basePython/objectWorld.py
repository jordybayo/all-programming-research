#coding:utf-8

import math

class Satellite(object):
    """classe d'un Satellite;les methodes:
       \impulsion\ & \affiche_vitesse\ & \energie\ 
    """
    def __init__(self,masseSat,vitesseSat,nom):
        self.masse = masseSat
        self.vitesse = vitesseSat
        self.name = nom
        self.variation_vit = float()

    def impulsion(self,force,duree):
        self.variation_vit = (force * duree) / (self.masse)

    def affiche_vitesse(self):
        #self.nom = 'Zoe'
        print("La vitesse du satellite {} est: {}m/s".format(self.name,self.variation_vit))
        
    def energie(self):
        carre = pow(self.variation_vit,2)
        energieCinetique = (self.masse * carre) / 2
        return energieCinetique
    
        
        
s1=Satellite(250,10,'Zoé')
s1.impulsion(500,15)
s1.affiche_vitesse()
print("Son energie Cinétique est : ",s1.energie(),'J')