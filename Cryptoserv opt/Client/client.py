import socket
import rsa
import os
import pickle
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
sock = socket.socket()
host = "127.0.0.1"
port = 9090
sock.connect((host, port))


def enc_pic(data):  # encrypt and pickle
    cipher = AES.new(key, AES.MODE_ECB)
    data = pickle.dumps(data)
    data = cipher.encrypt(pad(data, BS))
    return data


def decr_pic(data):  # decrypt and unpickle
    decipher = AES.new(key, AES.MODE_ECB)  # decryption
    data = unpad(decipher.decrypt(data), BS)  # decryption
    res = pickle.loads(data)  # decryption
    return res


def send_msg(inp):  # send message
    msg = enc_pic(inp)
    sock.send(msg)
    data1 = sock.recv(4096)
    data1 = decr_pic(data1)
    print(data1)
    # data = sock.recv(4096)
    # data = decr_pic(data)
    # print(data)
    send_msg(input())


def send_ks(key):  # send keys
    print("Sent encrypted AES key")
    key = rsa.encrypt(key, pub)
    sock.send(key)
    data = sock.recv(4096)
    print(data.decode('UTF-8'))


def rec_keys():  # receive message
    data = sock.recv(4096)
    data = rsa.key.PublicKey.load_pkcs1(data, format='DER')
    data1 = "Client has received the RSA public key"
    sock.send(data1.encode())
    return data


if __name__ == "__main__":  # main body
    pub = rec_keys()
    key = os.urandom(16)  # l = 128
    BS = 16
    send_ks(key)
    try:
        send_msg(input())
    except KeyboardInterrupt:
        print("keyboard interrupt")
        sock.close()
