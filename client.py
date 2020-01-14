#!/usr/bin/python
# 文件名：client.py
# coding=UTF-8
import os

import numpy as np
from keras.utils import np_utils
from keras.models import load_model
import socket

os.environ['KMP_WARNINGS'] = '0'
model = load_model('model.h5')

lab_num = ['小雲雀', '石燕', '竹雞', '灰樹鵲', '白頭翁']



s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口号

s.connect((host, port))

while True:
    x = s.recv(1024).decode()
    while not x:
        x = s.recv(1024).decode()
    if x == "end":
        break
    back = "ok"
    s.send(back.encode())
    print(x)
    x += " "
    if not x:
        break
    list0 = x.split()
    list1 = []
    list1 += [int(i) for i in list0]
    print(list1)
    list1 = np_utils.to_categorical(list1, 65).tolist()
    list1 = np.reshape(list1, (1,5*65)).astype('float32')
    predictions = model.predict_classes(list1)
    print(lab_num[predictions[0]])
s.close()
