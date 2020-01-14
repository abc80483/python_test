#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口
s.bind((host, port))  # 绑定端口

s.listen(5)  # 等待客户端连接

f = open('C:/Users/x240/Downloads/System/temp.txt', 'r', encoding='utf-8')
c, addr = s.accept()# 建立客户端连接
bool = 1
print('连接地址：', addr)
while True:
    line = f.readline()
    if len(line) < 5:
        line = f.readline()
    if not line:
        break
    list1 = line.split()
    str1 = ' '.join(str(e) for e in list1)
    print(str1)
    c.send(str1.encode())
    rec = c.recv(100).decode()
    while not rec:
        rec = c.recv(100).decode()
    print(rec)


ends = "end"
c.send(ends.encode())
c.close()  # 关闭连接
