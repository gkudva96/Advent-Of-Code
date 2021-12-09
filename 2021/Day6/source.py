# Importing Libraries
from collections import defaultdict, Counter
from argparse import ArgumentParser
import numpy

# Helper function definitions
def parse_input(input_file_path):
    with open(input_file_path, 'r') as f:
        lanternfish_ages = numpy.array(list(map(int, f.readline().split(','))))
    return lanternfish_ages
    
def part_1_2(lanternfish_ages, num_days):
    # Finding the frequencies of the initial reproduction timers (to avoid redudant computations)
    init_repro_counts = Counter(lanternfish_ages.tolist())
    day_repro_counts = defaultdict(float)
    # Simulating the initial reproduction timers only
    for init_repro_count in init_repro_counts:
        day_repro_counts[init_repro_count + 1] += init_repro_counts[init_repro_count]
        temp_repro_counts = (num_days - (init_repro_count + 1)) // 7
        for x in range(1, temp_repro_counts + 1):
            day_repro_counts[init_repro_count + 1 + (7 * x)] += init_repro_counts[init_repro_count]
    # Simulating the newly added reproduction timers
    for day_num in range(1, num_days + 1):
        if day_num in day_repro_counts:
            day_repro_counts[day_num + 9] += day_repro_counts[day_num]
            temp_repro_counts = (num_days - (day_num + 9)) // 7
            for x in range(1, temp_repro_counts + 1):
                day_repro_counts[day_num + 9 + (7 * x)] += day_repro_counts[day_num]
    # Finding the sum of reproduction counts up to and until the required number of days
    return (lanternfish_ages.shape[0] + sum([v for k, v in day_repro_counts.items() if k <= day_num]))

# Primary function definition
def main(args):
    # Parsing the input text file
    lanternfish_ages = parse_input(args.input_file_path)
    # Obtaining the total number of lanternfish after the required number of days
    part_1_2_solution = part_1_2(lanternfish_ages, args.num_days)
    # Displaying the solution
    print(f"Total Lanternfish : {part_1_2_solution}")

# If the script is invoked as entrypoint
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str)
    parser.add_argument('--num_days', type = int, default = 80)
    args = parser.parse_args()
    main(args)