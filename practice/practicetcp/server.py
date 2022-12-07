from socket import *

server_name = '127.0.0.1'
server_port = 5000
addr = (server_name, server_port)

# STEP 1: SOCKET
# STEP 2: BIND
# STEP 3: LISTEN
# STEP 4: ACCEPT

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((server_name, server_port))
server_socket.listen(1)
connection, address = server_socket.accept()

while True:
    sentence = connection.recv(2048)
    print(sentence.decode())
    message = input(">> ")
    connection.send(message.encode())


