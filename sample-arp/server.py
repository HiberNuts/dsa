import requests
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

PORT = 8090
ip_mac = {}
with open('data.json') as file:
    ip_mac = json.load(file)

class MyHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)  # 200 stands for request succeeded
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        print(self.path)
        if self.path == '/data':
            json_string = json.dumps(ip_mac)
            self.wfile.write(json_string.encode(encoding='utf_8'))


def run(server_class=HTTPServer, handler_class=MyHandler, addr="localhost", port=PORT):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread.start()
    url = f'http://localhost:{PORT}/data'
    request = requests.get(url)
    print(request.json())
