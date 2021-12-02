# Importing Libraries
import numpy as np

# Reading the input file
tree_map = []
with open('input.txt', 'r') as f:
    for line in f:
        temp = list(line.strip())
        tree_map.append(temp)
tree_map = np.array(tree_map)

# Accumulator for tree count
tot_trees = 0

# Initializing the starting coordinates
row_pos, col_pos = 0, 0

# Until the last row is passed
while True:
    col_pos = (col_pos + 3) % (tree_map.shape[1])
    row_pos += 1
    if row_pos == tree_map.shape[0]:
        break
    else:
        if tree_map[row_pos][col_pos] == '#':
            tot_trees += 1

# Displaying the total number of trees encountered
print("Total Trees Encountered:", tot_trees)