import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('Localhost', 6672))
s.listen()
Thread_count=0
def tel_technical_server(con):
    data='''
1."Computer Graphics" by Uma Kanth
2."Database Management Systems" by Raghu Ramakrishnan and Johannes Gehrke (translated into Telugu)
3."Data Structures and Algorithms in C++" by Michael T. Goodrich and Roberto Tamassia (translated into Telugu)
4."Object-Oriented Programming with C++" by Balagurusamy (translated into Telugu)
5."Digital Electronics" by S. Salivahanan and S. Arivazhagan (translated into Telugu)
6."Operating System Concepts" by Abraham Silberschatz, Peter B. Galvin, and Greg Gagne (translated into Telugu)
7."Software Engineering" by Ian Sommerville (translated into Telugu)
8."Computer Organization and Architecture" by William Stallings (translated into Telugu)
9."Programming in ANSI C" by E. Balagurusamy (translated into Telugu)
10."Java: The Complete Reference" by Herbert Schildt (translated into Telugu)'''
    con.send(str(len(data.encode('utf-8'))).encode())
    con.send(data.encode('utf-8'))
    con.close()

while True:
    con, addr = s.accept()
    Thread_count+=1
    print('Client',Thread_count,'connected\n')
    thread =threading.Thread(target=tel_technical_server, args=(con,))
    thread.start()
s.close()
