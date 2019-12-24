from random import randint
import socket
import pickle

HOST = '127.0.0.1'
PORT = 8071

sock = socket.socket()
sock.connect((HOST, PORT))

p, g = 7, 5
a = randint(0,9)
A = g ** a % p
sock.send(pickle.dumps((p, g, A)))
msg = sock.recv(1024)
B = pickle.loads(msg)

K= B**a % p
print(K)
str2=[]
str1=str(input('Enter frase:'))
str3=[]
for s in str1:
    a=ord(s)
    str2.append(a+K)
for s in str2:
	a=chr(s)
	str3.append(a)
str4 =str(str3)
print(str4)
sock.send(pickle.dumps(str4))
sock.close()
