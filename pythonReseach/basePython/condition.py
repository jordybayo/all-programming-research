#coding:utf-8

identifiant0 = "jordy"
passWord0 = "motdepasse"
"""
print('========== bienvenue Connecter Vous svp ! ==================')
identifiant1 = input("Nom d'utilisateur : ")
passWord1 = input("Mot de passe : ")

identifiant1 = str(identifiant1)
passWord1 = str(passWord1)

if identifiant1 == identifiant0 and passWord1 == passWord0:
	print("connect Sucessfull ! ")
"""

"""
print("=============test de voelle===================")
letter = input("just type your letter to see his nature: ")
voyelle="aeiouy"
if letter in voyelle:
	print("c'est une consonne")
else:
	print("c'est une voyelle")
"""
"""
print("=================comparaision de deyx nombre=================")
nb1=0
nb2=0
nb1=input("entre le prtemier nombre: ")
nb2=input("entre le druxieme nombre: ")
if nb1<nb2:
	print("le nb1  est superieur")
elif nb1>nb2:
	print("le nb2 est inferieur")
"""
print("==================Année Bisexstile=========================")
Annee = input("entrer votre Année : ")
Annee = int(Annee)
Bisexstile=False
if (Annee % 4) == 0:
	if (Annee%100) == 0:
		if (Annee%400) == 0:
			Bisexstile = True
		else Bisexstile = False
	else Bisexstile = False
else Bisexstile = False

if Bisexstile:
	print("Votre Annee est Bisexstile")
elif Bisexstile==False:
	print("Votre Année n'est pas Bisexstile")
	

