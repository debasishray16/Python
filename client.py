import socket
T_PORT=5006
TCP_IP='127.0.0.1'
BUF_SIZE=1024

Message="Hello World!"

# socket.SOCK_STREAM = for TCP/IP
# socket.SOCK_DGRAM = for UDP

link=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
link.connect((TCP_IP,T_PORT))

link.send(Message)
data=link.recv(BUF_SIZE)
link.close()
