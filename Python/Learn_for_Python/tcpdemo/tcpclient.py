# -*- coding utf-8 -*-
import socket
import time

server_ip='127.0.0.1'
server_port=1559
socket_num=int(input("连几个呀:"))

socket_ok=[]

for i in range(socket_num):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((server_ip,server_port))
    socket_ok.append(sock)
    print(f'{sock}已经创建，id为{i}')
while True:
    print('ok')
    for s in socket_ok:
        s.send((str(12).encode('utf-8')))
        print(f'client{s}已经发完了')
    time.sleep(3)