# -*- coding: utf-8 -*-

import socket
client = socket.socket()            # 生成socket实例
client.connect(('127.0.0.1', 5000)) # 连接服务器
while True:                         # while循环用于和客户端一直交互
    data = input(">>>>")
    client.send(data.encode())
    data = client.recv(1024)
