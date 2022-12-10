# Importing Libraries
from argparse import ArgumentParser
import re

# Function definition for parsing input file
def parse_input(input_file_path):
    stack_arrangement, arrangement_instructions = [], []
    switch_flag = True
    with open(input_file_path, 'r') as f:
        for line in f.readlines():
            if line.strip() != '':
                if switch_flag:
                    stack_arrangement.append([re.sub('\[|\]', '', line[x : x + 4].strip()) for x in range(0, len(line), 4)])
                else:
                    arrangement_instructions.append(list(map(int, re.sub('[a-zA-Z]', '', line.strip()).split())))
            else:
                switch_flag = False
    return stack_arrangement, arrangement_instructions

# Function definition for parts 1 & 2
def part_1_2(stack_arrangement, arrangement_instructions, keep_order):
    stacks = [[y[int(x) - 1] for y in stack_arrangement[:-1] if y[int(x) - 1] != ''] for x in stack_arrangement[-1]]
    for instruction in arrangement_instructions:
        popped_crates = stacks[instruction[1] - 1][:instruction[0]]
        del stacks[instruction[1] - 1][:instruction[0]]
        if not keep_order:
            stacks[instruction[2] - 1] = popped_crates[::-1] + stacks[instruction[2] - 1]
        else:
            stacks[instruction[2] - 1] = popped_crates + stacks[instruction[2] - 1]
    return ''.join([stack[0] for stack in stacks])

# Primary function definition
def main(args):
    stack_arrangement, arrangement_instructions = parse_input(args.input_file_path)
    part_1_solution = part_1_2(stack_arrangement, arrangement_instructions, False)
    print(f"Solution to part 1 : {part_1_solution}")
    part_2_solution = part_1_2(stack_arrangement, arrangement_instructions, True)
    print(f"Solution to part 2 : {part_2_solution}")

# If the script is invoked as entry-point
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str, default = 'input.txt')
    args = parser.parse_args()
    main(args)