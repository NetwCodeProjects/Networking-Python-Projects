import os
import getpass

user = getpass.getuser()
os.system("net user {} *".format(user))