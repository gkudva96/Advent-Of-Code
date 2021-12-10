# Importing Libraries
from argparse import ArgumentParser
import numpy

# Helper function definitions
def parse_input(input_file_path):
    with open(input_file_path, 'r') as f:
        crab_positions = list(map(int, f.readline().split(',')))
    return numpy.array(crab_positions)

def part_1(crab_positions):
    crab_pos_min, crab_pos_max = numpy.min(crab_positions), numpy.max(crab_positions)
    crab_pos_fuel = [numpy.sum(numpy.abs(crab_positions - crab_pos)) for crab_pos in range(crab_pos_min, crab_pos_max + 1)]
    return numpy.min(crab_pos_fuel)

def part_2(crab_positions):
    crab_pos_min, crab_pos_max = numpy.min(crab_positions), numpy.max(crab_positions)
    crab_pos_fuel = []
    for crab_pos in range(crab_pos_min, crab_pos_max + 1):
        crab_pos_diff = numpy.abs(crab_positions - crab_pos)
        crab_pos_diff = (crab_pos_diff * (crab_pos_diff + 1)) // 2
        crab_pos_fuel.append(numpy.sum(crab_pos_diff))
    return numpy.min(crab_pos_fuel)

# Primary function definition
def main(args):
    # Parsing the input text file
    crab_positions = parse_input(args.input_file_path)
    # Obtaining the solution to Part 1
    part_1_solution = part_1(crab_positions)
    # Obtaining the solution to Part 2
    part_2_solution = part_2(crab_positions)
    # Displaying the solution
    print(f"Part 1 Solution : {part_1_solution}")
    print(f"Part 2 Solution : {part_2_solution}")

# If the script is invoked as entrypoint
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str)
    args = parser.parse_args()
    main(args)