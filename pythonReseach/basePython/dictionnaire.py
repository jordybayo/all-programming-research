#coding:utf-8

"""
dictionnaire vide : dico = {}



#création de dico
dico = { "name":"je suis" , 3:[1,2,4,]  , 4:(4,5,6) }
print(dico["name"])

#modification de dico
dico["chien"] = "c'est un féliin "
print(dico)
dico[3] = "maintenant chaine"
print(dico)



#supréssion de dico
valeur_supprime = dico.pop(4)
print("valeur supprimé = ",valeur_supprime)



#vérifie l'existence
if "name" in dico:
	print("oui")
"""
dico = { "name":"je suis" , 3:[1,2,4,]  , 4:(4,5,6) }


#afficher les clées


for (k,v) in dico.items():
	print("clé: {} = valeur:{}".format(k,v))