import socket 

socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket_server.bind(('localhost',54321))
socket_server.listen(1)
print(f"Echo server is runnung on port:{54321}...")

client_socket, client_address = socket_server.accept()
print(f"connection from{client_address} establised!")

while True:
    data = client_socket.recv(1024).decode()

    if not data:
        break

    print("client said", data)
    if data.lower() == "exit":
        client_socket.sendall("GoodBye".encode())
        break

    client_socket.sendall(data.encode())

client_socket.close()
socket_server.close()

