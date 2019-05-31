import os
import getpass
# Must use admin cmd
# you can also type directly in an admin cmd "net user [acct name] *" to change the acct passw
user = getpass.getuser()
os.system("net user {} *".format(user))
