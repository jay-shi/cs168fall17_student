import sys
import socket

client_socket = socket.socket()
client_socket.connect((sys.argv[1], int(sys.argv[2])))

message = input('client: ')

while message != 'end this conversation':
    client_socket.send(message.encode())
    received = client_socket.recv(1024).decode()
    print("server: " + received)
    message = input('client: ')

client_socket.close()