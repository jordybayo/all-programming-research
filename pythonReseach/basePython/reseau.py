import socket


#creation du seveur
connexion_principal = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
connexion_principal.bind(('',12806))
connexion_principal.listen(5)
connexion_avec_client , info_connexion = connexion_principal.accept()
print("parametre de conn:" + str(connexion_avec_client))

#faire communiquer nos sockets
socket.getsockname = ('127.0.1.1', 12806)
conn = socket.socket(socket.AF_INET , socket.SOCK_STREAM, 0)
print("parametre de family:" + str(conn.family))
print("parametre de type:" + str(conn.type))
print("parametre de proto:" + str(conn.proto))
print("parametre de fileno:" + str(conn.fileno()))
print("parametre de laddr:" + str(conn.getsockname()))
print("parametre de raddr:" + str(conn.getpeername()))
connexion_avec_client.send(b"je viens d'accepter la connexion")

#fermer la connexion
connexion_avec_client.close()
