import socket
import subprocess
from subprocess import PIPE


if __name__ == "__main__":
    # Set up the server socket
    HOST = '127.0.0.1'  # Localhost
    PORT = 12345  # Arbitrary non-privileged port
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

                if command == 'description':
                    # Start the initiate() function as a subprocess
                    p = subprocess.Popen(['python', 'voice_to_txt.py'],
                                         cwd='C:/Users/Admin/OneDrive/Pulpit/Kodilla/Quest', stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE, shell=True)
                    # response = p.communicate()[0].decode('utf-8').strip()
                    stdout, stderr = p.communicate()
                    return_code = p.returncode

                    if return_code is None:
                        print("Subprocess is still running")
                    else:
                        print(f"Subprocess completed with return code {return_code}")

                elif command == "hello":
                    response = "Hello World!"
                    conn.sendall(response.encode('utf-8'))
                    continue

                elif command == 'description_answer':
                    if isinstance(response, str):
                        conn.sendall(response.encode('utf-8'))
                    elif response is None:
                        conn.sendall(''.encode('utf-8'))
                    else:
                        conn.sendall('Error: response was not a string'.encode('utf-8'))
                    continue

                else:
                    response = 'Invalid command'
                    # Send the response back to the client
                    conn.sendall(response.encode('utf-8'))
                    continue

