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
        data = sock.recv(4096)
    except:
        print("Bad data, try again? y/n")
        a = input()
        if a == "y":
            print(a)
            con_handle()

        else:
            sock.close()
    return data


host = "127.0.0.1"
port = 9090
sock = socket.socket()
sock.bind((host, port))
sock.listen(1)
conn, addr = sock.accept()
print('Client connected:', addr)


def rec():
    while True:
        data = con_handle()
        data = "Wrong data format"
        data = data.encode()
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
    data = "Wrong data format"
    data = data.encode()
    data = data.decode()
    print(data)
    data = "Received key"
    conn.send(data.encode())


rec_keys()
rec()
