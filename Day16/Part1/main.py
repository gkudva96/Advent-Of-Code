# Importing Libraries
import numpy as np

# Variable to keep track of the number of new lines encountered
new_lines_count = 0

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
                rule = rule[1].strip().split()
                # Obtaining the ranges
                range1_l, range1_r = map(int, rule[0].split('-'))
                range2_l, range2_r = map(int, rule[2].split('-'))
                # Adding the numbers in the ranges to the set of valid numbers
                valid_numbers.update([x for x in range(range1_l, range1_r + 1)])
                valid_numbers.update([x for x in range(range2_l, range2_r + 1)])
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

# Obtaining the invalid values
nearby_tickets_invalid = nearby_tickets[~np.isin(nearby_tickets, list(valid_numbers))]

# Obtaining the ticket scanning error rate
print(f"Ticket Scanning Error Rate : {np.sum(nearby_tickets_invalid)}")