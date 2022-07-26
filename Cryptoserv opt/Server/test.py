import os
import pickle
from Crypto.Util.Padding import pad, unpad


def lovea(args=''):
    allowed = ["-", "h", "l"]
    for i in args:
        if i not in allowed:
            print(f"-{i} is not an argument")
    if "-h" in args:
        print("this helps")
    if "-l" in args:
        print(os.listdir())
    print("this is func a")


def loveb():
    print("this is func b")


def lovec():
    print("this is func c")


def serv_cmd(inpt):  # parse commands
    func_dict = {
        "la": lovea,
        "lb": loveb,
        "lc": lovec
    }

    if " " in inpt:
        inpt, args = inpt.split(" ", 1)
        if inpt in func_dict:
            func_dict[inpt](args)
        else:
            print("wrong funct")
    else:
        if inpt in func_dict:
            func_dict[inpt]()
        else:
            print("wrong funct")
    # match inpt:
    #     case "-l":
    #         files_serv = os.listdir()
    #         files_serv = '\n'.join(files_serv)
    #         return files_serv
    #     case "-h":
    #         cmd_list = "-l: lists all files stored on the server \n" \
    #                    "-h: lists all server commands"
    #         return cmd_list
    #     case _:
    #         return "Invalid command, write -h for list of commands"


def test():
    # print(serv_cmd(input()))
    serv_cmd(input())
    test()


test()
# inpt = "test test test"
# inpt, args = inpt.split(" ", 1)
# print("\n", inpt, "\n", args)

