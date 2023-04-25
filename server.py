import socket
from socket import *

"""
  CREATE Socket
  Host,Post->get
  Bind
  Listen
  Accept
  Send/Receive
 """

T_PORT=60
TCP_IP='127.0.0.1'  #Your System IP Address
BUF_SIZE=30

link=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
link.bind((TCP_IP,T_PORT))

link.listen(1)
con,addr=link.accept()

print("Connection Address is: :,addr)

while True:
  data=con.recv(BUF_SIZE)
  if not data:
    break

print("Receive data: ",data)
con.send(data)
con.close()
