# Accumulator for the count
total_count = 0

# Loading from input file
with open('input.txt', 'r') as f:
    # Temporary list for each group
    group_list = []
    # For each line in the file
    for line in f:
        # For each member of a group
        if line != '\n':
            group_list += list(line.strip())
        # When end of group is encountered
        else:
            total_count += len(set(group_list))
            group_list = []
    # Adding the count of the last group
    total_count += len(set(group_list))

# Printing the result
print("Total Count:", total_count)