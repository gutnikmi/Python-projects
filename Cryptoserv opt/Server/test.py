import os


def list(args=None):
    files_serv = '\n'.join(os.listdir(args)) + "\n"
    print(files_serv)


# with open("test_folder" + "/test_txt.txt", "r") as f:
#     data = f.read()
# print(data)
cur_path = os.path.dirname(__file__)

def ls(cp):
    list(cp)


def up(cp):
    cur_path = os.path.dirname(cp)
    return cur_path


def down(cp):
    new_path = os.path.join(cp, "Server").replace('\\', '/')
    if not os.path.isdir(new_path):
        new_path = cp
        print("Not a valid dir")
    return new_path


print(cur_path)
list(cur_path)
cur_path = up(cur_path)
print(cur_path)
list(cur_path)
cur_path = down(cur_path)
print(cur_path)
list(cur_path)
print("this is a test string")