import socket
import rsa
import os
from Crypto.Cipher import AES

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


def send_ks(key):
    print("sent AES key", key)
    key = rsa.encrypt(key, pub)
    sock.send(key)
    data = sock.recv(4096)
    print(data.decode('UTF-8'))


def rec_keys():
    data = sock.recv(4096)
    data = rsa.key.PublicKey.load_pkcs1(data, format='DER')
    data1 = "Received RSA public key"
    sock.send(data1.encode())
    return data


pub = rec_keys()
key = os.urandom(16) # l = 128
send_ks(key)
send_msg()
sock.close()
