  #codding:utf-8

import http.server
# import socketserver

port=80
address=("", port)


server=http.server.HTTPServer

#handler=http.server.SimpleHTTPRequestHandler
#httpd=socketserver.TCPServer(address, handler)

handler=http.server.CGIHTTPRequestHandler
handler.cgi_directories=["/"]
httpd=server(address, handler)

print(f"serveur demarré sur le port{port}")

httpd.serve_forever()

