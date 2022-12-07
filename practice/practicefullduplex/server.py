from socket import *
import time
import threading

server_name = '127.0.0.1'
server_port = 5000
addr = (server_name, server_port)

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((server_name, server_port))
server_socket.listen(1)
connection, address = server_socket.accept()

def getMessage():
    while True:
        sentence = connection.recv(2048)
        print(sentence.decode())
        time.sleep(0.5)

def sendMessage():
    while True:
        message = input(">> ")
        connection.send(message.encode())
        time.sleep(0.5)

thread1 = threading.Thread(target=getMessage)
thread1.start()
thread2 = threading.Thread(target=sendMessage)
thread2.start()