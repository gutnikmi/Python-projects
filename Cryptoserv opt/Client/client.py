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


def send_msg(inp):
    cipher = AES.new(key, AES.MODE_ECB)
    msg = pad(pickle.dumps(inp), 16)
    msg = cipher.encrypt(msg)
    sock.send(msg)
    data1 = sock.recv(4096)
    decipher = AES.new(key, AES.MODE_ECB)  # decryption
    data1 = unpad(decipher.decrypt(data1), 16)  # decryption, unpadding
    data1 = pickle.loads(data1)  # unpickle
    print(data1)
    data = sock.recv(4096)
    decipher = AES.new(key, AES.MODE_ECB)  # decryption
    data = unpad(decipher.decrypt(data), 16)  # decryption, unpadding
    data = pickle.loads(data)  # unpickle
    print(data)
    send_msg(input())


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
    key = os.urandom(16)  # l = 128
    BS = 16
    send_ks(key)
    try:
        send_msg(input())
    except KeyboardInterrupt:
        print("keyboard interrupt")
        sock.close()
