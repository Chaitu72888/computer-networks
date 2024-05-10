'''import socket

# Define the host and port to bind to
HOST = '127.0.0.1'
PORT = 12345

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    # Bind the socket to the address and port
    server_socket.bind((HOST, PORT))
    
    print(f"Server is listening on {HOST}:{PORT}")
    
    while True:
        # Receive data from the client
        data, client_address = server_socket.recvfrom(1024)
        print(f"Received from {client_address}: {data.decode()}")
        
        # Echo back the received data to the client
        server_socket.sendto(data, client_address)'''


import socket

# Define the server address and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    # Send data to the server
    message = "Hello, server!"
    client_socket.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))
    
    # Receive data from the server
    received_data, server_address = client_socket.recvfrom(1024)
    print("Received from server:", received_data.decode())

