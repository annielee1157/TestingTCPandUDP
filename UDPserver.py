from socket import *

serverAddr = ('localhost', 12000)
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(serverAddr)
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    sentence = message.decode()
    arr = sentence.split(' ')
    s = ""
    for i in range(len(arr)):
        if len(arr[i]) == 0:
            continue
        s += str(len(arr[i])) + " "
    serverSocket.sendto(s.encode(), clientAddress)
