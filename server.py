import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 10000))
s.listen()
print("Socket listening on port 10000")

while True:
    client, addr = s.accept()
    print("Accepted connection from", addr)

    def receive_message():
        data = client.recv(1024).decode()
        if not data:
            return None
        print("Received message:", data)
        return data

    def send_message(message):
        client.send(message.encode())
        print("Sent message:", message)

    message = receive_message()
    send_message("Connected")

    while message:
        message = receive_message()

    client.close()
    print("Connection closed")
