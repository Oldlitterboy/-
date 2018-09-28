from socket import socket
import sys
import getpass as a
def main():
    if len(sys.argv)<3:
        return
    HOST = sys.argv[1]
    PORT=int(sys.argv[2])
    PORT=(HOST,PORT)
    s = socket()
    try:
        s.connect(PORT)
    except Exception as e:
        print(e)
        return
    print('''
            ================welcom=================
            －－ 1 注册　　　　２　登录　　　　３　退出　－－
            ''')
    while 1:
        try:
            cmd = input('>>')
            s.send(cmd.encode())    
            data = s.recv(2048)
            if data.decode()=='请输入密码>>':
                while 1:
                    mima = a.getpass('请输入密码>>')
                    mima1 = a.getpass('请再次输入密码>>')
                    if mima==mima1:
                        s.send(mima.encode())
                        data = s.recv(2048)
                        print(data.decode())
                        break
                    else:
                        print('两次密码不一致　请重新输入')
                        continue

            else:
                print(data.decode())
        except:
            s.send('quit'.encode())
            print('退出')
if __name__=='__main__':
    main()