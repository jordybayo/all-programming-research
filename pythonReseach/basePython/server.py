#coding:utf-8

import socket
import select
import os

ip='192.168.43.55'
os.system('networksetup -setmanualvi thdhcprouter vi-fi'+ip)
os.system('networksetup -setmanualwi thdhcprouter wi-fi 192.168.15.33')


hote = ''#addressClient
port = 12800

connexion_principal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principal.bind((hote,port))
connexion_principal.listen(5)
print("le server ecoute a present sur le port {}".format(port))

serveur_lance = True
clients_connectes = []
while serveur_lance:
    """on 
    va verifie que nouveau clients ne demandent pas  à  se connecter;
    pour cela on ecoute mla connexion_principale en lecture;
    on attend maxi 50ms
    """
    connexion_demandees, wlist, xlist=  select.select([connexion_principal], [] , [] , 0.05)
    for connexion in connexion_demandees:
        connexion_avec_client,info_connexion = connexion.accept()
        clients_connectes.append(connexion_avec_client)
        """
        Maintenant , on ecoute par select sont ceux devant ettre lus(recv)
        on attend laa encore 50ms maximum
        on enferme l'appel a select.select dans un bloc try
        En effet, si la liste de clients connecetéss est vide , une exception
        peut etre levée
        """

        client_a_lire = []
    try:
        client_a_lire, wlist, xlist = select.select(clients_connectes, [] , [] , 0.05)
    except select.error:
        pass
    else:
        #on parcourt la liste des clients à lire
        for client in client_a_lire:
            #peut planter si le message contient des caaractères spéciaux
            msg_recu = client.recv(1024)
            msg_recu = msg_recu.decode()
            print("Recu {}".format(msg_recu))
            client.send(b"msg recu 5/5")
            if msg_recu == "fin":
                serveur_lance  = False

print("fermeture des connexions")
for client in clients_connectes:
    client.close()
connexion_principal.close()


