# Import socket
import socket 

# Accept user input
print("Enter website address:")
hostName = input()

# Get the local host name
myHostName = socket.gethostname()

# Get the IP address of the local host
myIP = socket.gethostbyname(myHostName)

# If user inputs "local", Host name and host IP will be displayed
if hostName == "local":
	print("Name of the localhost is {}".format(myHostName))
	print("IP address of the localhost is {}".format(myIP))
# Else program will provide IP for inputed website address
else:
	# use input to get IP
	ipAddress = socket.gethostbyname(hostName)
	# print the information
	print("IP address of {} is: {}".format(hostName, ipAddress))