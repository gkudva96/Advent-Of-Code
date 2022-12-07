# Importing Libraries
from argparse import ArgumentParser

# Function definition for part 1
def part_1(args):
    max_total_calorie_count = 0
    with open(args.input_file_path, 'r') as f:
        temp_calorie_sum = 0
        for line in f.readlines():
            if line.strip() != '':
                temp_calorie_sum += int(line.strip())
            else:
                max_total_calorie_count = max(max_total_calorie_count, temp_calorie_sum)
                temp_calorie_sum = 0
    return max_total_calorie_count

# Function definition for part 2
def part_2(args):
    total_calorie_count = []
    with open(args.input_file_path, 'r') as f:
        temp_calorie_sum = 0
        for line in f.readlines():
            if line.strip() != '':
                temp_calorie_sum += int(line.strip())
            else:
                total_calorie_count.append(temp_calorie_sum)
                temp_calorie_sum = 0
    return sum(sorted(total_calorie_count, reverse = True)[0 : 3])
        
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