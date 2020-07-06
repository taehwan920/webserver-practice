import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler
PORT = 8080

with socketserver.TCPServer(('', PORT), handler) as httpd:
    print(f'Server listening on port {PORT}...')
    httpd.serve_forever()
