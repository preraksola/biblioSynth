#!/usr/bin/env python

import BaseHTTPServer
import CGIHTTPServer 
import cgitb
cgitb.enable() # for debuging


server = BaseHTTPServer.HTTPServer #server class
handler = CGIHTTPServer.CGIHTTPRequestHandler #handler class for running CGI scripts
server_address = ("", 8000) #(server name, server port)
handler.cgi_directories = ["/"] #directories to serve CGI script

httpd = server(server_address, handler)
httpd.serve_forever()
