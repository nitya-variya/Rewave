import http.server
import socketserver
import os

PORT = 8089
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

class ThreadingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == '__main__':
    with ThreadingServer(('127.0.0.1', PORT), Handler) as httpd:
        print(f"Serving HTTP on 127.0.0.1:{PORT} from {DIRECTORY}")
        httpd.serve_forever()

