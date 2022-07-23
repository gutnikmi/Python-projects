import socket
import rsa
import os
from Crypto.Cipher import AES

sock = socket.socket()
host = "127.0.0.1"
port = 9090
sock.connect((host, port))


pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def send_msg():
    cipher = AES.new(key, AES.MODE_ECB)
    msg = cipher.encrypt(pad(input()).encode())
    sock.send(msg)
    data = sock.recv(4096)
    print(data.decode())
    send_msg()


def send_ks(key):
    print("Sent encrypted AES key")
    key = rsa.encrypt(key, pub)
    sock.send(key)
    data = sock.recv(4096)
    print(data.decode('UTF-8'))


def rec_keys():
    data = sock.recv(4096)
    data = rsa.key.PublicKey.load_pkcs1(data, format='DER')
    data1 = "Client has received the RSA public key"
    sock.send(data1.encode())
    return data


if __name__ == "__main__":
        pub = rec_keys()
        key = os.urandom(16) # l = 128
        BS = 16
        send_ks(key)
        send_msg()
        sock.close()