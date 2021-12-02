# Importing Libraries
from itertools import combinations

# List to store the numbers
numbers = []

# Reading from input file
with open('input.txt', 'r') as f:
    # For each line in the file
    for line in f:
        numbers.append(int(line.strip()))

# Determining the number after the preamble that does not meet the XMAS property
low_index, high_index = 0, 24
for i in range(25, len(numbers)):
    xmas_flag = False
    for pair in combinations(numbers[low_index : high_index + 1], 2):
        if sum(pair) == numbers[i]:
            xmas_flag = True
            break
    if not xmas_flag:
        print("Required Number:", numbers[i])
        break
    low_index += 1
    high_index += 1    