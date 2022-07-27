import os


def list(args=None):
    files_serv = '\n'.join(os.listdir(args)) + "\n"
    print(files_serv)


# with open("test_folder" + "/test_txt.txt", "r") as f:
#     data = f.read()
# print(data)
cur_path = os.path.dirname(__file__)
print("cp:", cur_path)
new_path = os.path.relpath("/test_folder/TF2", cur_path)
print(new_path)
list(new_path)
