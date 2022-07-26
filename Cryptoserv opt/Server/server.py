import socket
import time
import rsa
import pickle
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def rec():  # receive message
    while True:
        data = con_handle()  # receive data
        decipher = AES.new(aes_key, AES.MODE_ECB)  # decryption
        data = unpad(decipher.decrypt(data), 16)  # decryption
        res = pickle.loads(data)  # decryption
        data1 = serv_cmd(res)  # parse commands
        print(data1)
        cipher = AES.new(aes_key, AES.MODE_ECB)
        data1 = pickle.dumps(data1)
        data1 = cipher.encrypt(pad(data1, 16))
        a = time.asctime()
        data2 = f"message received at {a}"
        data2 = pickle.dumps(data2)
        cipher = AES.new(aes_key, AES.MODE_ECB)
        data2 = cipher.encrypt(pad(data2, 16))
        con.conn.send(data1)
        con.conn.send(data2)
        rec()


def rec_keys():  # receive keys
    data = con_handle()
    data = rsa.decrypt(data, pri)
    data1 = "Server has received and decrypted the AES key"
    con.conn.send(data1.encode())
    return data


def send_ks(a):  # send keys
    a = a.save_pkcs1(format='DER')
    con.conn.send(a)
    data = con.conn.recv(4096)
    print(data.decode('UTF-8'))


def new_con():  # creates new connection
    global con
    con = Cnct()


def con_handle():  # handles received data, creates new connections
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


def serv_cmd(inpt):  # parse commands
    match inpt:
        case "-l":
            files_serv = os.listdir()
            return files_serv
        case _:
            return "Invalid command, write -h for list of commands"


class Cnct:  # settings for a connection
    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind((host, port))
        self.sock.listen(2)
        self.conn, self.addr = self.sock.accept()
        print('Client connected:', self.addr)


if __name__ == "__main__":  # main body
    host = "127.0.0.1"
    port = 9090
    con = Cnct()
    (pub, pri) = rsa.newkeys(512)
    send_ks(pub)
    aes_key = rec_keys()
    print("Received the AES key")
    rec()
