# Importing Libraries
from argparse import ArgumentParser
import numpy
from collections import Counter

# Helper function definitions
def parse_input(input_file_path):
    with open(input_file_path, 'r') as f:
        vent_line_coords = [[int(y) for x in line.strip().split('->') for y in x.strip().split(',')] for line in f.readlines()]
        return numpy.array(vent_line_coords)

def find_overlap_count(vent_points):
    overlap_count = numpy.array([x for x in Counter(vent_points).values()])
    return len(overlap_count[overlap_count >= 2])
    
def part_1_2(vent_line_coords):
    part_1_vent_points, part_2_vent_points = [], []
    for row_idx in range(vent_line_coords.shape[0]):
        beg_coords = vent_line_coords[row_idx, :2]
        end_coords = vent_line_coords[row_idx, 2:]
        coords_offset = end_coords - beg_coords
        if (beg_coords[0] == end_coords[0]) or (beg_coords[1] == end_coords[1]):
            if (coords_offset[0] + coords_offset[1]) < 0:
                if coords_offset[0] == 0:
                    part_1_vent_points.extend([(beg_coords[0], x) for x in range(beg_coords[1], end_coords[1] - 1, -1)])
                elif coords_offset[1] == 0:
                    part_1_vent_points.extend([(x, beg_coords[1]) for x in range(beg_coords[0], end_coords[0] - 1, -1)])
            elif (coords_offset[0] + coords_offset[1]) > 0:
                if coords_offset[0] == 0:
                    part_1_vent_points.extend([(beg_coords[0], x) for x in range(beg_coords[1], end_coords[1] + 1)])
                elif coords_offset[1] == 0:
                    part_1_vent_points.extend([(x, beg_coords[1]) for x in range(beg_coords[0], end_coords[0] + 1)])
        else:
            if (coords_offset[0] < 0) and (coords_offset[1] < 0):
                part_2_vent_points.extend([(x, y) for x, y in zip(list(range(beg_coords[0], end_coords[0] - 1, -1)), list(range(beg_coords[1], end_coords[1] - 1, -1)))])
            elif (coords_offset[0] < 0) and (coords_offset[1] > 0):
                part_2_vent_points.extend([(x, y) for x, y in zip(list(range(beg_coords[0], end_coords[0] - 1, -1)), list(range(beg_coords[1], end_coords[1] + 1)))])
            elif (coords_offset[0] > 0) and (coords_offset[1] < 0):
                part_2_vent_points.extend([(x, y) for x, y in zip(list(range(beg_coords[0], end_coords[0] + 1)), list(range(beg_coords[1], end_coords[1] - 1, -1)))])
            elif (coords_offset[0] > 0) and (coords_offset[1] > 0):
                part_2_vent_points.extend([(x, y) for x, y in zip(list(range(beg_coords[0], end_coords[0] + 1)), list(range(beg_coords[1], end_coords[1] + 1)))])
    return (find_overlap_count(part_1_vent_points), find_overlap_count(part_1_vent_points + part_2_vent_points))

# Primary function definition
def main(args):
    # Parsing the input text file
    vent_line_coords = parse_input(args.input_file_path)
    # Solving Part 1 & 2
    part_1_solution, part_2_solution = part_1_2(vent_line_coords)
    # # Displaying the solutions
    print(f"Part 1 Solution : {part_1_solution}")
    print(f"Part 2 Solution : {part_2_solution}")

# If the script is invoked as entrypoint
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str)
    args = parser.parse_args()
    main(args)