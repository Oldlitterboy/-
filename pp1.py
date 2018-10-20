# -*- coding: utf-8
from __future__ import unicode_literals
import easygui as a
from urllib import request
from urllib import parse
from urllib.request import urlopen
import socket
import os
import requests as s




def fanyi(con):
    while 1:
        data = con.recv(4096).decode()
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
        # shuru = input('请输入想翻译的内容>>')
        # shuru = a.enterbox(msg='请输入想翻译的内容')
        if data == 'quit':
            return  (addr, '已退出')
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded;',
            'charset': 'UTF-8',
            'Accept-Language': 'zh-CN,zh;q=0.9'}
        duixiang = {
            "type": "AUTO",
            'i': data,
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTIME',
            'typoResult': 'true'
            }

        data1 = parse.urlencode(duixiang).encode('utf-8')
        requset1 = request.Request(url, data=data1, headers=headers)
        respone = request.urlopen(requset1)
        s = respone.read().decode()
        s = s[96:-5]
        q = 0
        for i in s:
            q += 1
            if i == ',':
                z = s[q:]
                q = 0
                for i in z:
                    q += 1
                    if i == ':':
                        s = z[q:]
        s = ('%s' % data) + ' :  ' + s
        # p = a.ccbox(msg=s, choices=('ok', 'quit'))
        # if p == False:
        #     break
        con.send(s.encode())

s = socket.socket()
s.bind(('0.0.0.0', 8888))
s.listen(10)
while 1:
    try:
        con, addr = s.accept()
        print(addr)
    except:
        continue
    pid =os.fork()
    if pid == 0:
        s.close()
        while 1:
            s = fanyi(con)
            if s !='None':
                print(s)
                break
    else:
        con.close()
        continue
s.close()

