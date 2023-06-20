import socket
import os
import sys
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('Localhost',6666))
print('Server Connetced')
Language=input('Enter the Language of the books within the options:\n1. Telugu\n2. Hindi\n3. English\n')
Genre=input('\nEnter the Genres of the books within the options:\n1. Horror\n2. Detective\n3. Technical\n')
data=Language+','+Genre

s.send(data.encode("utf-8"))
size=s.recv(1024)
received=s.recv(int.from_bytes(size,'little')).decode('utf-8')
if received=='Invalid':
    print('\nInvalid Inputs Please Try Again')
else :
    print('\nThe list of '+Language+' '+Genre+' books are:'+received)
s.close()
