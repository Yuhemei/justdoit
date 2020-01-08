import socket

sk = socket.socket()
sk.connect('127.0.0.1', 1559)

# 接收欢迎消息

while True:
    i = input("> ")
    # 向服务端发送消息
    sk.sendall(bytes(i, encoding='utf8'))

    # 接收服务端发来的消息
    msg = sk.recv(1024)
    print(str(msg, encoding='utf-8'))

sk.close()