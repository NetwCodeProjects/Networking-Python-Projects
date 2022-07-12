import math
# calculate \\
# 
# 
# 
# 
# 
# 
# Population Standard Deviation, mean, and Coefficiant variation (CV)

#create list for input data
data = []
#list for sum of floats in list trick
sqrsum = []

#number of elements input
n = int(input("Enter number of elements : "))
  
#iterating list range 0 to n
for i in range(0, n):
    # input data elements
    ele = float(input())
    # append data elements to list
    data.append(ele)

# calculate mean
mean = sum(data) / len(data)

# for item x in data 
for x in data:
    # Subtract x by mean, square, and add to list
    subtmean = sqrsum.append((x - mean) ** 2)
# fsum provides sum of all floats in list sqrsum
sum = math.fsum(sqrsum)
# calculate mean of subtmean
sqrmean = sum / n
# sqrroot of sqrsum[] mean produces stdev
# this is the stdev
sqrt = math.sqrt(sqrmean)

# calculate coefficient of Varitaion
cv = (sqrt / mean) * 100

# print results
print("---------------------------")
print(f"[+] The Standard Deviation is {sqrt}")
print(f"[+] The mean is {mean}")
print(f"[+] The CV (Coefficiant of variation) is {cv} %")
print("----------------------------------")