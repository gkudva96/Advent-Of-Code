# Accumulator variable for total number of valid passports
val_passports = 0

# Initializing a temporary list for the keys
temp_key_list = []

# Reading from the input file
with open('input.txt', 'r') as f:
    # For each line in the file
    for line in f:
        # If the line is not a blank line
        if line != '\n':
            temp_key_list += [x.split(':')[0] for x in line.strip().split()]
        # If the line is a blank line (marks the end of one passport)
        else:
            temp_key_list_len = len(temp_key_list)
            # If all the 8 fields are present
            if temp_key_list_len == 8:
                val_passports += 1
            # If all the 8 fields are not present
            elif temp_key_list_len < 8:
                # If 'cid' is the only missing field
                if temp_key_list_len == 7 and 'cid' not in temp_key_list:
                    val_passports += 1
            # Re-initializing the temporary key list
            temp_key_list = []

# Printing the total number of valid passports
print("Total Number of Valid Passports:", val_passports)