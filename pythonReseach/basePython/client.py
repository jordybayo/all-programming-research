#coding:utf-8

import socket

hote = '192.168.56.1'
port = 12800


connexion_avec_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connexion_avec_server.connect((hote,port))
print("connexion etablite avec le port {}".format(port))

msg_a_envoyer = b""

while (msg_a_envoyer  != 'fin'):
    msg_a_envoyer = input("$msg> ")
    msg_a_envoyer = msg_a_envoyer.encode()
    connexion_avec_server.send(msg_a_envoyer)
    msg_recu = connexion_avec_server.recv(1024)
    print(msg_recu.decode())
    msg_a_envoyer = msg_a_envoyer.decode()


connexion_avec_server.close()
print("fermeture de la connexion avec le serveur ...")


