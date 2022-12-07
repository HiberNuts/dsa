
import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 8000))
print("waiting for date-time from server")
data = c.recv(1024).decode('utf-8')
print("date-time from server:")
print(data)
c.close()