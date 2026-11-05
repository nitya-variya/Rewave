import http.server
import socketserver
import os
import sys

# Ensure stdout and stderr are valid streams even in GUI / detached mode (e.g. pythonw or WindowStyle Hidden)
if sys.stderr is None:
    sys.stderr = open(os.devnull, 'w')
if sys.stdout is None:
    sys.stdout = open(os.devnull, 'w')

PORT = 8089
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, format, *args):
        try:
            if sys.stderr:
                super().log_message(format, *args)
        except Exception:
            pass

class ThreadingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == '__main__':
    with ThreadingServer(('127.0.0.1', PORT), Handler) as httpd:
        try:
            print(f"Serving HTTP on 127.0.0.1:{PORT} from {DIRECTORY}")
        except Exception:
            pass
        httpd.serve_forever()
