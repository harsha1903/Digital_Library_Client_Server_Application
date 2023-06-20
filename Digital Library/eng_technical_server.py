import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('Localhost', 6678))
s.listen()
Thread_count=0
def eng_technical_server(con):
    data='''
1."The C Programming Language" by Brian Kernighan and Dennis Ritchie
2."Clean Code: A Handbook of Agile Software Craftsmanship" by Robert C. Martin
3."Design Patterns: Elements of Reusable Object-Oriented Software" by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides
4."Code Complete: A Practical Handbook of Software Construction" by Steve McConnell
5."Structure and Interpretation of Computer Programs" by Harold Abelson and Gerald Jay Sussman
6."Cracking the Coding Interview: 189 Programming Questions and Solutions" by Gayle Laakmann McDowell
7."The Art of Computer Programming" by Donald Knuth
8."Clean Architecture: A Craftsman's Guide to Software Structure and Design" by Robert C. Martin
9."Introduction to Algorithms" by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein
10."Head First Design Patterns" by Eric Freeman and Elisabeth Robson'''
    con.send(str(len(data.encode('utf-8'))).encode())
    con.send(data.encode('utf-8'))
    con.close()

while True:
    con, addr = s.accept()
    Thread_count+=1
    print('Client',Thread_count,'connected\n')
    thread =threading.Thread(target=eng_technical_server, args=(con,))
    thread.start()
s.close()
