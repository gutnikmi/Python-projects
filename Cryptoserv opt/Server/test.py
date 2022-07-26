import os
import pickle
from Crypto.Util.Padding import pad, unpad


files_serv = os.listdir()
files_serv = pickle.dumps(files_serv)
a = pad(files_serv, 16)
print(a)
b = unpad(a, 16)
b = pickle.loads(b)
print(b)


