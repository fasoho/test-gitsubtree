#!/usr/bin/env python

import textwrap

from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class HelloRequestHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    if self.path != '/':
      self.send_error(404, "Object Not Found")
      return
    self.send_response(200)
    self.send_header('Content-type', 'text/html; charset=utf-8')
    self.end_headers()
    response_text = textwrap.dedent('''\
      <!DOCTYPE html>
      <head>
        <title>Hello World</title>
      </head>
      <body>
        <h2>Hello World</h2>
      </body>
      </html>
    ''')
    self.wfile.write(response_text.encode('utf-8'))

server_address = ('', 8000)
http = HTTPServer(server_address, HelloRequestHandler)
http.serve_forever()