import socket

# Set up the client socket
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # The same port as the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Send commands and receive responses
    while True:
        # Send a command to the server
        command = "hello"
        s.sendall(command.encode('utf-8'))

        # Receive and print the response
        data = s.recv(1024)
        response = data.decode('utf-8').strip()
        print(f"Server response: {response}")

        # Exit the loop if the 'exit' command is sent
        if response == 'Hello, world!':
            break

    # Close the connection
    print("Closing connection...")
