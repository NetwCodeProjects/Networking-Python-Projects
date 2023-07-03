import math
from itertools import permutations

def is_special_permutation(word):
    for i in range(len(word)):
        if word[i] == str(i):
            return False
    return True

def count_special_permutations(word):
    n = len(word)
    k_values = {}
    for char in word:
        if char in k_values:
            k_values[char] += 1
        else:
            k_values[char] = 1

    total_special_permutations = math.factorial(n)
    for k in k_values.values():
        total_special_permutations //= math.factorial(k)

    count = 0
    perm_list = []
    for perm in permutations(word):
        if is_special_permutation(perm):
            count += 1
            perm_list.append("".join(perm))

    return total_special_permutations, count, perm_list

def calculate_permutations(n, r):
    permutations = math.factorial(n) // math.factorial(n - r)
    return permutations

def calculate_combinations(n, r):
    combinations = math.comb(n, r)
    return combinations

word = input("Enter a word: ")

total_special_permutations, count, perm_list = count_special_permutations(word)
print("Total special permutations:", total_special_permutations)

choice = input("Which version would you like to print? (nPr/nCr/sp): ")

if choice.lower() == "npr":
    r = int(input("Enter the value of r: "))
    permutations_r = calculate_permutations(len(word), r)
    print("Number of permutations (nPr) for r =", r, ":", permutations_r)
    
elif choice.lower() == "ncr":
    n = len(word)
    r = int(input("Enter the value of r: "))
    combinations_r = calculate_combinations(n, r)
    print("Number of combinations (nCr) for r =", r, ":", combinations_r)

elif choice.lower() == "sp":
    print("Special Permutations:")
    for perm in perm_list:
        print(perm)
else:
    print("Invalid choice.")
