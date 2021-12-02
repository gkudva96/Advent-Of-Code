# Importing Libraries
from argparse import ArgumentParser

# Helper function definitions
def parse_input(input_file_path):
    with open(input_file_path, 'r') as f:
        measurements = [int(line.strip()) for line in f.readlines()]
    return measurements

def part_1(measurements):
    increment_count = sum([1 if measurements[x] > measurements[x - 1] else 0 for x in range(1, len(measurements))])
    return increment_count

def part_2(measurements):
    measurements = [sum(measurements[x : x + 3]) for x in range(0, len(measurements) - 2)]
    increment_count = part_1(measurements)
    return increment_count

# Primary function definition
def main(args):
    # Parsing the input text file
    measurements = parse_input(args.input_file_path)
    # Solving Part 1
    part_1_solution = part_1(measurements)
    # Solving Part 2
    part_2_solution = part_2(measurements)
    # Displaying the solutions
    print(f"Part 1 Solution : {part_1_solution}\nPart 2 Solution : {part_2_solution}")

# If the script is invoked as entrypoint
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str, default = 'input.txt')
    args = parser.parse_args()
    main(args)