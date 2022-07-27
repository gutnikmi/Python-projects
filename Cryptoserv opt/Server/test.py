import os
import pickle
from Crypto.Util.Padding import pad, unpad


def func_template(args=''):
    res = ""
    allowed = []
    res += arg_filter(args, allowed)
    if "-a" in args:  # optional args
        pass
    if args == '' or "-b" in args:  # default arg
        pass
    return res


def arg_filter(args, allowed):
    res = ""
    f_args = args
    while f_args != "":
        if " " in f_args:
            arg, f_args = f_args.split(" ", 1)
            if arg not in allowed:
                res += f"{arg} is not an argument, type -h -l for all valid args \n"
        else:
            if f_args not in allowed:
                res += f"{f_args} is not an argument, type -h -l for all valid args \n"
            f_args = ""
    # for i in args:
    #     if (i != " " and i != "-") and (f"-{i}" not in allowed):
    #         res += f"-{i} is not an argument, type -h -l for all valid args \n"
    return res



def listf(args=''):
    res = ""
    allowed = ["-h", "-l"]
    res += arg_filter(args, allowed)
    if "-h" in args:
        res += "this function lists all files on the server.\n"
    if args == '' or "-l" in args:
        files_serv = '\n'.join(os.listdir()) + "\n"
        res += files_serv
    return res


def helpf(args=''):
    res = ""
    allowed = ["-h", "-l"]
    res += arg_filter(args, allowed)
    if "-l" in args:  # optional args
        res += "-l: lists all files stored on the server.\n" \
               "accepts arguments:\n" \
               "-h: description \n"
    if args == '' or "-h" in args:  # default arg
        res += "-l: lists all files stored on the server \n" \
                   "-h: lists all server commands"
    return res


def lovec():
    print("this is func c")


def serv_cmd(inpt):  # parse commands
    func_dict = {
        "-l": listf,
        "-h": helpf,
    }

    if " " in inpt:
        inpt, args = inpt.split(" ", 1)
        if inpt in func_dict:
            return func_dict[inpt](args)
        else:
            return "Unknown command, type -h to list all available commands"
    else:
        if inpt in func_dict:
            return func_dict[inpt]()
        else:
            return "wrong func"
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
    print(serv_cmd(input()))
    test()


test()
# inpt = "test test test"
# inpt, args = inpt.split(" ", 1)
# print("\n", inpt, "\n", args)

