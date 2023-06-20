import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('Localhost', 6675))
s.listen()
Thread_count=0
def hin_technical_server(con):
    data='''
1."Java: A Beginner's Guide" by Herbert Schildt
2."Python Crash Course" by Eric Matthes
3."Data Structures and Algorithms" by Narasimha Karumanchi (translated into Hindi)
4."Computer Networks" by Andrew S. Tanenbaum
5."Head First Design Patterns" by Eric Freeman and Elisabeth Robson
6."Artificial Intelligence: A Modern Approach" by Stuart Russell and Peter Norvig (translated into Hindi)
7."Computer System Architecture" by M. Morris Mano
8."C Programming Language" by Brian W. Kernighan and Dennis M. Ritchie (translated into Hindi)
9."The Pragmatic Programmer: From Journeyman to Master" by Andrew Hunt and David Thomas
10."Operating System Concepts" by Abraham Silberschatz, Peter B. Galvin, and Greg Gagne'''
    con.send(str(len(data.encode('utf-8'))).encode())
    con.send(data.encode('utf-8'))
    con.close()

while True:
    con, addr = s.accept()
    Thread_count+=1
    print('Client',Thread_count,'connected\n')
    thread =threading.Thread(target=hin_technical_server, args=(con,))
    thread.start()
s.close()
