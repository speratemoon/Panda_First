from socket import *

host="127.0.0.1"
port=8888
adrr=(host,port)

sockfd=socket()
sockfd.connect(adrr)
while True:
    msg=input("发言：")
    if not msg:
        break
    sockfd.send(msg.encode())
    data=sockfd.recv(1024)
    print(data.decode())