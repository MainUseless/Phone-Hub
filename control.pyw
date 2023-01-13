from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
from notifypy import Notify
import os

def notify(mess):
    notification = Notify()
    notification.title = "Cool Title"
    notification.message = mess
    notification.send()

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        result = json.loads(post_data.decode('utf-8'))
        print(result)
        
        if(result['command']=="/test"):
            notify("testing")
            
        elif (result['command']=='/kill'):
            notify('remotely shutting down')
            os.system("shutdown /s /t 10")
        
        elif (result['command']=='/sleep'):
            notify("Remotely hibernating")
            os.system("shutdown /h")
        
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=12000):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        notify(f"Server ON : Port {port}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()