#coding:utf-8

import math 


class Binary(object):
	"""binary class object of converting"""
	def __init__(self,number):
		self.number = number
	def binary_decimal(self):
		self.number = self.number +2
		print(self.number)
	def binary_octal(self):
		pass
	def binary_hexadecimal(self):
		pass


binaire = Binary(12)
binaire.binary_decimal()


var = 1245
compteur = 0
nb_binaire = 0
var = str(var)
liste = list()
print(liste[:])
for x in var:
	liste.append(x)
	compteur = compteur+1
print(liste)
print(compteur)


for y in liste:
	nb_binaire = nb_binaire + (math.pow(y , compteur))
	compteur = compteur - 1

print('finalement c\'est : ',compteur)

"""

class Octal(object):
 	octal class object of converting
 	def __init__(self, number):
 		self.number = number
	def octal_decimal(self):
		pass
	def octal_binary(self):
		pass
	def octal_hexadecimal(self):
		pass



class Hexadecimal(object):
	hexadecimal class object of converting
	 	def __init__(self, number):
	 		self.number = number
	def hexadecimal_decimal(self):
		pass
	def hexadecimal_binary(self):
		pass
	def hexadecimal_octal(self):
		pass



class Decimal(object):
	decimal class object of converting
	 	def __init__(self, number):
	 		self.number = number
	def decimal_hexadecimal(self):
		pass
	def decimal_binary(self):
		pass
	def decimal_octal(self):
		pass



"""







if __name__ == "__main__":
	Binary(object)







pour convertir de B a base 10 on prend les indexes qu'on multiplie fois B epx(indexe) jusqu'à n-1
pour passer de de decimale a base B on fait jesute une division succesive par B jusqu'à obtenir Vx=1 puis on prend le resultat en inverse

