#coding:utf-8

maList = list()
print(maList)

maListe1 = []
print(maListe1)

maListe2 = range(4)
print(maListe2)

print('parcour de la liste avec while')
i=0;
while i<len(maListe2) :
    print(i)
    i+=1

print('avec la boucle for plutot')

for valeur in maListe2:
    print(valeur)

crc ="Listes avec des chaines de caracteres"
print(crc.center(60,'-'))
listCArac = ["arc" ,  "epée" , "bouclié" , "yomoMA"]
print('selcetion de liste')
print(listCArac[:])
print(listCArac[:2])
print(listCArac[1:])
print(listCArac[-1])
print(listCArac[1:4])
crc ="modification d'une liste"
print(crc.center(60,'-'))
listModif = ["fuck" , "you" , "man" , "#" , 666]
print(listModif)
listModif[4] = 777
print(listModif)
listModif[:2]= [777] * 2
print(listModif[:])

crc ="recerche dans une liste"
print(crc.center(60,'-'))
listSearch = [16 ,"bouclier"]
if 16 in listSearch:
    print('je possede un bouclier')
else:
    print('je ne possede pas de bouclier')
crc ="Ajout dans une liste"
print(crc.center(60,'-'))
listAjust = list()
listAjust.append("arc")
print(listAjust[:])
listAjust.append(60)
print(listAjust)
listAjust.insert(1,69)
print(listAjust)
print('Supprimmons un peu')
listAjust.remove(60)
indice = listAjust.index("arc")
del listAjust[indice]
print(listAjust[:])





crc ="tri dans une liste"
print(crc.center(60,'-'))
listTrié = ["lol" , "conard" , "arbeloa" , "lol"]
print(listTrié)
listTrié.sort()
print(listTrié[:])
listTrié.reverse()
print(listTrié[:])
print('le nombre de fois de \'lol\': ', listTrié.count("lol"))
chaine = " ".join(list(listTrié))
print('la chaine est : ',chaine)
listTrié.clear()

crc ="copie de liste"
print(crc.center(60,'-'))

list1 = [1 , 2, 3, 4]
list2 = [0, -1, -2, -3]
list3 = list()
list2 = list1
print(list1[:])
print(list2[:])
list2.append("un-plus")
print(list1[:])
print(list2[:])
from copy import deepcopy
list2 = deepcopy(list1)
list2.append("un-moins")
print(list1[:])
print(list2[:])

list3 = list1 + list2
print(list3[:])

