from socket import *
import time

serverAddr = ('localhost', 12000)
clientSocket = socket(AF_INET,SOCK_DGRAM)
start_time = time.time()
with open("testcases.txt", "r") as f:
    f1 = f.readlines()
    for message in f1:
        message = message.replace('\n', '')
        if len(message) == 0:
            continue
        clientSocket.sendto(message.encode(), serverAddr)
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

        print(modifiedMessage.decode())
latency = time.time() - start_time
print(f'Latency: {round(latency*1000, 3)}ms')
clientSocket.close()
