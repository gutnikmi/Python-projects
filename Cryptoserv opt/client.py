import socket
from RSA import keygen, rsa, rsa_dec


def encr():
    stri = input()
    lst = []
    for i in stri:
        lst.append(chr(ord(i) * 2))
    ostr = ''.join(lst)
    return ostr.encode()


sock = socket.socket()
host = "127.0.0.1"
port = 9090
sock.connect((host, port))


def send_msg():
    d = rsa(input(), pub)
    sock.send(d)
    data = sock.recv(4096)
    print(data.decode())
    send_msg()


def send_ks():
    a = "2"
    sock.send(a.encode())
    data = sock.recv(4096)
    print(data.decode('UTF-8'))


def rec_keys():
    data = sock.recv(4096)
    data = data.decode()
    data = tuple(map(int, data.split(',')))
    print(data)
    data1 = "Received keys"
    sock.send(data1.encode())
    return data


pub = rec_keys()
send_ks()
send_msg()
sock.close()
