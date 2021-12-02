# Importing libraries
from collections import Counter

# Accumulator for the count
total_count = 0

# Loading from input file
with open('input.txt', 'r') as f:
    # Temporary list and number of persons in each group
    group_list, group_count = [], 0
    # For each line in the file
    for line in f:
        # For each member of a group
        if line != '\n':
            group_list += list(line.strip())
            group_count += 1
        # When end of group is encountered
        else:
            group_dict = Counter(group_list)
            for key in group_dict:
                if group_dict[key] == group_count:
                    total_count += 1
            group_list, group_count = [], 0
    # Adding the count of the last group
    group_dict = Counter(group_list)
    for key in group_dict:
        if group_dict[key] == group_count:
            total_count += 1

# Printing the result
print("Total Count:", total_count)