import os
import pickle
from Crypto.Util.Padding import pad, unpad


def serv_cmd(inpt):  # parse commands
    match inpt:
        case "-l":
            files_serv = os.listdir()
            files_serv = '\n'.join(files_serv)
            return files_serv
        case _:
            return "Invalid command, write -h for list of commands"


def test():
    print(serv_cmd(input()))
    test()


test()