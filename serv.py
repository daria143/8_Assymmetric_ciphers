import socket
import pickle
from random import randint

HOST = '127.0.0.1'
PORT = 8071

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

msg = conn.recv(1024)
p, g, A = pickle.loads(msg)
b = randint(0,9)
B = g ** b % p

conn.send(pickle.dumps(B))

K = A ** b % p
print(K)
msg2 = conn.recv(1024)
str1 = pickle.loads(msg2)
print(str1)
str2=[]#chisla
str3=[]#word

for s in str1:
    a=ord(s)
    if (a)!=32 and (a)!=ord('[') and a !=ord("'") and (a)!=ord(']') and (a)!=ord(','):
	    str2.append(a)
#print(str2)

for s in str2:
    a=s-K
    a1=chr(a)
    str3.append(a1)
print(''.join(str3))


conn.close()
