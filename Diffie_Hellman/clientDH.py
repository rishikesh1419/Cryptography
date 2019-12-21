#!/usr/bin/python3
import socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
clientsocket.connect((host, port))

g = 7
p = 23
print("g = 7, p = 23 (These values are public.)")
y = int(input("Enter y: "))
R2 = (g**y)%p
clientsocket.send(str(R2).encode())

R1 = clientsocket.recv(1024)
R1 = int(R1.decode())
print("Received: R1 =",R1)
K = (R1**y)%p
print("Shared secret key: K =",K)
clientsocket.close()

