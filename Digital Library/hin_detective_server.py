import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('Localhost', 6674))
s.listen()
Thread_count=0
def hin_detective_server(con):
    data='''
1."Kanoon Ka Devta" by Dharamvir Bharati
2."Ek Tha Rusty" by Ruskin Bond
3."Gumshuda Qatil" by Surendra Mohan Pathak
4."Nirbhay" by Vishnu Prabhakar
5."Bhagya Ke Badalte Rishte" by Gulshan Nanda
6."Vardi Wala Gunda" by Ved Prakash Sharma
7."Saat Saal Baad" by Surender Mohan Pathak
8."Adhura Adhura Ujala" by Surender Mohan Pathak
9."Sone Ki Chidiya" by Gulshan Nanda
10."Khunkhwar" by Surender Mohan Pathak'''
    con.send(str(len(data.encode('utf-8'))).encode())
    con.send(data.encode('utf-8'))
    con.close()

while True:
    con, addr = s.accept()
    Thread_count+=1
    print('Client',Thread_count,'connected\n')
    thread =threading.Thread(target=hin_detective_server, args=(con,))
    thread.start()
s.close()
