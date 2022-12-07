
import socket 
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 8000))
msg = input("enter message to send to server: ")
c.sendall(msg.encode('utf-8'))

data = c.recv(1024)
print("echoed message: ", data.decode('utf-8'))
c.close()