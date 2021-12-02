# List for storing the boarding passes
boarding_passes = []

# Reading the input file
with open('input.txt', 'r') as f:
    for line in f:
        boarding_passes.append(line.strip())

# List for storing the seat IDs
seat_ids = []

# For each boarding pass
for boarding_pass in boarding_passes:
    # Initializing the range and the total number of rows
    row_low, row_high, row_total = 0, 127, 128
    # Initializing the range and the total number of seats in each row
    seat_low, seat_high, seat_total = 0, 7, 8
    # For each character in the code
    for direction in boarding_pass:
        if direction == 'F':
            row_total = (row_total // 2)
            row_high = row_low + row_total - 1
        if direction == 'B':
            row_total = (row_total // 2)
            row_low = row_high - row_total + 1
        if direction == 'L':
            seat_total = (seat_total // 2)
            seat_high = seat_low + seat_total - 1
        if direction == 'R':
            seat_total = (seat_total // 2)
            seat_low = seat_high - seat_total + 1
    # Determining the seat ID
    seat_ids.append(row_low * 8 + seat_low)

# Printing out the highest seat ID
print("Highest Seat ID:", max(seat_ids))