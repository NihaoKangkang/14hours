import globalVar as gl
import socket
import crypto
import random

#上传
def trans(newMessege):

    addr = gl.get_value('addr')
    port = gl.get_value('port')
    target_host = addr
    target_port = port
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, int(target_port)))


    msg = crypto.aes_encode('MSG='+newMessege,gl.get_value('key'))

    client.send(bytes(msg, encoding='utf-8'))

    response = crypto.aes_decode(bytes.decode(client.recv(4096)), gl.get_value('key'))

    if response == 'R':
        return True
    else:
        return False

#下载
def RC():
    addr = gl.get_value('addr')
    port = gl.get_value('port')
    target_host = addr
    target_port = port
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host, int(target_port)))
    msg = crypto.aes_encode('RMSG', gl.get_value('key'))
    client.send(bytes(msg, encoding='utf-8'))

    response = crypto.aes_decode(bytes.decode(client.recv(4096)), gl.get_value('key'))

    return response