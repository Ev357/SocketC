import socket

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 10000

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

print("Server listening on port", port)

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from", addr)
    data = clientsocket.recv(1024).decode("utf-8")
    print("Received data: ", data)

    # send a HTTP response to the client
    http_response = "HTTP/1.1 200 OK\n\nHello from the server!"
    clientsocket.sendall(http_response.encode("utf-8"))

    clientsocket.close()
