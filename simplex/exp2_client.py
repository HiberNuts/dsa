
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto('DCN lab'.encode('utf-8'), ('127.0.0.1', 8000))
print("message has been sent from client")