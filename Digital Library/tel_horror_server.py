import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('Localhost', 6670))
s.listen()
Thread_count=0

def tel_horror_server(con):
    data='''
1."Rudraveena" by Sri Sri
2."Adivi Biddalu" by Yandamoori Veerendranath
3."Daiva Bhayam" by Madhu Babu
4."Cheekati Rajyam" by Yandamoori Veerendranath
5."Asathoma Sadgamaya" by Malladi Venkata Krishnamurthy
6."Nigraham" by Devipriya
7."Maha Prachandudu" by Yandamoori Veerendranath
8."Tulasidalam" by Yandamoori Veerendranath
9."Kona Hrudayam" by Madhu Babu
10."Bhramaravasu" by Yandamoori Veerendranath'''
    con.send(str(len(data.encode('utf-8'))).encode())
    con.send(data.encode('utf-8'))
    con.close()

while True:
    con, addr = s.accept()
    Thread_count+=1
    print('Client',Thread_count,'connected\n')
    thread =threading.Thread(target=tel_horror_server, args=(con,))
    thread.start()
s.close()
