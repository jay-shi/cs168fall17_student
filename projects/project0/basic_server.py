import socket
import sys

server_socket = socket.socket()
server_socket.bind(('localhost', int(sys.argv[1])))
print('server is hosted on local port: ' + sys.argv[1])
server_socket.listen(2)
(client_socket, address) = server_socket.accept()
while True:
    message = client_socket.recv(1024)
    print("client: " + message.decode())
    res = input("server: ")
    client_socket.send(res.encode())
server_socket.close()
    