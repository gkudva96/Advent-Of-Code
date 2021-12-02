# Constant to define the total bitsize
BITSIZE = 36

# Dictionary to map mem locations to list indices
mem_to_idx = {}

# List to store the values at memory locations
values = []

# Loading from file
with open('input.txt', 'r') as f:

    # Initializing the mask and index counter
    mask, idx = None, 0

    # For each line
    for line in f:

        # Obtaining the components of the line
        line_components = line.strip().split()

        # If the line is a bitmask declaration
        if line_components[0].startswith('mask'):
            mask = line_components[2]

        # If the line is a memory value allocation
        elif line_components[0].startswith('mem'):
            
            # Obtaining the memory location
            mem_loc = line_components[0][4 : -1]

            # Obtaining the value to be assigned
            value = bin(int(line_components[2]))[2:]
            value = '0' * (BITSIZE - len(value)) + value

            # If the memory location is encountered for the first time
            if mem_loc not in mem_to_idx:
                mem_to_idx[mem_loc] = idx
                values.append('0' * BITSIZE)
                idx += 1
            
            # Updating the value at the memory location
            values[mem_to_idx[mem_loc]] = ''.join([value[i] if mask[i] == 'X' else mask[i] for i in range(len(mask))])

# Computing the final sum
print(f"Sum : {sum(list(map(lambda x : int(x, 2), values)))}")