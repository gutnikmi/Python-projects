import os
from os import listdir
from os.path import isfile, join


def serv_cmd(inpt):  # parse commands
    func_dict = {
        "-l": list_f,
        "-h": help_f,
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
            return "Unknown command, type -h to list all available commands"


def arg_filter(args, allowed):
    res = ""
    f_args = args
    while f_args != "":
        if " " in f_args:
            arg, f_args = f_args.split(" ", 1)
            if arg not in allowed:
                res += f"{arg} is not an argument, type -h -l for all valid args"
        else:
            if f_args not in allowed:
                res += f"{f_args} is not an argument, type -h -l for all valid args"
            f_args = ""
    return res


def list_f(args=''):
    res = ""
    allowed = ["-h", "-l"]
    res += arg_filter(args, allowed)
    if "-h" in args:
        res += "this function lists all files on the server.\n"
    if "-h" in args:
        res += "this function lists all files on the server.\n"
    if args == '' or "-l" in args:
        files_serv = '\n'.join(os.listdir()) + "\n"
        res += files_serv
    return res


def help_f(args=''):
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
