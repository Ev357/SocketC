import socket

HOST = 'socketc.onrender.com'
PORT = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input('Enter your message: ')
        s.sendall(message.encode())
        data = s.recv(1024)
        print('Received', repr(data.decode()))
        if message == 'close':
            break
