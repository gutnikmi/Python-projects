import socket
import time


def decr(stri):
    st = stri.decode()
    lst = []
    for i in st:
        lst.append(chr(int(ord(i) / 2)))
    ostr = ''.join(lst)
    return ostr


def con_handle():
    try:
        data = conn.recv(4096)
    except Exception as e:
        print(e)
        print("Bad data, create new connection? y/n")
        a = input()
        if a == "y":
            sock.close()
            con.connect()

        else:
            con_handle()
    return data


class Connect:
    def connect(self):
        self.conn, self.addr = sock.accept()
        return self.conn, self.addr


host = "127.0.0.1"
port = 9090
sock = socket.socket()
sock.bind((host, port))
sock.listen(2)
con = Connect()
conn, addr = con.connect()
print('Client connected:', addr)


def rec():
    while True:
        data = con_handle()
        data = decr(data)
        print(data)
        a = time.asctime()
        data = f"message received at {a}"
        if not data:
            break
        conn.send(data.encode())

    rec()


def rec_keys():
    data = con_handle()
    data = data.decode()
    print(data)
    data = "Received key"
    conn.send(data.encode())


rec_keys()
rec()
