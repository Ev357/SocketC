import socket

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# specify the IP address of the server
host = "localhost"                           

port = 10000

# connection to hostname on the port.
clientsocket.connect((host, port))                               

# send a HTTP request to the server
http_request = "GET / HTTP/1.1\nHost: " + host + "\n\n"
clientsocket.sendall(http_request.encode("utf-8"))

# receive data from the server
data = clientsocket.recv(1024).decode("utf-8")
print("Received data: ", data)

clientsocket.close()
