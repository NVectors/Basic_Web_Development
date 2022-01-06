import http.server
import socketserver

#Define a port
PORT = 8080

# Make a simple HTTP request handler 
# that serves files from the current directory and any subdirectories
# TCPServer uses TCP protocol to send and receive messages
# Server instantiated with TCP address -> ((ANY IP,PORT), Request Handler)
HANDLER = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), HANDLER) as httpd:
    print("Serving at Port: ", PORT)
    httpd.serve_forever() #Start listening and responding to incoming requests

