#client,py
import socket

#create local socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get local
host = socket.gethostname()

port = 9999

#connection to hostname on the port
s.connect((host, port))

tm = s.recv(1024)

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))
