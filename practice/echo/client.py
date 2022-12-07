from socket import *

server_name  ='127.0.0.1'
server_port = 5000

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

while True:
    message = input(">> ")
    client_socket.send(message.encode())
    sentence = client_socket.recv(2048)
    print(sentence.decode())