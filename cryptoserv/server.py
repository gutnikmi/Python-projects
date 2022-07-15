import socket
import time
from RSA import keygen, rsa, rsa_dec


def decr(stri):
    st = stri.decode()
    lst = []
    for i in st:
        lst.append(chr(int(ord(i) / 2)))
    ostr = ''.join(lst)
    return ostr


def rec():
    while True:
        data = con_handle()
        data = decr(data)
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
    data = "Received key"
    con.conn.send(data.encode())


def send_ks():
    a = "2"
    con.conn.send(a.encode())
    data = con.conn.recv(4096)
    print(data.decode('UTF-8'))


def new_con():
    global con
    con = Cnct()


def con_handle():
    try:
        data = con.conn.recv(4096)
    except Exception as e:
        print(e)
        print("Bad data, create new connection? y/n")
        a = input()
        if a == "y":
            con.sock.close()
            new_con()
            rec_keys()
            rec()
            data = "error"
        else:
            con.sock.close()
            data = "error"
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
rec_keys()
rec()
