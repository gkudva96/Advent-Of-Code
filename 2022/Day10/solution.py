# Importing Libraries
from argparse import ArgumentParser
import numpy as np

# Function definition to parse input file
def parse_input_file(args):
    with open(args.input_file_path, 'r') as f:
        instructions = [line.strip().split() for line in f.readlines()]
    return instructions

# Function definition for part 1
def part_1(instructions):
    cycle_register_values = []
    register = 1
    for instruction in instructions:
        if instruction[0] == 'addx':
            cycle_register_values += [register] * 2
            register += int(instruction[1])
        elif instruction[0] == 'noop':
            cycle_register_values += [register]
    return sum([cycle_register_values[i] * (i + 1) for i in [j for j in range(19, 19 + 6 * 40, 40)]])

# Function definition for part 2
def part_2(instructions):
    register = 1
    sprite_range = {register - 1, register, register + 1}
    crt_row_num, crt_col_num = 0, 0
    image = np.zeros((6, 40))
    for instruction in instructions:
        if instruction[0] == 'addx':
            for i in range(2):
                if crt_col_num in sprite_range:
                    image[crt_row_num, crt_col_num] = 1
                else:
                    image[crt_row_num, crt_col_num] = 0
                crt_col_num += 1
                if crt_col_num == image.shape[1]:
                    crt_row_num = (crt_row_num + 1) % image.shape[0]
                    crt_col_num = 0
            register += int(instruction[1])
            sprite_range = {register - 1, register, register + 1}
        elif instruction[0] == 'noop':
            if crt_col_num in sprite_range:
                image[crt_row_num, crt_col_num] = 1
            else:
                image[crt_row_num, crt_col_num] = 0
            crt_col_num += 1
            if crt_col_num == image.shape[1]:
                crt_row_num = (crt_row_num + 1) % image.shape[0]
                crt_col_num = 0
    image_string = []
    for r in range(image.shape[0]):
        for c in range(image.shape[1]):
            image_string.append('#') if image[r, c] == 1 else image_string.append('.')
        image_string.append('\n')
    return ''.join(image_string)

# Primary function definition
def main(args):
    instructions = parse_input_file(args)
    part_1_solution = part_1(instructions)
    print(f"Solution to part 1 : {part_1_solution}")
    part_2_solution = part_2(instructions)
    print(f"Solution to part 2 : \n{part_2_solution}")

# If the script is invoked as entry-point
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str, default = 'input.txt')
    args = parser.parse_args()
    main(args)