from socket import *

HOST=''
PORT=8088
BUFSIZE=1024

udp_socket=socket(AF_INET,SOCK_DGRAM)
ADDR=(HOST,PORT)
udp_socket.bind(ADDR)
# 阻塞
while True:
    print('waiting吧')
    data,addr=udp_socket.recvfrom(BUFSIZE)
    cont=data.decode('utf-8')
    udp_socket.sendto(cont.encode('utf-8'))
    print(cont)
    if not data:
        break
udp_socket.close()