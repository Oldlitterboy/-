import os,re
import time
import sys
import signal
import pymysql
from socket import *
# 定义需要的全局变量
text = './dict.txt'
HOST = '0.0.0.0'
PORT = 6666
ADDR = (HOST, PORT)
# 流程控制
def jiemian1(c,cur,db):
    while 1:
        hua = '请输入用户名>>'
        c.send(hua.encode())
        data = c.recv(1024).decode()
        hua1 = '请输入密码>>'
        c.send(hua1.encode())
        data1=c.recv(1024).decode()
        cur.execute("select  name from  user;")
        s = cur.fetchall()
        jiagong =("('%s',)"%data)
        for i in s:
            if   jiagong == str(i):
                print(jiagong,i)
                c.send('用户名已存在'.encode())
                break
        else:
            cur.execute("insert into user (name,passwd) values ('%s','%s')"%(data,data1))
            db.commit()
            c.send('恭喜你注册成功'.encode())
            return 
def cz(c,cur,db,name):
    while 1:
        data1 = c.recv(1024).decode()
        if  data1 =='quit':
            break
        cur.execute("select interpret from worlds where word='%s'" % data1)
        s = cur.fetchall()
        if s==():
            c.send('输入的内容不存在'.encode())
        else:
            s = s[0][0]
            c.send(s.encode())
            cur.execute("insert into hist (name,world,time) values ('%s','%s',now())"%(name,data1))
            db.commit()
def hist(c,cur,hua0):
    cur.execute("select  world,time from hist where name='%s';"% hua0)
    s = cur.fetchall()
    s = str(s)
    if not s:
        c.send('记录为空'.encode())
    else:
        c.send(s.encode())
def jiemian2(c,cur,db):
    while 1:
        hua = '请输入用户名>>>'
        c.send(hua.encode())
        hua0 = c.recv(1024).decode()
        hua1 = '请输入密码>>>'
        c.send(hua1.encode())
        hua1 = c.recv(1024).decode()
        cur.execute("select  name,passwd from user;")
        s = cur.fetchall()
        if (hua0,hua1) in s:
            while 1:
                l ='''
                        登录成功　请操作
                =====================================
                1 查询历史　　2　查询单词   quit 退出
                '''
                c.send(l.encode())
                data = c.recv(1024)
                if data.decode() =='2':
                    c.send('请开始查找'.encode())
                    cz(c,cur,db,hua0)
                    continue
                elif data.decode()=='1':
                    hist(c,cur,hua0)
                    c.send('\n已经查询所有内容　'.encode())
                    continue
                elif data.decode()=='quit':
                    break
            return hua0

        else:
            c.send('账号密码不匹配，　请重新输入2'.encode())
            break
def sf(c, db):
    while 1:
        data = c.recv(1024).decode()
        cur = db.cursor()
        if data == '1':
            jiemian1(c, cur,db)
            continue
        elif data == '2':
            jiemian2(c,cur,db)
            continue
        elif data=='3':
            data = c.send('拜拜'.decode())
            break
        else:
            c.send('请输入１　２　３　其中的一个'.encode())
            continue
def main():
    # 数据库链接
    db = pymysql.connect('localhost', 'root', '123456', 'dict')
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    # 忽略紫禁城信号
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    while 1:
        try:
            c, addr = s.accept()
            print(addr)
        except KeyboardInterrupt:            
            s.close()
            sys.exit('服务器退出')
        except Exception as e:
            print(e)
            continue
        pid = os.fork()
        if pid == 0:
            s.close()
            print('有人来了')
            sf(c, db)
            sys.exit('退出')
        else:
            c.close()
            continue
    s.close()
if __name__ == '__main__':
    main()
