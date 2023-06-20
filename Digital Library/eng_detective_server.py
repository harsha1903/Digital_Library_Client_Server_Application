import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('Localhost', 6677))
s.listen()
Thread_count=0
def eng_detective_server(con):
    data='''
1."The Adventures of Sherlock Holmes" by Arthur Conan Doyle
2."The Girl with the Dragon Tattoo" by Stieg Larsson
3."The Cuckoo's Calling" by Robert Galbraith (pseudonym of J.K. Rowling)
4."The Silence of the Lambs" by Thomas Harris
5."The Murder of Roger Ackroyd" by Agatha Christie
6."The Big Sleep" by Raymond Chandler
7."The Maltese Falcon" by Dashiell Hammett
8."The No. 1 Ladies' Detective Agency" by Alexander McCall Smith
9."In the Woods" by Tana French
10."The Moonstone" by Wilkie Collins'''
    con.send(str(len(data.encode('utf-8'))).encode())
    con.send(data.encode('utf-8'))
    con.close()

while True:
    con, addr = s.accept()
    Thread_count+=1
    print('Client',Thread_count,'connected\n')
    thread =threading.Thread(target=eng_detective_server, args=(con,))
    thread.start()
s.close()
