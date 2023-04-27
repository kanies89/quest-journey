import socket
import main

# Set up the server socket
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    # Wait for incoming connections
    print(f"Server is listening on {HOST}:{PORT}...")

    while True:
        conn, addr = s.accept()
        print(f"Connected by {addr}")

        # Receive data and send response
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # Decode the incoming command and send response
            command = data.decode('utf-8').strip()

            # do something with the command
            print('Command received: ' + command)

            if command == 'hello':
                response = 'Hello, world!'
                # Send the response back to the client
                conn.sendall(response.encode('utf-8'))
                continue

            else:
                response = 'Invalid command'
                # Send the response back to the client
                conn.sendall(response.encode('utf-8'))
                continue
