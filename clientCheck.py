import socket
import random
import hashlib
import globalVar as gl
def sha256(s):
    return hashlib.sha256(str(s).encode('utf-8')).hexdigest()

def loginCheck(addr, port, password):
    #应该不能用while循环 否则会爆炸
    _Xa = random.randint(gl.get_value('q')-1000, gl.get_value('q'))
    gl.set_value('_Xa', _Xa)
    _A = gl.get_value('a')
    _Q = gl.get_value('q')
    _Ya = pow(_A, _Xa, _Q)
    target_host = addr
    target_port = port
    target_pass = password
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host, int(target_port)))
    msg = target_pass+str(_Ya)
    client.send(bytes(msg, encoding='utf-8'))

    response = bytes.decode(client.recv(4096))
    if response[:64] == sha256('Y'):
        return response[64:]
    else:
        return False