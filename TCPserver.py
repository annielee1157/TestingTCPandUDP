from socket import *


server_address = ('localhost', 12000)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(server_address)
serverSocket.listen(1)
print ('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    arr = sentence.split(' ')
    s = ""
    for i in range(len(arr)):
        if len(arr[i]) == 0:
            continue
        s += str(len(arr[i])) + " "
    connectionSocket.send(s.encode())
    connectionSocket.close()