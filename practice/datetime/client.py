from socket import *
from datetime import datetime
import time

server_name = '127.0.0.1'
server_port = 5000

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.connect((server_name, server_port))

while True:
    sentence = server_socket.recv(2048)
    print(sentence.decode())
    time.sleep(1)