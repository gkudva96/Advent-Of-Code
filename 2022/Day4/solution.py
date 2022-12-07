# Importing Libraries
from argparse import ArgumentParser

# Function definition for part 1
def part_1(args):
    fully_contained_assignments = 0
    with open(args.input_file_path, 'r') as f:
        for line in f.readlines():
            ranges = line.strip().split(',')
            range1 = list(map(int, ranges[0].split('-')))
            range2 = list(map(int, ranges[1].split('-')))
            range1 = set([x for x in range(range1[0], range1[1] + 1)])
            range2 = set([x for x in range(range2[0], range2[1] + 1)])
            if range1.issubset(range2) or range2.issubset(range1):
                fully_contained_assignments += 1
    return fully_contained_assignments


# Function definition for part 2
def part_2(args):
    overlapping_assignments = 0
    with open(args.input_file_path, 'r') as f:
        for line in f.readlines():
            ranges = line.strip().split(',')
            range1 = list(map(int, ranges[0].split('-')))
            range2 = list(map(int, ranges[1].split('-')))
            range1 = set([x for x in range(range1[0], range1[1] + 1)])
            range2 = set([x for x in range(range2[0], range2[1] + 1)])
            if len(range1.intersection(range2)) != 0:
                overlapping_assignments += 1
    return overlapping_assignments

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