from socket import *
import time
import threading

server_name = '127.0.0.1'
server_port = 5000
addr = (server_name, server_port)

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.connect((server_name, server_port))


def getMessage():
    while True:
        sentence = server_socket.recv(2048)
        print(sentence.decode())
        time.sleep(0.5)

def sendMessage():
    while True:
        message = input(">> ")
        server_socket.send(message.encode())
        time.sleep(0.5)

thread1 = threading.Thread(target=sendMessage)
thread1.start()
thread2 = threading.Thread(target=getMessage)
thread2.start()