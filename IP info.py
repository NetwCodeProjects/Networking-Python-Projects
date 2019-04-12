import netaddr
import socket
from netaddr import IPAddress

# Allow user input for ip
print("what is the ip?")
addr = input()
# reverse DNS
dns = socket.gethostbyaddr(addr)
# Define ip
ip = IPAddress(addr)
net = IPAddress(addr)
# Print info
print("IP version -", ip.version)
print("private -", ip.is_private())
print("unicast -", ip.is_unicast())
print("multicast -", ip.is_multicast())
print("IP in bits -", ip.bits())
print("reverse dns -", dns)
