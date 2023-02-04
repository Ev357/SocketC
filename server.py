import socket
import ssl

HOST = '0.0.0.0'
PORT = 12345

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='ssl/cert.pem', keyfile='ssl/key.pem')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        with context.wrap_socket(conn, server_side=True) as ssock:
            while True:
                data = ssock.recv(1024)
                if not data:
                    break
                ssock.sendall(data[::-1])
