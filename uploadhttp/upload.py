import socket
import http.server
import socketserver
handle=http.server.SimpleHTTPRequestHandler
http=socketserver.TCPServer(("",8080),handle)
print('Server started at port ',8080)
http.serve_forever()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8080))
s.sendall('GET/HTTP/1.1 \r\n HOST:http://127.0.0.1:8080/index.html \r\n\r\n')
