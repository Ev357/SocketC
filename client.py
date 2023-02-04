import socket
import ssl

HOST = 'socketc.onrender.com'
PORT = 443

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with context.wrap_socket(s, server_hostname=HOST) as ssock:
        while True:
            message = input('Enter your message: ')
            ssock.sendall(message.encode())
            data = ssock.recv(1024)
            print('Received', repr(data.decode()))
            if message == 'close':
                break
