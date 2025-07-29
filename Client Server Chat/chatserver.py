import socket

# Setup server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 65432))
server_socket.listen(1)

print("Chat server is waiting for a connection on port 65432...")

# Accept client connection
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

# Start the chat loop
while True:
    # Receive message from client
    client_msg = client_socket.recv(1024).decode()
    if client_msg.lower() == "exit":
        print("Client has exited the chat.")
        break
    print("Client:", client_msg)

    # Send message to client
    server_msg = input("Server message to client: ")
    client_socket.sendall(server_msg.encode())
    if server_msg.lower() == "exit":
        break

# Close connections
client_socket.close()
server_socket.close()
print("Chat closed.")
