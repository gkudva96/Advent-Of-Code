# Importing Libraries
import numpy as np

# List for storing the instructions
instructions = []

# Reading from input file
with open('input.txt', 'r') as f:
    for line in f:
        instructions.append(line.strip())

# Initializing the coordinates of the ship and the waypoint
ship_coordinates = [0, 0]
waypoint_coordinates = [10, 1]

# For each instruction
for instruction in instructions:

    # Splitting the instruction into character and integer instructions
    char_instruction = instruction[0]
    integer_instruction = int(instruction[1:])

    # If the instruction is to move forward
    if char_instruction == 'F':
        # If the waypoint lies ahead of the ship horizontally
        if waypoint_coordinates[0] >= ship_coordinates[0]:
            x_coordinate_diff = abs(abs(waypoint_coordinates[0]) - abs(ship_coordinates[0]))
        # If the waypoint lies behind the ship horizontally
        else:
            x_coordinate_diff = -abs(abs(waypoint_coordinates[0]) - abs(ship_coordinates[0]))
        # If the waypoint lies ahead of the ship vertically
        if waypoint_coordinates[1] >= ship_coordinates[1]:
            y_coordinate_diff = abs(abs(waypoint_coordinates[1]) - abs(ship_coordinates[1]))
        # If the waypoint lies behind the ship vertically
        else:
            y_coordinate_diff = -abs(abs(waypoint_coordinates[1]) - abs(ship_coordinates[1]))
        # Determining the new ship coordinates
        ship_coordinates[0] += x_coordinate_diff * integer_instruction
        ship_coordinates[1] += y_coordinate_diff * integer_instruction
        # Determining the new waypoint coordinates
        waypoint_coordinates[0] = ship_coordinates[0] + x_coordinate_diff
        waypoint_coordinates[1] = ship_coordinates[1] + y_coordinate_diff

    # If the instruction is to move east
    if char_instruction == 'E':
        waypoint_coordinates[0] += integer_instruction
    
    # If the instruction is to move west
    if char_instruction == 'W':
        waypoint_coordinates[0] -= integer_instruction

    # If the instruction is to move north
    if char_instruction == 'N':
        waypoint_coordinates[1] += integer_instruction
    
    # If the instruction is to move south
    if char_instruction == 'S':
        waypoint_coordinates[1] -= integer_instruction

    # If the instruction is to rotate right (clockwise)
    if char_instruction in ['R', 'L']:
        # Determining the sign of the degrees
        integer_instruction = -integer_instruction if char_instruction == 'R' else integer_instruction
        # Assigning temporary variables
        temp_x, temp_y = waypoint_coordinates[0], waypoint_coordinates[1]
        # Subtracting the point of rotation
        temp_x -= ship_coordinates[0]
        temp_y -= ship_coordinates[1]
        # Rotating the point by the angle and adding the offset
        waypoint_coordinates[0] = temp_x * np.cos(np.deg2rad(integer_instruction)) - \
            temp_y * np.sin(np.deg2rad(integer_instruction)) + ship_coordinates[0]
        waypoint_coordinates[1] = temp_x * np.sin(np.deg2rad(integer_instruction)) + \
            temp_y * np.cos(np.deg2rad(integer_instruction)) + ship_coordinates[1]

# Obtaining the Manhattan Distance
print("Manhattan Distance:", abs(ship_coordinates[0]) + abs(ship_coordinates[1]))       