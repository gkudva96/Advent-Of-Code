# Importing Libraries
from argparse import ArgumentParser
import numpy as np

# Dictionary to map offset
offset_dict = {'L' : (-1, 0), 'R' : (1, 0), 'U' : (0, 1), 'D' : (0, -1), 'LU' : (-1, 1), 'RU' : (1, 1), 'LD' : (-1, -1), 'RD' : (1, -1)}

# Function definition for parsing input file
def parse_input_file(args):
    with open(args.input_file_path, 'r') as f:
        instructions = [tuple(line.strip().split()) for line in f.readlines()]
    return instructions

# Function definition to return the neighbourhood positions of the head knot
def get_neighbourhood(knot_pos, size):
    neighbourhood = set()
    neighbourhood.update([tuple(np.array(knot_pos) + np.array([i, j])) for i in range( - (size // 2), (size // 2) + 1) for j in range(- (size // 2), (size // 2) + 1)])
    return neighbourhood

# Function definition to check if head and tail knots are adjacent
def is_adjacent(prev_knot_pos, next_knot_pos, size):
    neighbourhood = get_neighbourhood(prev_knot_pos, size)
    return True if next_knot_pos in neighbourhood else False

# Function to move the subsequent knot
def move_subsequent_knot(prev_knot_pos, next_knot_pos, size):
    if is_adjacent(prev_knot_pos, next_knot_pos, size):
        pass
    else:
        if (prev_knot_pos[0] == next_knot_pos[0]) and (prev_knot_pos[1] > next_knot_pos[1]):
            next_knot_pos = tuple(np.array(next_knot_pos) + np.array(offset_dict['U']))
        elif (prev_knot_pos[0] == next_knot_pos[0]) and (prev_knot_pos[1] < next_knot_pos[1]):
            next_knot_pos = tuple(np.array(next_knot_pos) + np.array(offset_dict['D']))
        elif (prev_knot_pos[0] < next_knot_pos[0]) and (prev_knot_pos[1] == next_knot_pos[1]):
            next_knot_pos = tuple(np.array(next_knot_pos) + np.array(offset_dict['L']))
        elif (prev_knot_pos[0] > next_knot_pos[0]) and (prev_knot_pos[1] == next_knot_pos[1]):
            next_knot_pos = tuple(np.array(next_knot_pos) + np.array(offset_dict['R']))
        elif (prev_knot_pos[1] > next_knot_pos[1]) and (prev_knot_pos[0] > next_knot_pos[0]):
            next_knot_pos = tuple(np.array(next_knot_pos) + np.array(offset_dict['RU']))
        elif (prev_knot_pos[1] > next_knot_pos[1]) and (prev_knot_pos[0] < next_knot_pos[0]):
            next_knot_pos = tuple(np.array(next_knot_pos) + np.array(offset_dict['LU']))
        elif (prev_knot_pos[1] < next_knot_pos[1]) and (prev_knot_pos[0] > next_knot_pos[0]):
            next_knot_pos = tuple(np.array(next_knot_pos) + np.array(offset_dict['RD']))
        elif (prev_knot_pos[1] < next_knot_pos[1]) and (prev_knot_pos[0] < next_knot_pos[0]):
            next_knot_pos = tuple(np.array(next_knot_pos) + np.array(offset_dict['LD']))
    return next_knot_pos

# Function definition for part 1
def part_1_2(instructions, size, num_knots):
    knot_positions = [(0, 0) for i in range(num_knots)]
    tail_positions = set()
    tail_positions.add(knot_positions[-1])
    for instruction in instructions:
        for _ in range(int(instruction[1])):
            knot_positions[0] = tuple(np.array(knot_positions[0]) + np.array(offset_dict[instruction[0]]))
            for i in range(1, num_knots):
                knot_positions[i] = move_subsequent_knot(knot_positions[i - 1], knot_positions[i], size)
            tail_positions.add(knot_positions[-1])
    return len(tail_positions)

# Primary function definition
def main(args):
    instructions = parse_input_file(args)
    part_1_solution = part_1_2(instructions, 3, 2)
    print(f"Solution to part 1 : {part_1_solution}")
    part_2_solution = part_1_2(instructions, 3, 10)
    print(f"Solution to part 2 : {part_2_solution}")

# If the script is invoked as entry-point
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str, default = 'input.txt')
    args = parser.parse_args()
    main(args)