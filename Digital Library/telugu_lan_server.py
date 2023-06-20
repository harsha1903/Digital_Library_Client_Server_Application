import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('Localhost', 6667))
s.listen()
Thread_count=0

def telugu_lan_server(con):
    data = con.recv(1024).decode("utf-8")
    g=data
    gen=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    if g=='Horror' :
        gen.connect(('Localhost',6670))
        size=gen.recv(1024)
        con.send(size)
        con.sendall(gen.recv(int.from_bytes(size,'little')))
    elif g=='Detective':
        gen.connect(('Localhost',6671))
        size=gen.recv(1024)
        con.send(size)
        con.sendall(gen.recv(int.from_bytes(size,'little')))
    elif g=='Technical':
        gen.connect(('Localhost',6672))
        size=gen.recv(1024)
        con.send(size)        
        con.sendall(gen.recv(int.from_bytes(size,'little')))
    else:
        data='Invalid'
        size=len(data.encode('utf-8'))
        con.send(str(size).encode('utf-8'))
        con.send(data.encode('utf-8'))
    gen.close()
    con.close()

while True:
    con, addr = s.accept()
    Thread_count+=1
    print('Client',Thread_count,'connected\n')
    thread =threading.Thread(target=telugu_lan_server, args=(con,))
    thread.start()
s.close()
