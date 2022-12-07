from socket import *

server_name = '127.0.0.1'
server_port = 5000
addr = (server_name, server_port)


client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.connect((server_name, server_port))

while True:
    message = input(">> ")
    client_socket.sendto(message.encode(), addr)
    sentence = client_socket.recvfrom(2048)
    print(sentence[0].decode())