import socket
import time
import rsa


def rec():
    while True:
        data = con_handle()
        data = rsa.decrypt(data, pri).decode()
        print(data)
        a = time.asctime()
        data = f"message received at {a}"
        if not data:
            break
        con.conn.send(data.encode())
    rec()


def rec_keys():
    data = con_handle()
    data = data.decode()
    print(data)
    data = "Received keys"
    con.conn.send(data.encode())


def send_ks(a):
    a = a.save_pkcs1(format='DER')
    con.conn.send(a)
    data = con.conn.recv(4096)
    print(data.decode('UTF-8'))


def new_con():
    global con
    con = Cnct()


def con_handle():
    try:
        data = con.conn.recv(4096)
        if data == b'':
            raise Exception()
        return data
    except Exception as e:
        print(e)
        print("Bad data, creating new connection")
        con.sock.close()
        new_con()
        send_ks(pub)
        rec_keys()
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


host = "127.0.0.1"
port = 9090
con = Cnct()
(pub, pri) = rsa.newkeys(512)
send_ks(pub)
rec_keys()
rec()
