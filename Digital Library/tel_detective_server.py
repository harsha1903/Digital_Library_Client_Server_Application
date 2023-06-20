import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('Localhost', 6671))
s.listen()
Thread_count=0
def tel_detective_server(con):
    data='''
1."Naa Istam" by Ram Gopal Varma
2."Sudheer" by Yandamoori Veerendranath
3."CID Jagannadham" by Madhu Babu
4."Swarnakhadgam" by Yandamoori Veerendranath
5."Jayam Manadera" by Malladi Venkata Krishnamurthy
6."Drohi" by Yandamoori Veerendranath
7."Gudachari 116" by Malladi Venkata Krishnamurthy
8."Vennello Aadapilla" by Yandamoori Veerendranath
9."Superintendent of Police" by Madhu Babu
10."Chivaraku Migiledi" by Buchi Babu'''
    con.send(str(len(data.encode('utf-8'))).encode())
    con.send(data.encode('utf-8'))
    con.close()

while True:
    con, addr = s.accept()
    Thread_count+=1
    print('Client',Thread_count,'connected\n')
    thread =threading.Thread(target=tel_detective_server, args=(con,))
    thread.start()
s.close()
