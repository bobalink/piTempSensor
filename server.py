#!/usr/bin/python
# from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer



from http.server import HTTPServer, BaseHTTPRequestHandler


PORT_NUMBER = 8080

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')


httpd = HTTPServer(('localhost', PORT_NUMBER), SimpleHTTPRequestHandler)
httpd.serve_forever()
