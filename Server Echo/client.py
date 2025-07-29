
import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 54321))

while True:
    message = input("you: ")
    client_socket.sendall(message.encode())

    reply = client_socket.recv(1024).decode()

    print("server: ",reply)

    if message.lower() == "exit":
        break

    
client_socket.close()
