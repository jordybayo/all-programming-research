import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'localhost'

def pscan(port):
    try:
        s.connect((server, port))
        return True
    except:
        return False


for x in range(70,105):
    if pscan(x):
        print('le port',x,'est ouvert..')
    else:
        print('le port',x,'est fermer')