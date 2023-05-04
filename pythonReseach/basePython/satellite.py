
#coding:utf-8

import math

class Satellite(object):
    """classe d'un Satellite;les methodes:\impulsion\ & \affiche_vitesse\ & \energie\ """
    def __init__(self,masse,vitesse,nom):
        self.masse = 100
        self.vitesse = 0
        self.nom = "Satellite^defaut"
    def impulsion(self,force,duree):
        variation_vit = (force * duree) / self.masse
        return variation_vit
    def affiche_vitesse(self):
        print("La vitesse issue a la variation du satellite",self.nom," est:",impulsion())
    def energie(self):
        carre = pow(self.variation_vit,2)
        energieCinetique = (self.masse * carre) / 2
        return energieCinetique
    
        
        
