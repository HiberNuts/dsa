from socket import *
from socketserver import *
from http.server import *

handle = SimpleHTTPRequestHandler
http = TCPServer(("",5000),handle)
http.serve_forever()

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.connect(('127.0.0.1', 5000))

server_socket.sendall('GET/HTTP/1.1 \r\n HOST:http://127.0.0.1:5000 \r\n\r\n')