import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


IP_ADDRESS='127.0.0.1'
PORT=8050
SERVER=None
Buffer_size=8090
clients={}


def musicWindow():
    window=Tk()
    window.title("Music window")
    window.geometry("300 x 300")
    window.configure(bg="green")







    namelabel = Label(window, text= "select your song", font = ("Calibri",10))
    namelabel.place(x=10, y=8)

    

    listbox = Listbox(window,height = 5,width = 67,activestyle = 'dotbox', font = ("Calibri",10))
    listbox.place(x=10, y=70)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playtButton=Button(window,text="play",bd=1, font = ("Calibri",10))
    playtButton.place(x=282,y=160)

   
    stopButton=Button(window,text="stop",bd=1, font = ("Calibri",10))
    stopButton.place(x=350,y=160)

    uploadButton=Button(window,text="Upload",bd=1, font = ("Calibri",10))
    uploadButton.place(x=282,y=160)

   
    downloadButton=Button(window,text="Download",bd=1, font = ("Calibri",10))
    downloadButton.place(x=350,y=160)
 
 

    window.mainloop()

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
    musicWindow()
    setup_threads=Thread(target=setup)
    setup_threads.start()
    

