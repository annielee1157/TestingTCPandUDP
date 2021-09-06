from socket import *
import time

start_time = time.time()
with open("testcases.txt", "r") as f:
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
latency = time.time() - start_time
print(f'Latency: {round(latency*1000, 3)}ms')