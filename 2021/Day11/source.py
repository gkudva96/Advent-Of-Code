# Importing Libraries
from argparse import ArgumentParser
import numpy

# Helper function definitions
def parse_input(input_file_path):
    with open(input_file_path, 'r') as f:
        energy_levels = [list(map(int, list(line.strip()))) for line in f.readlines()]
    return numpy.array(energy_levels)

def increment_adjacent(grid, flash_flags, row_pos, col_pos):
    try:
        if flash_flags[row_pos, col_pos] == 0 and row_pos != -1 and col_pos != -1:
            grid[row_pos, col_pos] += 1
    except:
        pass

def part_1_2(energy_levels, num_steps):
    energy_levels_copy, flash_flags = numpy.copy(energy_levels), numpy.zeros_like(energy_levels)
    total_flashes, step_counter = 0, 1
    while True:
        energy_levels_copy += 1
        while True:
            row_idxs, col_idxs = map(list, numpy.where((energy_levels_copy > 9) & (flash_flags == 0)))
            if len(row_idxs) != 0:
                while len(row_idxs) != 0:
                    temp_row, temp_col = row_idxs.pop(), col_idxs.pop()
                    increment_adjacent(energy_levels_copy, flash_flags, temp_row - 1, temp_col - 1)
                    increment_adjacent(energy_levels_copy, flash_flags, temp_row - 1, temp_col)
                    increment_adjacent(energy_levels_copy, flash_flags, temp_row - 1, temp_col + 1)
                    increment_adjacent(energy_levels_copy, flash_flags, temp_row, temp_col + 1)
                    increment_adjacent(energy_levels_copy, flash_flags, temp_row + 1, temp_col + 1)
                    increment_adjacent(energy_levels_copy, flash_flags, temp_row + 1, temp_col)
                    increment_adjacent(energy_levels_copy, flash_flags, temp_row + 1, temp_col - 1)
                    increment_adjacent(energy_levels_copy, flash_flags, temp_row, temp_col - 1)
                    flash_flags[temp_row, temp_col] = 1
                    if step_counter <= num_steps:
                        total_flashes += 1
                    energy_levels_copy[temp_row, temp_col] = 0
            else:
                break
        if flash_flags.sum() == (energy_levels.shape[0] * energy_levels.shape[1]):
            return (total_flashes, step_counter)
        flash_flags[flash_flags == 1] = 0
        step_counter += 1

# Primary function definition
def main(args):
    # Parsing the input text file
    energy_levels = parse_input(args.input_file_path)
    # Obtaining the solutions to Part 1 and 2
    part_1_solution, part_2_solution = part_1_2(energy_levels, args.num_steps)
    # Displaying the solution
    print(f"Part 1 Solution : {part_1_solution}")
    print(f"Part 2 Solution : {part_2_solution}")

# If the script is invoked as entrypoint
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str)
    parser.add_argument('--num_steps', type = int, default = 100)
    args = parser.parse_args()
    main(args)