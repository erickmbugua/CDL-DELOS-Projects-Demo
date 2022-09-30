import socket
import os

def client():
    SRV = os.getenv('SERVER_ADDRESS')
    PORT = int(os.getenv('SERVER_PORT'))

    client_socket = socket.socket()
    client_socket.connect((SRV, PORT))

    message = "hello world"
    
    while True:
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        if data.lower() == "bye":
            break
        print(data)
    client_socket.close()

if __name__ == "__main__":
    client()