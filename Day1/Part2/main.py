# Importing Libraries
from itertools import combinations

# Initializing the expense report list
expense_report = []

# Reading from the input file
with open('input.txt', 'r') as f:
    for line in f:
        expense_report.append(int(line.strip()))

# For each distinct triplet of expenses
for triplet in combinations(expense_report, 3):
    if sum(triplet) == 2020:
        print("The Expenses:", triplet[0], triplet[1], triplet[2])
        print("The Required Product:", triplet[0] * triplet[1] * triplet[2])