#coding:utf-8

"""
try:
	ce qu'il faut faire
except:
	l'érreur d'erreur
--------------------------------------code minimal
else:
	afcfiche si opération bien exécuté
finally:
	affiche un message dans tout les cas.
----------------------LES DIFFERENTES ERREURS NATIVE DE PYTTHON-------------------------
ValueError
ZeroDivisionError
TypeError
NameError
AssertionError: <condition que vous vouler que ce soit verifié>
------------------------------CREATION DES PROTOTYPES DE GESTION D'ERREUR raise ET assert----------------------
"""
from random import randrange

nombre_aleatoire = randnge(50)
print("Nb_alea : ", nombre_aleatoire)




items = input("Entrer le nombre d'items")
try:
	items = int(items)
	assert items<10
except ValueError:
	print("valeur incorrect")
except AssertionError:
	print("Armes en excès")
else:
	print("++Nouvel arme ajouté :)")
finally:
	print("VOUS ETES DANS LE JEUX DRAGON ROUGE")
