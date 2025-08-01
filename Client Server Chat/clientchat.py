import socket

# Connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 65432))

# Start the chat loop
while True:
    # Send message to server
    message = input("Client message to server: ")
    client_socket.sendall(message.encode())
    if message.lower() == "exit":
        break

    # Receive reply from server
    reply = client_socket.recv(1024).decode()
    if reply.lower() == "exit":
        print("Server has exited the chat.")
        break
    print("Server:", reply)

# Close connection
client_socket.close()
print("Chat Closed.")
