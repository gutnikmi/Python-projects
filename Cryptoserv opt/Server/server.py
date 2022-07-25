import socket
import time
import rsa
import pickle
from Crypto.Cipher import AES

unpad = lambda s: s[:-ord(s[len(s)-1:])]


def rec():
    while True:
        data = con_handle()
        decipher = AES.new(aes_key, AES.MODE_ECB)
        print(unpad(decipher.decrypt(data).decode()))
        a = time.asctime()
        data = f"message received at {a}"
        if not data:
            break
        con.conn.send(data.encode())
    rec()


def rec_keys():
    data = con_handle()
    data = rsa.decrypt(data, pri)
    data1 = "Server has received and decrypted the AES key"
    con.conn.send(data1.encode())
    return data


def send_ks(a):
    a = a.save_pkcs1(format='DER')
    con.conn.send(a)
    data = con.conn.recv(4096)
    print(data.decode('UTF-8'))


def new_con():
    global con
    con = Cnct()


def con_handle():
    global aes_key
    try:
        data = con.conn.recv(4096)
        if data == b'':
            raise Exception()
        return data
    except Exception as e:
        print(e)
        print("Bad data, listening for new connections")
        con.sock.close()
        new_con()
        send_ks(pub)
        aes_key = rec_keys()
        rec()
        data = b'Errors detected '
        data = rsa.encrypt(data, pub)
        return data


class Cnct:
    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind((host, port))
        self.sock.listen(2)
        self.conn, self.addr = self.sock.accept()
        print('Client connected:', self.addr)


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 9090
    con = Cnct()
    (pub, pri) = rsa.newkeys(512)
    send_ks(pub)
    aes_key = rec_keys()
    print("Received the AES key")
    rec()
