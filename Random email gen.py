# Importing random to generate  
# random string sequence  
import random  
     
# Importing string library function  
import string

# Create input for password length
print("How many characters")
quantity = input()
     
def rand_pass(size):  
         
    # Takes random choices from  
    # ascii_letters and digits  
    generate_pass = ''.join([random.choice( string.ascii_uppercase +
                                            string.ascii_lowercase +
                                            string.digits )
                                            for n in range(size)])  
                             
    return generate_pass  
     
# Driver Code   
password = rand_pass(int(quantity)) 
print(password + "@" + password + ".com")  