import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('0.0.0.0', 10000))
print("Connected to server")

def send_message(message):
    s.send(message.encode())
    print("Sent message:", message)

def receive_message():
    data = s.recv(1024).decode()
    print("Received message:", data)
    return data

send_message("Hello Server")
response = receive_message()

while True:
    message = input("Enter message to send (type 'exit' to quit): ")
    if message == "exit":
        break
    send_message(message)
    response = receive_message()

s.close()
print("Connection closed")
