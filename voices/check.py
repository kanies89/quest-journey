import socket

# create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific port
server_address = ('localhost', 9999)
server_socket.bind(server_address)

# listen for incoming connections
server_socket.listen(1)
print('Server is listening on port {}...'.format(server_address[1]))

# wait for a client connection
client_socket, client_address = server_socket.accept()

# when a client connects, receive a command
command = client_socket.recv(1024)
print('Received command: {}'.format(command.decode()))

# close the connection
client_socket.close()
server_socket.close()
