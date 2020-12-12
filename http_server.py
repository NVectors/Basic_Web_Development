import http.server
import socketserver
import os

#Define a port
PORT = 8080

web_dir = os.path.join(os.path.dirname(__file__), "HTML_CSS_JS")
os.chdir(web_dir)

# Make a simple HTTP request handler 
# that serves files from the current directory and any subdirectories
# TCPServer uses TCP protocol to send and receive messages
# Server instantiated with TCP address -> ((ANY IP,PORT), Request Handler)
HANDLER = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), HANDLER) as httpd:
    print("Serving at Port: ", PORT)
    httpd.serve_forever() #Start listening and responding to incoming requests

