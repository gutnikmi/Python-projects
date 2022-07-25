import os
import pickle


def pad(byte_array: bytearray):
    """
    pkcs5 padding
    """
    pad_len = 16 - len(byte_array) % 16
    return byte_array + (bytes([pad_len]) * pad_len)


# pkcs5 - unpadding
def unpad(byte_array: bytearray):
    return byte_array[:-ord(byte_array[-1:])]


files_serv = "adsfs" # os.listdir()
files_serv = pickle.dumps(files_serv)
a = pad(files_serv)
print(a)
b = unpad(a)
b = pickle.loads(b)
print(b)


