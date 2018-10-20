# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import easygui as a
import socket
s = socket.socket()
s.connect(('172.88.4.178', 8888))
while 1:
    shuru = a.enterbox(msg='请输入想翻译的内容')
    if not shuru:
        s.send('quit'.encode())
        break
    s.send(shuru.encode())
    data = s.recv(4096).decode()
    p = a.ccbox(msg=data, choices=('ok', 'quit'))
