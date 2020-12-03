# Importing Libraries
from itertools import combinations

# Initializing the expense report list
expense_report = []

# Reading from the input file
with open('input.txt', 'r') as f:
    for line in f:
        expense_report.append(int(line.strip()))

# For each distinct pair of expenses
for pair in combinations(expense_report, 2):
    if sum(pair) == 2020:
        print(pair[0] * pair[1])