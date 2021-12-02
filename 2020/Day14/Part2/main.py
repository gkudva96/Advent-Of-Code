# Importing Libraries
import numpy as np

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
            
            # Obtaining the value
            value = int(line_components[2])

            # Obtaining the binary string representation of the memory location
            mem_loc_bs = bin(int(mem_loc))[2:]
            mem_loc_bs = '0' * (BITSIZE - len(mem_loc_bs)) + mem_loc_bs

            # Updating the memory location
            new_mem_loc_bs = np.array([mem_loc_bs[i] if mask[i] == '0' else mask[i] for i in range(len(mask))])

            # Finding the number of locations containing 'X' in the updated memory location 
            num_loc_x = np.sum(new_mem_loc_bs == 'X')

            # Obtaining the new memory locations due to the floating bits
            for x in range(0, 2 ** num_loc_x):

                # Storing the updated memory location in a temporary variable
                temp_new_mem_loc_bs = new_mem_loc_bs.copy()

                # Assigning one of the permutations to each placeholder 'X' 
                temp_new_mem_loc_bs[temp_new_mem_loc_bs == 'X']  = list('0' * (num_loc_x - len(bin(x)[2:])) + bin(x)[2:])
                new_mem_loc = int(''.join(temp_new_mem_loc_bs.tolist()), 2)

                # If the memory location is encountered for the first time
                if new_mem_loc not in mem_to_idx:
                    mem_to_idx[new_mem_loc] = idx
                    values.append(0)
                    idx += 1
                
                # Updating the value at the memory location
                values[mem_to_idx[new_mem_loc]] = value

# Computing the final sum
print(f"Sum : {sum(values)}")