#! /bin/bash
## -*- coding: utf-8 -*-

import socket
import threading
import getpass
import psutil
import hashlib
import crypto
import random
import globalVar as gl


# 实现密码求散列的功能
def sha256(s):
    return hashlib.sha256(str(s).encode('utf-8')).hexdigest()


def get_netcard():
    netcard_info = []
    info = psutil.net_if_addrs()
    for k, v in info.items():
        for item in v:
            if item[0] == 2 and not item[1] == '127.0.0.1':
                netcard_info.append((k, item[1]))
                return netcard_info


ipaddr = get_netcard()[0][1]
print('本机ip地址为： ', ipaddr)

gl._init()
_A = gl.get_value('a')
_Q = gl.get_value('q')

bind_ip = '0.0.0.0'
bind_port = 0
while (bind_port < 1024 or bind_port > 65535):
    # 突然想到要安全编程 防止输入非预期字符导致程序崩溃 这是面试书上的
    try:
        bind_port = int(input('请输入要开放的端口(>1023): '))
    except:
        print('只可以输入数字！')

password = sha256(getpass.getpass('请输入约定好的密码'))
repassword = sha256(getpass.getpass('请二次确认密码'))
while (repassword != password):
    password = sha256(getpass.getpass('请输入约定好的密码'))
    repassword = sha256(getpass.getpass('请二次确认密码'))


def handle_client(client_socket):
    if gl.get_value('_Xb') == None:
        _Xb = random.randint(_Q - 1000, _Q)
        gl.set_value('_Xb', _Xb)


    _Yb = pow(_A, gl.get_value('_Xb'), _Q)
    request = bytes.decode(client_socket.recv(1024))
    if gl.get_value('key') == None:
        gl.set_value('key', str(pow(int(request[64:]), gl.get_value('_Xb'), _Q))[:16].rjust(16, '0'))
# 因为是服务器端，所以只要程序运行，那么这个文件就不能改
    if request[:64] == password:
        try:
            f = open((password), 'w')
            client_socket.send(bytes(sha256('Y') + str(_Yb), encoding='utf-8'))  # 登录成功
    
        except:
            print('文件初始化创建失败')
    else:
        request = crypto.aes_decode(request, gl.get_value('key'))
        if request[:4] == 'MSG=':
            try:
                f = open(('./'+password), 'w')
                f.write(request[4:])
                client_socket.send(bytes(crypto.aes_encode('R', gl.get_value('key')), encoding='utf-8'))  # 登录成功
            except:
                print('写入文件失败')
        elif request[:4] == 'RMSG':
            try:
                f = open(('./'+password), 'r')
                msg = f.read()
                client_socket.send(bytes(crypto.aes_encode(msg, gl.get_value('key')), encoding='utf-8'))
            except:
                print('文件读取失败')
    f.close()
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)  # set max connecting number

print('[*] Listening on %s:%d' % (bind_ip, bind_port))

while True:
    client, addr = server.accept()

    print('[*] Accepted connection from: %s:%d' % (addr[0], addr[1]))

    client_handle = threading.Thread(target=handle_client, args=(client,))

    client_handle.start()
