import os
import pickle
files_serv = os.listdir()
# [print(i) for i in files_serv]
pckg = pickle.dumps(files_serv)
print("pickled list", pckg)
pckg = pickle.loads(pckg)
print("unpickled list", pckg)

