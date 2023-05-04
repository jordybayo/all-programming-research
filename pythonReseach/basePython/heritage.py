#coding:utf-8

"""
heritage : relation mere  fille

fontion d'héritage : isinstance-->si l'objet est d'une instance de classe
					 issubclass-->si une classe est pas fille de l'autre classe mere

"""

#classe mere
class Vehicule(object):
	"""cette classe contient  la fonction de deplacement et 2 attribut """
	def __init__(self,nom_voiture,qte_essence):
		self.nom = nom_voiture
		self.qte_essence = qte_essence

	def deplacement(self):
		print('le Vehicule {} se deplace'.format(self.nom))


#classe fille
class Voiture(Vehicule):
	""" cette classe contient uner fonction deplacement et 3 attribut """
	def __init__(self,nom,carburant,marchandise):
		Vehicule.__init__(self,nom,carburant)
		self.marchandise = marchandise

	def porte(self):
		print("la voiture {} transporte une marchandise appele {}".format(self.nom,self.marchandise))


V1 = Voiture("toyota carina",90,"fruit de mer naturel")
V1.porte()

print(isinstance(V1,Voiture))
print(issubclass(Voiture,Vehicule))



#classe mere
class  Carnivore(object):
	"""docstring for  Carnivore"""
	pass


#class fille
class Herbivore(Carnivore):
	pass


class Cochon(Carnivore,Herbivore):
	"""docstring for Cochon"""
	pass
		





