# Importing Libraries
from argparse import ArgumentParser
import string

# Dictionary to map priorities
priority = {x : y for x, y in zip(list(string.ascii_letters), [z for z in range(1, 53)])}

# Function definition for part 1
def part_1(args):
    with open(args.input_file_path, 'r') as f:
        common_item_priorities = [priority[set(l.strip()[0 : len(l.strip()) // 2]).intersection(set(l.strip()[len(l.strip()) // 2 : ])).pop()] for l in f.readlines()]
    return sum(common_item_priorities)

# Function definition for part 2
def part_2(args):
    with open(args.input_file_path, 'r') as f:
        lines = f.readlines()
        common_item_priorities = [priority[set(lines[l_index].strip()).intersection(set(lines[l_index + 1].strip())).intersection(set(lines[l_index + 2].strip())).pop()] for l_index in range(0, len(lines), 3)]
    return sum(common_item_priorities)

# Primary function definition
def main(args):
    part_1_solution = part_1(args)
    print(f"Solution to part 1 : {part_1_solution}")
    part_2_solution = part_2(args)
    print(f"Solution to part 2 : {part_2_solution}")

# If the script is invoked as entry-point
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str, default = 'input.txt')
    args = parser.parse_args()
    main(args)