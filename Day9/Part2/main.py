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
low_index, high_index, required_number = 0, 24, 0
for i in range(25, len(numbers)):
    xmas_flag = False
    for pair in combinations(numbers[low_index : high_index + 1], 2):
        if sum(pair) == numbers[i]:
            xmas_flag = True
            break
    if not xmas_flag:
        required_number = numbers[i]
        break
    low_index += 1
    high_index += 1

# Determining the encryption weakness
for combination_length in range(2, len(numbers)):
    range_found_flag = False
    for i in range(0, len(numbers) - combination_length):
        temp_range = numbers[i : i + combination_length]
        if sum(temp_range) == required_number:
            print(f"Encryption Weakness: {min(temp_range) + max(temp_range)}")
            range_found_flag = True
            break
    if range_found_flag:
        break