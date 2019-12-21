#!/usr/bin/python3
import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
serversocket.bind((host, port))
serversocket.listen(5)                                          
clientsocket,addr = serversocket.accept()

g = 7
p = 23
print("g = 7, p = 23 (These values are public.)")
x = int(input("Enter x: "))
R1 = (g**x)%p
clientsocket.send(str(R1).encode())

R2 = clientsocket.recv(1024) 
R2 = int(R2.decode())
print("Received: R2 =",R2)
K = (R2**x)%p
print("Shared secret key: K =",K)
clientsocket.close()
serversocket.close()

