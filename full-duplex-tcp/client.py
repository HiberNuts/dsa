import socket
import time
import threading

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',1400))

def getmsg():
    while True:
        msg=client.recv(1000).decode('utf-8')
        print('Server: ',msg)
        time.sleep(0.5)

def sendmsg():
    while True:
        msg=input("")
        client.sendall(msg.encode())
        time.sleep(0.5)
        if msg=='bye':
            break

     
thread1= threading.Thread(target=sendmsg)
thread1.start()

thread2=threading.Thread(target=getmsg)
thread2.start()
