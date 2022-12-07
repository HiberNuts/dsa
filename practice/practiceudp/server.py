from socket import *

server_name = '127.0.0.1'
server_port = 5000
addr = (server_name, server_port)

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind((server_name, server_port))

while True:
    sentence, addr = server_socket.recvfrom(2048)
    print(sentence.decode())
    message = input(">> ")
    server_socket.sendto(message.encode(), addr)


