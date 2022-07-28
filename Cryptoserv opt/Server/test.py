import os


def list(args=None):
    files_serv = '\n'.join(os.listdir(args)) + "\n"
    print(files_serv)


# with open("test_folder" + "/test_txt.txt", "r") as f:
#     data = f.read()
# print(data)
cur_path = os.path.dirname(__file__)
print(cur_path)
list(cur_path)
new_path = cur_path + "\\" + input()
if not os.path.isdir(new_path):
    new_path = cur_path
    print("Not a valid dir")
#  new_path = cur_path + "\\" + input()
print(new_path)
list(new_path)

