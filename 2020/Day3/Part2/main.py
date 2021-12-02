# Importing Libraries
import numpy as np

# Reading the input file
tree_map = []
with open('input.txt', 'r') as f:
    for line in f:
        temp = list(line.strip())
        tree_map.append(temp)
tree_map = np.array(tree_map)

# Initializing the list of given slopes to test
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

# Accumulator for the tree counts per slope
tot_trees = []

# Testing each slope
for pair in slopes:

    # Initializing the starting coordinates
    row_pos, col_pos = 0, 0

    # Temporary accumulator for tree count
    temp_count = 0

    # Until the last row is passed
    while row_pos < tree_map.shape[0]:
        if tree_map[row_pos][col_pos] == '#':
                temp_count += 1
        col_pos = (col_pos + pair[0]) % (tree_map.shape[1])
        row_pos += pair[1]
            
    # Adding to the tree count accumulator list
    tot_trees.append(temp_count)

# Displaying the product of the total number of trees encountered per slope
final_prod = 1
for tree_count in tot_trees:
    final_prod *= tree_count
print("Required Product of Total Tree Counts per Slope:", final_prod)