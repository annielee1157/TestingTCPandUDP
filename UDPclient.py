from socket import *

serverAddr = ('localhost', 12000)
clientSocket = socket(AF_INET,SOCK_DGRAM)
f = open("testcases.txt", "r")
f1 = f.readlines()
for message in f1:
    message = message.replace('\n', '')
    if len(message) == 0:
        continue
    clientSocket.sendto(message.encode(), serverAddr)
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    print(modifiedMessage.decode())

clientSocket.close()
