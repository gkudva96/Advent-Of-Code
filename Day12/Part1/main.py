# List for storing the instructions
instructions = []

# Reading from input file
with open('input.txt', 'r') as f:
    for line in f:
        instructions.append(line.strip())

# List of directions and their integer signs
directions = ['E', 'S', 'W', 'N']
directions_sign = [1, -1, -1, 1]

# Starting from the East direction
current_direction, current_direction_idx = directions[0], 0

# Initializing the units moved in each direction
east_or_west, north_or_south = 0, 0

# For each instruction
for instruction in instructions:
    
    # Splitting the instruction into character and integer instructions
    char_instruction = instruction[0]
    integer_instruction = int(instruction[1:])

    # If the instruction is to move forward
    if char_instruction == 'F':
        if current_direction in ['E', 'W']:
            east_or_west += directions_sign[directions.index(current_direction)] * integer_instruction
        if current_direction in ['N', 'S']:
            north_or_south += directions_sign[directions.index(current_direction)] * integer_instruction
    
    # If the instruction is to move a certain number of units in the East or West
    elif char_instruction in ['E', 'W']:
        east_or_west += directions_sign[directions.index(char_instruction)] * integer_instruction

    # If the instruction is to move a certain number of units in the North or South
    elif char_instruction in ['N', 'S']:
        north_or_south += directions_sign[directions.index(char_instruction)] * integer_instruction

    # If the instruction is to rotate a certain number of degrees to the right
    elif char_instruction == 'R':
        current_direction_idx = (current_direction_idx + (integer_instruction // 90)) % 4
        current_direction = directions[current_direction_idx]

    # If the instruction is to rotate a certain number of degrees to the left
    elif char_instruction == 'L':
        current_direction_idx = (current_direction_idx - (integer_instruction // 90)) % 4
        current_direction = directions[current_direction_idx]

# Obtaining the Manhattan Distance
print("Manhattan Distance:", abs(east_or_west) + abs(north_or_south))       