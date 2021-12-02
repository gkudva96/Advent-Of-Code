# Importing Libraries
import numpy as np

# Function definition to obtain the 8 neighbours
def get_neighbours(row, col, arrangement):

    # Initializing the list of neighbours
    neighbours = ['.' for x in range(8)]

    # Obtaining the total rows and columns
    (tot_row, tot_col) = arrangement.shape

    # If it is the first row
    if row == 0:
        # If it is the first element
        if col == 0:
            neighbours[4] = arrangement[row][col + 1]
            neighbours[6] = arrangement[row + 1][col]
            neighbours[7] = arrangement[row + 1][col + 1]
        # If it is the last element
        elif col == tot_col - 1:
            neighbours[3] = arrangement[row][col - 1]
            neighbours[5] = arrangement[row + 1][col - 1]
            neighbours[6] = arrangement[row + 1][col]
        # It is is any middle element
        else:
            neighbours[3] = arrangement[row][col - 1]
            neighbours[4] = arrangement[row][col + 1]
            neighbours[5] = arrangement[row + 1][col - 1]
            neighbours[6] = arrangement[row + 1][col]
            neighbours[7] = arrangement[row + 1][col + 1]
    # If it is the last row
    elif row == tot_row - 1:
        # If it is the first element
        if col == 0:
            neighbours[1] = arrangement[row - 1][col]
            neighbours[2] = arrangement[row - 1][col + 1]
            neighbours[4] = arrangement[row][col + 1]
        # If it is the last element
        elif col == tot_col - 1:
            neighbours[0] = arrangement[row - 1][col - 1]
            neighbours[1] = arrangement[row - 1][col]
            neighbours[3] = arrangement[row][col - 1]
        # It is is any middle element
        else:
            neighbours[0] = arrangement[row - 1][col - 1]
            neighbours[1] = arrangement[row - 1][col]
            neighbours[2] = arrangement[row - 1][col + 1]
            neighbours[3] = arrangement[row][col - 1]
            neighbours[4] = arrangement[row][col + 1]
    # If it is the first column
    elif col == 0:
        # If it is any middle element
        neighbours[1] = arrangement[row - 1][col]
        neighbours[2] = arrangement[row - 1][col + 1]
        neighbours[4] = arrangement[row][col + 1]
        neighbours[6] = arrangement[row + 1][col]
        neighbours[7] = arrangement[row + 1][col + 1]
    # If it is the last column
    elif col == tot_col - 1:
        # If it is any middle element
        neighbours[0] = arrangement[row - 1][col - 1]
        neighbours[1] = arrangement[row - 1][col]
        neighbours[3] = arrangement[row][col - 1]
        neighbours[5] = arrangement[row + 1][col - 1]
        neighbours[6] = arrangement[row + 1][col]
    # If it is any other row and column
    else:
        neighbours[0] = arrangement[row - 1][col - 1]
        neighbours[1] = arrangement[row - 1][col]
        neighbours[2] = arrangement[row - 1][col + 1]
        neighbours[3] = arrangement[row][col - 1]
        neighbours[4] = arrangement[row][col + 1]
        neighbours[5] = arrangement[row + 1][col - 1]
        neighbours[6] = arrangement[row + 1][col]
        neighbours[7] = arrangement[row + 1][col + 1]
    
    # Returning the neighbours
    return neighbours

# Matrix to keep track of the seating arrangement
seating_arrangement = []

# Reading from the input file
with open('input.txt', 'r') as f:
    # For each line
    for line in f:
        seating_arrangement.append(list(line.strip()))

# Converting the list of lists into a numpy array
seating_arrangement = np.array(seating_arrangement)
prev_seating_arrangement = seating_arrangement

# Running the loop until there is no more change in seating arrangement
while True:

    # Initializing the next seating arrangement
    next_seating_arrangement = np.full(prev_seating_arrangement.shape, '.', dtype = str)

    # For each seat in the arrangement
    for row in range(prev_seating_arrangement.shape[0]):
        for col in range(prev_seating_arrangement.shape[1]):
            # Obtaining the 8 neighbours of the seat
            neighbours = get_neighbours(row, col, prev_seating_arrangement)
            # Initializing the next status of the seat
            next_seating_arrangement[row][col] = prev_seating_arrangement[row][col]
            # If the current seat is empty
            if prev_seating_arrangement[row][col] == 'L':
                check_empty = True if sum([1 for x in neighbours if x == '#']) == 0 else False
                if check_empty:
                    next_seating_arrangement[row][col] = '#'
            # If the current seat is occupied
            if prev_seating_arrangement[row][col] == '#':
                check_occupied = sum([1 for x in neighbours if x == '#'])
                if check_occupied >= 4:
                    next_seating_arrangement[row][col] = 'L'

    # Exit condition
    if (prev_seating_arrangement == next_seating_arrangement).all():
        print("Number of occupied seats:", np.count_nonzero(next_seating_arrangement == '#'))
        break

    # Updating the seating arrangement
    prev_seating_arrangement = next_seating_arrangement