# Importing Libraries
from argparse import ArgumentParser
import numpy

# Helper function definitions
def parse_input(input_file_path):
    height_map = []
    with open(input_file_path, 'r') as f:
        height_map = [list(map(int, list(line.strip()))) for line in f.readlines()]
    return numpy.array(height_map)

def part_1(height_map):
    row_conditions, col_conditions = numpy.zeros_like(height_map), numpy.zeros_like(height_map)
    for i in range(height_map.shape[0]):
        if i == 0:
            row_conditions[i, :] = height_map[i, :] < height_map[i + 1, :]
        elif i == height_map.shape[0] - 1:
            row_conditions[i, :] = height_map[i, :] < height_map[i - 1, :]
        else:
            c1 = height_map[i, :] < height_map[i + 1, :]
            c2 = height_map[i, :] < height_map[i - 1, :]
            row_conditions[i, :] = numpy.logical_and(c1, c2)
    for i in range(height_map.shape[1]):
        if i == 0:
            col_conditions[:, i] = height_map[:, i] < height_map[:, i + 1]
        elif i == height_map.shape[1] - 1:
            col_conditions[:, i] = height_map[:, i] < height_map[:, i - 1]
        else:
            c3 = height_map[:, i] < height_map[:, i + 1]
            c4 = height_map[:, i] < height_map[:, i - 1]
            col_conditions[:, i] = numpy.logical_and(c3, c4)
    low_point_map = numpy.logical_and(row_conditions, col_conditions)
    height_map_filtered = height_map[low_point_map]
    return numpy.sum(height_map_filtered + 1), low_point_map

def part_2(height_map, low_point_map):
    seen_locations, basin_sizes = set(), []
    low_point_row_idxs, low_point_col_idxs = numpy.where(low_point_map == True)
    for low_point_row_idx, low_point_col_idx in zip(low_point_row_idxs, low_point_col_idxs):
        basin_size = 0
        stack = [(low_point_row_idx, low_point_col_idx)]
        seen_locations.add((low_point_row_idx, low_point_col_idx))
        while stack:
            r, c = stack.pop()
            basin_size += 1
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (0 <= nr < height_map.shape[0] and 0 <= nc < height_map.shape[1] and height_map[nr][nc] != 9 and (nr, nc) not in seen_locations):
                    stack.append((nr, nc))
                    seen_locations.add((nr, nc))
        basin_sizes.append(basin_size)
    return(numpy.prod(sorted(basin_sizes, reverse = True)[:3]))

# Primary function definition
def main(args):
    # Parsing the input text file
    height_map = parse_input(args.input_file_path)
    # Obtaining the solution to Part 1
    part_1_solution, low_point_map = part_1(height_map)
    # Obtaining the solution to Part 2
    part_2_solution = part_2(height_map, low_point_map)
    # Displaying the solution
    print(f"Part 1 Solution : {part_1_solution}")
    print(f"Part 2 Solution : {part_2_solution}")

# If the script is invoked as entrypoint
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str)
    args = parser.parse_args()
    main(args)