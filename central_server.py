import socket
import threading
import sys
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('Localhost', 6666))
s.listen()
Thread_count=0
def central_server(con):
    data = con.recv(1024).decode('utf-8')
    l=data.split(',',2)
    lan=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if l[0]=='Telugu' :
        lan.connect(('Localhost',6667))
        lan.send(l[1].encode('utf-8'))
        size=lan.recv(1024)
        con.send(size)
        con.send(lan.recv(int.from_bytes(size,'little')))
    elif l[0]=='Hindi':
        lan.connect(('Localhost',6668))
        lan.send(l[1].encode('utf-8'))
        size=lan.recv(1024)
        con.send(size)
        con.send(lan.recv(int.from_bytes(size,'little')))
    elif l[0]=='English':
        lan.connect(('Localhost',6669))
        lan.send(l[1].encode('utf-8'))
        size=lan.recv(1024)
        con.send(size)
        con.send(lan.recv(int.from_bytes(size,'little')))
    else:
        data='Invalid'
        size=len(data.encode('utf-8'))
        con.send(str(size).encode('utf-8'))
        con.send(data.encode('utf-8'))
    lan.close()
    con.close()
while True:
    con, addr = s.accept()
    Thread_count+=1
    print('Client',Thread_count,'connected\n')
    thread =threading.Thread(target=central_server, args=(con,))
    thread.start()
s.close()
