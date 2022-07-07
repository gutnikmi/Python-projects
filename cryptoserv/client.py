import socket

def encr():
    str = input()
    list = []
    for i in str:
        list.append(chr(ord(i) * 2))
    ostr = ''.join(list)
    return ostr.encode()


sock = socket.socket()
host = "127.0.0.1"
port = 9090
sock.connect((host, port))


def send():
    d = encr()
    sock.send(bytes(d))
    data = sock.recv(4096)
    print(data.decode('UTF-8'))
    send()


send()
sock.close()
