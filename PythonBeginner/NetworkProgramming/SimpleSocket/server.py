#server.py
import socket
import time

#create socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get local machine name
host = socket.gethostname()

port = 9999

#bind to the port
serverSocket.bind((host, port))

#queue up to five request
serverSocket.listen(5)

while True:
    #establish a connection
    clientsocket, address = serverSocket.accept()

    print("got a connection  fron %s" % str(address))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
