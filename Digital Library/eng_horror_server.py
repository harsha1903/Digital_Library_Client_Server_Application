import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('Localhost', 6676))
s.listen()
Thread_count=0
def eng_horror_server(con):
    data='''
1."Dracula" by Bram Stoker
2."Frankenstein" by Mary Shelley
3."The Shining" by Stephen King
4."The Exorcist" by William Peter Blatty
5."The Silence of the Lambs" by Thomas Harris
6."Interview with the Vampire" by Anne Rice
7."The Haunting of Hill House" by Shirley Jackson
8."Carrie" by Stephen King
9."The Strange Case of Dr. Jekyll and Mr. Hyde" by Robert Louis Stevenson
10."Pet Sematary" by Stephen King'''
    con.send(str(len(data.encode('utf-8'))).encode())
    con.send(data.encode('utf-8'))
    con.close()

while True:
    con, addr = s.accept()
    Thread_count+=1
    print('Client',Thread_count,'connected\n')
    thread =threading.Thread(target=eng_horror_server, args=(con,))
    thread.start()
s.close()
