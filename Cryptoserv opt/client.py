import socket
import rsa


sock = socket.socket()
host = "127.0.0.1"
port = 9090
sock.connect((host, port))


def send_msg():
    # d = rsa(input(), pub)
    d = rsa.encrypt(input().encode(), pub)
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
    # data = data.decode()
    # data = tuple(map(int, data.split(',')))
    data = rsa.key.PublicKey.load_pkcs1(data, format='DER')
    #print(data)
    data1 = "Received keys"
    sock.send(data1.encode())
    return data


pub = rec_keys()
send_ks()
send_msg()
sock.close()
