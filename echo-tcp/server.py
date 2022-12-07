
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8000))
s.listen(1)
print("waiting for client")
conn, addr = s.accept()
print("connected successfully at", addr)
data = conn.recv(1024)
print("received:", data.decode('utf-8'))
conn.sendall(data)
conn.close()
