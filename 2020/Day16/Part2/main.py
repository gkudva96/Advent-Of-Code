# Importing Libraries
import numpy as np
from collections import defaultdict

# Variable to keep track of the number of new lines encountered
new_lines_count = 0

# Dictionary to keep track of the rules and their respective valid numbers
rules_dict = defaultdict(set)

# Dictionary to keep track of the rule position on the ticket
rules_to_pos, pos_to_rules = defaultdict(lambda : 0), defaultdict(lambda : "")

# Set to store the valid numbers
valid_numbers = set()

# List to store our ticket numbers
personal_ticket = []

# List to store the nearby ticket numbers
nearby_tickets = []

# Reading from the input file
with open('input.txt', 'r') as f:
    # For each line in the file
    for line in f:
        # If the line is a new line
        if line == '\n':
            # Incrementing the count
            new_lines_count += 1
        # Otherwise
        else:
            # Obtaining the rules
            if new_lines_count == 0:
                # Splitting the line
                rule = line.strip().split(':')
                # Obtaining the rule name
                rule_name = rule[0]
                # Obtaining the ranges
                ranges = rule[1].strip().split()
                range1_l, range1_r = map(int, ranges[0].split('-'))
                range2_l, range2_r = map(int, ranges[2].split('-'))
                # Adding the numbers in the ranges to the set of valid numbers
                rules_dict[rule_name].update([x for x in range(range1_l, range1_r + 1)])
                rules_dict[rule_name].update([x for x in range(range2_l, range2_r + 1)])
            # Obtaining my ticket
            elif new_lines_count == 1:
                # If the line contains the sentence "your ticket"
                if line.strip().startswith('your ticket:'):
                    continue
                # Obtaining your ticket numbers
                else:
                    personal_ticket = list(map(int, line.strip().split(',')))
            # Obtaining nearby tickets
            elif new_lines_count > 1:
                # If the line contains the sentence "nearby tickets"
                if line.strip().startswith('nearby tickets'):
                    continue
                # Obtaining nearby ticket numbers
                else:
                    nearby_tickets.append(list(map(int, line.strip().split(','))))

# Converting the nearby tickets list to a numpy array
nearby_tickets = np.array(nearby_tickets)

# Discarding the tickets containing invalid values
valid_numbers = set()
for range_set in rules_dict.values():
    valid_numbers.update(range_set)
nearby_tickets_invalid_mask = np.logical_not(np.isin(nearby_tickets, list(valid_numbers))).any(axis = 1)
nearby_tickets_valid = nearby_tickets[np.logical_not(nearby_tickets_invalid_mask)]

# Determining the validity of each rule for each position
rules_validity, idx_count = [], 0
for rule in rules_dict:
    rules_validity.append((np.isin(nearby_tickets_valid, list(rules_dict[rule])).all(axis = 0)).tolist())
    pos_to_rules[str(idx_count)] = rule
    idx_count += 1
rules_validity = np.array(rules_validity)

# Determining the final position of each rule
while rules_validity.any():
    # Go through each row of the matrix
    for row_idx in range(rules_validity.shape[0]):
        row_list = rules_validity[row_idx].tolist()
        if row_list.count(True) == 1:
            rules_to_pos[pos_to_rules[str(row_idx)]] = row_list.index(True)
            rules_validity[:, row_list.index(True)] = False

# Printing the final product
product = 1
for rule in rules_to_pos:
    if rule.startswith('departure'):
        product *= personal_ticket[rules_to_pos[rule]]
print(f"Departure Product : {product}")