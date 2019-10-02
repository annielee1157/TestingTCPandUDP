from socket import *


f = open("testcases.txt", "r")
f1 = f.readlines()
for message in f1:
    message = message.replace('\n', '')
    if len(message) == 0:
        continue
    serverAddr = ('localhost', 12000)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(serverAddr)
    clientSocket.send(message.encode())
    modifiedSentence = clientSocket.recv(1024)
    print (modifiedSentence.decode())
    clientSocket.close()