import os
from os import listdir
from os.path import isfile, join
from PIL import Image
import io

''' to implement a function: add to dictionary in serv_cmd, add allowed commands in allowed list inside a function '''


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
        "ls": list_f,
        "man": help_f,
        "cat": read_f,
        "..": go_up,
        "cd": go_down,
        "show": show
    }

    if " " in inpt:
        inpt, args = inpt.split(" ", 1)
        if inpt in func_dict:
            return func_dict[inpt](args)
        else:
            return "Unknown command, type man to list all available commands"
    else:
        if inpt in func_dict:
            return func_dict[inpt]()
        else:
            return "Unknown command, type man to list all available commands"


def arg_filter(args, allowed):
    res = ""
    f_args = args
    while f_args != "":
        if " " in f_args:
            arg, f_args = f_args.split(" ", 1)
            if arg not in allowed:
                res += f"{arg} is not an argument, type man command for all valid args"
        else:
            if f_args not in allowed:
                res += f"{f_args} is not an argument, type man command for all valid args"
            f_args = ""
    return res


def list_f(args=''):
    res = ""
    allowed = ["-a", "-files", "-folders"]
    res += arg_filter(args, allowed)
    if "-files" in args:
        res += f"Current directory:{glob.path} \n"
        fl = [f for f in listdir(glob.path) if isfile(join(f))]
        res += '\n'.join(fl) + "\n"
    if "-folders" in args:
        res += f"Current directory:{glob.path} \n"
        fl = [f for f in listdir(glob.path) if not isfile(join(f))]
        res += '\n'.join(fl) + "\n"
    if args == '' or "-a" in args:
        res += f"Current directory:{glob.path} \n"
        files_serv = '\n'.join(os.listdir(glob.path)) + "\n"
        res += files_serv
    return res


def help_f(args=''):
    res = ""
    allowed = ["-h", "ls", "cat", "..", "cd", "show"]
    res += arg_filter(args, allowed)
    if "ls" in args:  # optional args
        res += "-list: lists all files stored on the server.\n" \
               "accepts arguments:\n" \
               "-a: full folder contents \n" \
               "-files: list only files\n" \
               "-folders: list only folders"
    # if ".." in args: #  man template
    #     res +=
    if "cat" in args:
        res += "if possible reads text from the file, otherwise reads bytes from the file"
    if ".." in args:
        res += "moves path up a directory"
    if "cd" in args:
        pass
    if "show" in args:
        pass
    if args == '' or "-h" in args:  # default arg
        res += "ls: lists all files stored on the server \n" \
                   "man: lists all server commands \n" \
               "type man command to get info on said command"
    return res


def read_f(args=''):
    try:
        with open(glob.path + "/" + args, "r") as f:
            data = f.read()
    except Exception:
        with open(glob.path + "/" + args, "rb") as f:
            data = f.read()
    return data


def test():
    print(serv_cmd(input()))
    test()


def go_up(args=''):
    res = ""
    allowed = ["-ls"]
    res += arg_filter(args, allowed)
    if args == '' or "-ls" in args:  # default arg
        glob.path = os.path.dirname(glob.path)
        res += f"Current directory:{glob.path}"
    if "-ls" in args:  # optional args
        res = list_f()
    return res


def go_down(args):
    res = ""
    new_path = os.path.join(glob.path, args).replace('\\', '/')
    if not os.path.isdir(new_path):
        res += "Not a valid dir"
    else:
        glob.path = new_path
        res += f"Current directory:{glob.path}"

    return res


def show(args):
    res = ""
    try:
        with open(os.path.join(glob.path, args), "rb") as f:
            data = f.read()
        im = Image.open(io.BytesIO(data))
        res = im.show()
    except Exception as e:
        print(e)
    return res


class Globals:
    def __init__(self):
        self.path = os.path.dirname(__file__)


glob = Globals()


if __name__ == "__main__":
    test()
