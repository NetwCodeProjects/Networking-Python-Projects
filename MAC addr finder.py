# Python 3 code to print MAC in formatted way
import re, uuid 
  
# joins elements of getnode() after each 2 digits. 
# using regex expression 
print ("The MAC address is : ", end="") 
print (':'.join(re.findall('..', '%012x' % uuid.getnode()))) 