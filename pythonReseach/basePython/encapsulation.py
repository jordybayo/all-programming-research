#coding:utf-8


class Personne(object):
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom
        self.age = 12
        self._lieu_residence = "Douala"
        self._message = "bonjour a tous"
    def _get_lieu_residence(self):
        return _lieu_residence
    def _set_lieu_residence(self,nouveau_lieu):
        self._lieu_residence = nouveau_lieu
        return nouveau_lieu
    lieu_residence = property(_get_lieu_residence,_set_lieu_residence)
        



P1 = Personne("bayo","jordy")
print(P1._lieu_residence)
print(P1.prenom)
print(P1.age)
print(P1._message)

P1.prenom = "alba"
print(P1.prenom)

P1._lieu_residence = "BAff"
print(P1._lieu_residence)