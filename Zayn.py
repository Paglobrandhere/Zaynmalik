python
from http.server important baseHTTPRequestHandler,HTTPServer

class simpleHTTPRequestHandler(BaseHTTPRequestHandler):
     def do_GET(self):
         self.send_response(200)
         self.send_header('Content-type', 'text/html')
         self.send_headers()
         self.wlife.write(b 'Hello, Welcome to the offline server!')
         
         
         def run(server_class=HTTPServer,
         handler_class=SimpleHTTPRequestHandler,
         port=8000):
           server_address = ( '', port)
           httpd = server_class(server_address,handler_class)
           print(f'Starting on port {port}...')
           httpd.serve_forever()
           
      if __name__== ' __main__':
         run()
