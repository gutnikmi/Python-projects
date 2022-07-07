import socket


def decr(str):
    st = str.decode()
    list = []
    for i in st:
        list.append(chr(int(ord(i) / 2)))
    ostr = ''.join(list)
    return ostr


host = "127.0.0.1"
port = 9090

sock = socket.socket()
sock.bind((host, port))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    data = decr(data)
    print(data)
    data = data.encode()
    if not data:
        break
    conn.send(data)


conn.close()
