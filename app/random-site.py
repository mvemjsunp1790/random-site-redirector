from http.server import HTTPServer, BaseHTTPRequestHandler
import random
import os

sitelist=os.getenv('SITES').split(',')
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        randomSite = random.choice(sitelist)
        self.send_response(307)
        new_path = '%s%s'%(randomSite, self.path)
        self.send_header('Location', new_path)
        self.end_headers()


httpd = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
