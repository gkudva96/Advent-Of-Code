# Importing Libraries
from argparse import ArgumentParser

# Function definition for parsing input file
def parse_input_file(args):
    directory_sizes = {}
    history_stack = []
    with open(args.input_file_path, 'r') as f:
        for line in f.readlines():
            line_comp = line.strip().split()
            if line_comp[0] == '$':
                if line_comp[1] == 'cd':
                    if line_comp[2] == '/' and line_comp[2] not in directory_sizes:
                        history_stack.append(line_comp[2])
                        directory_sizes[tuple([line_comp[2]])] = 0
                    elif line_comp[2] == '/' and line_comp[2] in directory_sizes:
                        history_stack = ['/']
                    elif line_comp[2] == '..':
                        del history_stack[-1]
                    elif line_comp[2] != '/' and line_comp[2] != '..':
                        history_stack.append(line_comp[2])
                        directory_sizes[tuple([x for x in history_stack])] = 0
            else:
                if line_comp[0] != 'dir':
                    for x in range(len(history_stack)):
                        directory_sizes[tuple([y for y in history_stack[0 : x + 1]])] += int(line_comp[0])
    return directory_sizes

# Function definition for part 1
def part_1(directory_sizes):
    return sum([v for v in directory_sizes.values() if v <= 100000])

# Function definition for part 2
def part_2(directory_sizes):
    unused_space = 70000000 - directory_sizes[('/',)]
    directory_sizes_sorted = dict(sorted(directory_sizes.items(), key = lambda item : item[1]))
    smallest_directory_size = [v for k, v in directory_sizes_sorted.items() if unused_space + v >= 30000000][0]
    return smallest_directory_size  

# Primary function definition
def main(args):
    directory_sizes = parse_input_file(args)
    part_1_solution = part_1(directory_sizes)
    print(f"Solution to part 1 : {part_1_solution}")
    part_2_solution = part_2(directory_sizes)
    print(f"Solution to part 2 : {part_2_solution}")

# If the script is invoked as entry-point
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str, default = 'input.txt')
    args = parser.parse_args()
    main(args)