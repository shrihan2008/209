import socket
from threading import Thread

IP_ADDRESS='127.0.0.1'
PORT=8050
SERVER=None
Buffer_size=8090
clients={}

def acceptConnections(client,addr):
    global SERVER
    global clients

    while True:
        client,addr=SERVER.accept()
        print(client.addr)

def setup():
    print("\n\n\n\n\n\n\t Messenger \n")
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))

    SERVER.listen(100)

    print("watiting for connections")

    acceptConnections()

    setup_threads=Thread(target=setup)
    setup_threads.start()
    