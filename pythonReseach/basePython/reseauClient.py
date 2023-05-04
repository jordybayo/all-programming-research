import socket

#creation du client

connexion_avec_serveur = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

#connecter le  client

connexion_avec_serveur.connect(('localhost',12806))


#faire commmuniquer nos sockets

msg_recu = connexion_avec_serveur.recv(1024)
print(msg_recu)

#fermer la connectin
connexion_avec_serveur.close()
