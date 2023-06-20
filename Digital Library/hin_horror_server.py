import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('Localhost', 6673))
s.listen()
Thread_count=0
def hin_horror_server(con):
    data='''
1."Dayan" by Premchand
2."Darwaza" by Surendra Mohan Pathak
3."Kya Koi Itna Chahne Laga Hai" by Manoj Kumar Mohanty
4."Bhoot Bhavish Bartaman" by Surendra Mohan Pathak
5."Pret Khooni" by Ved Prakash Sharma
6."Beeswin Sadi Ki Shaitani Kahaniyan" by Surender Mohan Pathak
7."Raat Pashmine Ki" by Gulshan Nanda
8."Khooni Darwaza" by Surender Mohan Pathak
9."Agyaat" by Dr. Anand Saxena
10."Chehre Ke Peeche" by Dinesh Singh'''
    con.send(str(len(data.encode('utf-8'))).encode())
    con.send(data.encode('utf-8'))
    con.close()

while True:
    con, addr = s.accept()
    Thread_count+=1
    print('Client',Thread_count,'connected\n')
    thread =threading.Thread(target=hin_horror_server, args=(con,))
    thread.start()
s.close()
