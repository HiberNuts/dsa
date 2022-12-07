from socket import *

server_name  ='127.0.0.1'
server_port = 5000

server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind((server_name, server_port))

server_socket.listen(1)

connection, address = server_socket.accept()

while True:
    sentence = connection.recv(2048)
    connection.send(sentence)
