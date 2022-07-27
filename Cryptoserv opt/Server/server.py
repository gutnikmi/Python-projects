import socket, time, rsa, pickle, os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from serv_commands import serv_cmd


def enc_pic(data):  # encrypt and pickle
    cipher = AES.new(aes_key, AES.MODE_ECB)
    data = pickle.dumps(data)
    data = cipher.encrypt(pad(data, BS))
    return data


def decr_pic(data):  # decrypt and unpickle
    decipher = AES.new(aes_key, AES.MODE_ECB)
    data = unpad(decipher.decrypt(data), BS)
    res = pickle.loads(data)
    return res


def rec():  # receive message
    while True:
        data = decr_pic(con_handle())  # receive data
        res = serv_cmd(data)  # parse commands
        print(res)
        res_data = enc_pic(res)
        time_rec = time.asctime()
        data2 = f"message received at {time_rec}"
        data2 = enc_pic(data2)
        con.conn.send(res_data)
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
        print("Connection closed, listening for new connections")
        con.sock.close()
        new_con()
        send_ks(pub)
        aes_key = rec_keys()
        print("Received the AES key")
        rec()
        data = b'Errors detected '
        data = rsa.encrypt(data, pub)
        return data


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
    BS = 16
    print("Server is up, awaiting connections")
    con = Cnct()
    (pub, pri) = rsa.newkeys(512)
    send_ks(pub)
    aes_key = rec_keys()
    print("Received the AES key")
    rec()
