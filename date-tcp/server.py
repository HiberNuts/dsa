
import socket
from datetime import datetime
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8000))
s.listen(1)
print("waiting for client")
conn, addr = s.accept()
print("connected to client at", addr)

data = datetime.now()
print(data)
print("sending date-time to client")
conn.sendall(str(data).encode('utf-8'))
conn.close()
s.close()

