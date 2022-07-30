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


ls(cur_path)
with open("D:\\Git\Python-projects\\Cryptoserv opt\\Server\\TF\\Capybara.jpg", "r") as f:
    data = f.read()
    print(data)



