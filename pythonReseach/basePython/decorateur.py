#coding:utf-8



import time
"""
definir une obseletation sur une fonction
def mon_decorateur(fonction):
	print("notre decorateur est appele avec en parame la fonction {0}".format(fonction))
	return fonction


def obsolete(fonction_origine):
	def fonction_modifiee():
		raise RuntimeError("la fonction {0} est obsolète!".format(fonction_origine))
	return fonction_modifiee


@obsolete
def salut():
	print("salut")


salut()

"""

#decorateur permettant d'indiquer lque le nombre de temps est passé
"""
def controller_temps(nb_secs):

	def decorateur(fonction_a_executer):

		def fonction_modifiees(*para_nommes , **para_nonNOmmes):
			temps_avant = time.time()
			ret = fonction_a_executer(*para_nommes , **para_nonNOmmes)
			temps_apres = time.time()
			temps_execution = temps_apres - temps_avant
			if temps_execution >= nb_secs:
				print("la fonction {0} a mis {1} pur s'executer ".format(fonction_a_executer,temps_execution))
			return ret
		return fonction_modifiees
	return decorateur
	

@controller_temps(4)
def attendre_saisi():
	input("eppuyez sur <<ENTER>> ...")


attendre_saisi()

"""
def singleton(classe_definie):
	instances = {}
	def get_instance():
		if classe_definie not in instances:
			instances[classe_definie] = classe_definie()
		return instances[classe_definie]
	return get_instance



@singleton
class Test(object):
	pass


a = Test()
b = Test()

print(a is b)


