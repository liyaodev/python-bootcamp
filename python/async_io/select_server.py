# -*- coding: utf-8 -*-

import select
import socket
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setblocking(False)       # 设置为非阻塞状态
server.bind(("0.0.0.0", 5000))
server.listen(5)
inputs, outputs = [], []
inputs.append(server)           # 将sever作为一个fd也放入select并进行检测
while True:
    readable, writable, exceptionable = select.select(inputs, outputs, inputs)
    for r in readable:
        if r is server:         # 判断r是不是server本身，如果是本身则代表来了新的连接
            conn, addr = r.accept()
            print("客户端：{}已经连接".format(addr))
            inputs.append(conn)
        else:                   # 否则代表readable里是已经建立的连接
            data = r.recv(1024)
            if data:
                print(data)
                r.send(data)
            else:
                print("客户端已经断开")
                inputs.remove(r)
        for e in exceptionable:
            print("客户端出错！")
            inputs.remove(e)
