# Importing Libraries
from argparse import ArgumentParser
import numpy

# Helper function definitions
def parse_input(input_file_path):
    point_locations, fold_instructions, end_of_point_locations = [], [], False
    with open(input_file_path, 'r') as f:
        for line in f.readlines():
            if line != '\n':
                if not end_of_point_locations:
                    point_locations.append(list(map(int, line.strip().split(','))))
                else:
                    fold_instructions.append(line.strip().split(' ')[-1])
            else:
                end_of_point_locations = True
    return point_locations, fold_instructions

def part_1_2(point_locations, fold_instructions):
    part_1_solution, part_2_solution, num_instructions = None, None, len(fold_instructions)
    max_point_coords = numpy.max(point_locations, axis = 0)
    point_grid = numpy.zeros((max_point_coords[1] + 1, max_point_coords[0] + 1))
    point_grid[point_locations[:, 1], point_locations[:, 0]] = 1
    for idx, fold_instruction in enumerate(fold_instructions):
        hor_or_ver, line_num = fold_instruction.split('=')
        temp_point_grid_shape = point_grid.shape
        if hor_or_ver == 'x':
            offset = min(int(line_num) - 0, (temp_point_grid_shape[1] - 1) - int(line_num))
            point_grid[:, 0 : 0 + offset] += point_grid[:, int(line_num) + offset : int(line_num) : -1]
            point_grid = point_grid[:, 0 : 0 + offset]
        elif hor_or_ver == 'y':
            offset = min(int(line_num) - 0, (temp_point_grid_shape[0] - 1) - int(line_num))
            point_grid[0 : 0 + offset, :] += point_grid[int(line_num) + offset : int(line_num) : -1, :]
            point_grid = point_grid[0 : 0 + offset, :]
        point_grid[point_grid >= 1] = 1
        if idx == 0:
            part_1_solution = numpy.sum(point_grid)
        if idx == num_instructions - 1:
            part_2_solution = point_grid
    return part_1_solution, part_2_solution

# Primary function definition
def main(args):
    # Parsing the input text file
    point_locations, fold_instructions = parse_input(args.input_file_path)
    # Obtaining the solutions to Part 1 and 2
    part_1_solution, part_2_solution = part_1_2(numpy.array(point_locations), fold_instructions)
    # Displaying the solution
    print(f"Part 1 Solution : \n{part_1_solution}")
    print(f"Part 2 Solution : \n{part_2_solution.astype(numpy.uint8)}")

# If the script is invoked as entrypoint
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str)
    args = parser.parse_args()
    main(args)