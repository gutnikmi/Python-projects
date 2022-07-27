import os
from os import listdir
from os.path import isfile, join


def func_template(args=''):
    res = ""
    allowed = []
    res += arg_filter(args, allowed)
    if "-a" in args:  # optional args
        pass
    if args == '' or "-b" in args:  # default arg
        pass
    return res


def serv_cmd(inpt):  # parse commands
    func_dict = {
        "-list": list_f,
        "-help": help_f,
        "-read": read_f
    }

    if " " in inpt:
        inpt, args = inpt.split(" ", 1)
        if inpt in func_dict:
            return func_dict[inpt](args)
        else:
            return "Unknown command, type -help to list all available commands"
    else:
        if inpt in func_dict:
            return func_dict[inpt]()
        else:
            return "Unknown command, type -help to list all available commands"


def arg_filter(args, allowed):
    res = ""
    f_args = args
    while f_args != "":
        if " " in f_args:
            arg, f_args = f_args.split(" ", 1)
            if arg not in allowed:
                res += f"{arg} is not an argument, type -help -command for all valid args"
        else:
            if f_args not in allowed:
                res += f"{f_args} is not an argument, type -h -command for all valid args"
            f_args = ""
    return res


def list_f(args=''):
    res = ""
    allowed = ["-h", "-l", "-a", "-files", "-folders"]
    res += arg_filter(args, allowed)
    if "-h" in args:
        res += "this function lists all files on the server.\n"
    if "-files" in args:
        fl = [f for f in listdir() if isfile(join(f))]
        res += '\n'.join(fl) + "\n"
    if "-folders" in args:
        fl = [f for f in listdir() if not isfile(join(f))]
        res += '\n'.join(fl) + "\n"
    if args == '' or "-a" in args:
        files_serv = '\n'.join(os.listdir()) + "\n"
        res += files_serv
    return res


def help_f(args=''):
    res = ""
    allowed = ["-h", "-list"]
    res += arg_filter(args, allowed)
    if "-list" in args:  # optional args
        res += "-list: lists all files stored on the server.\n" \
               "accepts arguments:\n" \
               "-h: description \n" \
               "-a: full folder contents \n" \
               "-files: list only files"
    if args == '' or "-h" in args:  # default arg
        res += "-list: lists all files stored on the server \n" \
                   "-help: lists all server commands \n" \
               "type -help -command to get info on said command"
    return res


def read_f(args=''):
    res = ""
    allowed = []
    res += arg_filter(args, allowed)
    if "-a" in args:  # optional args
        pass
    if args == '' or "-b" in args:  # default arg
        print("this works")
    return res


def test():
    print(serv_cmd(input()))
    test()


if __name__ == "__main__":
    test()
