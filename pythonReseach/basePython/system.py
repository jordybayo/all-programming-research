import sys
import os

print(sys.stdin)
print(sys.stdout)
print(sys.stdout)

sys.stdout.write("un test")
print(sys.stdout.write("nombre de caractere\n"))

fichier = open('stdout.txt', 'w')
sys.stdout = fichier
print("hellow world")

sys.stdout = sys.__stdout__
print(os.getcwd())

import signal

print(signal.SIGINT)

def ferme_program(signal , frame):
    """Fonction appelée quand vient l'heure de ferme notre programme"""
    print("c'est l'heure de la fermeture !")
    sys.exit(0)

signal.signal(signal.SIGINT, ferme_program)

print("le programme va boucle")
while True:
    continue