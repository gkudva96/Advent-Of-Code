# Importing Libraries
from argparse import ArgumentParser
import numpy

# Dictionary to map the instructions
instruction_mapping_part_1 = {'forward' : numpy.array([1, 0]), \
    'up' : numpy.array([0, -1]), \
    'down' : numpy.array([0, 1])}

instruction_mapping_part_2 = {'forward' : numpy.array([1, 1, 0]), \
    'up' : numpy.array([0, 0, -1]), \
    'down' : numpy.array([0, 0, 1])}

# Helper function definitions
def parse_input(input_file_path):
    with open(input_file_path, 'r') as f:
        instructions = [line.strip().split() for line in f.readlines()]
    return instructions

def part_1(instructions):
    initial_position = numpy.array([0, 0])
    for instruction in instructions:
        initial_position += instruction_mapping_part_1[instruction[0]] * int(instruction[1])
    return initial_position[0] * initial_position[1]

def part_2(instructions):
    initial_position = numpy.array([0, 0, 0])
    for instruction in instructions:
        if instruction[0] != 'forward':
            initial_position += instruction_mapping_part_2[instruction[0]] * int(instruction[1])
        else:
            initial_position += instruction_mapping_part_2[instruction[0]] * numpy.array([int(instruction[1]), \
                int(instruction[1]) * initial_position[2], 0])
    return initial_position[0] * initial_position[1]

# Primary function definition
def main(args):
    # Parsing the input text file
    instructions = parse_input(args.input_file_path)
    # Solving Part 1
    part_1_solution = part_1(instructions)
    # Solving Part 2
    part_2_solution = part_2(instructions)
    # Displaying the solutions
    print(f"Part 1 Solution : {part_1_solution}")
    print(f"Part 2 Solution : {part_2_solution}")

# If the script is invoked as entrypoint
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str)
    args = parser.parse_args()
    main(args)