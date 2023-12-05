# Importing Libraries
from argparse import ArgumentParser
import math

# Function definition for part 1
def part_1(args):
    accumulator = 0
    max_limits = {"red" : 12, "green" : 13, "blue" : 14}
    with open(args.input_file_path, 'r') as f:
        for line in f.readlines():
            game_id = line.strip().split(':')[0].split()[-1]
            game_sets = [a.strip() for z in [y.split(',') for y in [x.strip() for x in line.strip().split(':')[-1].split(';')]] for a in z]
            conditions = [int(b.split()[0]) <= max_limits[b.split()[-1]] for b in game_sets]
            if all(conditions):
                accumulator += int(game_id)
    return accumulator

# Function definition for part 2
def part_2(args):
    accumulator = 0
    with open(args.input_file_path, 'r') as f:
        for line in f.readlines():
            minimum_cubes = {"red" : 0, "green" : 0, "blue" : 0}
            game_sets = [a.strip() for z in [y.split(',') for y in [x.strip() for x in line.strip().split(':')[-1].split(';')]] for a in z]
            for x in game_sets:
                cube_count, cube_colour = x.split()
                if int(cube_count) > minimum_cubes[cube_colour]:
                    minimum_cubes[cube_colour] = int(cube_count)
            power = math.prod([x for x in minimum_cubes.values()])
            accumulator += power
    return accumulator
        
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