import socket

# Set up the client socket
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # The same port as the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Send a command to the server
    command = "description"
    s.sendall(command.encode('utf-8'))
    # Close the connection
    print("Closing connection...")


import asyncio
import unreal
from concurrent.futures import ThreadPoolExecutor
import socket
import select


# Define the function you want to execute on a separate thread
async def connect(com):
    # Set up the client socket
    HOST = '127.0.0.1'  # Localhost
    PORT = 12345  # The same port as the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setblocking(False)  # Set the socket to non-blocking mode
        s.connect((HOST, PORT))

        # Send commands and receive responses
        while True:
            # Wait for the socket to become readable
            readable, _, _ = select.select([s], [], [], 0.1)
            if s in readable:
                # Read data from the socket
                data = s.recv(1024)
                if not data:
                    # The connection has been closed
                    break
                response = data.decode('utf-8').strip()
                print(f"Server response: {response}")

                # Exit the loop if the 'exit' command is sent
                if isinstance(response, str):
                    break

            # Send a command to the server
            command = com
            s.sendall(command.encode('utf-8'))

        # Close the connection
        print("Closing connection...")
        set_var_out(response)


def set_var_out(result):
    unreal.GlobalEditorUtilityBase.get_main_thread_rpc_queue().run_on_main_thread(
        lambda: set_var_out_on_main_thread(result))


def set_var_out_on_main_thread(result):
    actors = unreal.GameplayStatics.get_all_actors_with_tag(unreal.get_game_world(), "PS")
    if len(actors) > 0:
        actor = actors[0]
        actor.set_property("var_out", result)
    else:
        print("No actors found with the tag 'PS' in the current level.")


async def main():
    com = "description"  # Replace this with the desired command
    with ThreadPoolExecutor(max_workers=1) as executor:
        # Submit the function to the thread pool
        future = executor.submit(asyncio.run, connect(com))
        await future


asyncio.run(main())
