#!/usr/bin/env python3
"""
3. Develop a simple API using Python with the `http.server` module
"""
import http.server
import json


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    A request handler class that inherits from BaseHTTPRequestHandler.
    It defines the behavior for GET requests.
    """

    def do_GET(self):
        """
        Handles GET requests based on the path.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run(server_class=http.server.HTTPServer,
        handler_class=SimpleHTTPRequestHandler):
    """
    Starts the HTTP server on port 8000.
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Serving at port 8000")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
