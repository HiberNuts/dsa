
import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8000))
print("server waiting for message to receive")
data, addr = s.recvfrom(1024)
print("received message:")
print(data.decode('utf-8'))
