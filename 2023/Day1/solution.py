# Importing Libraries
from argparse import ArgumentParser
import re

# Function definition for part 1
def part_1(args):
    with open(args.input_file_path, 'r') as f:
        lines = f.readlines()
    return sum(list(map(int, [x[0] + x[-1] for x in [re.sub('\D', '', line) for line in lines]])))

# Function definition for part 2
def part_2(args):
    accumulator = 0
    string_to_digit_mapping = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", \
                            "seven" : "7", "eight" : "8", "nine" : "9"}
    with open(args.input_file_path, 'r') as f:
        for line in f.readlines():
            true_digit_occurrences = [match.start() for match in re.finditer(r'\d', line)]
            temp_digit_string = re.sub('\D', '', line)
            first_digit = (temp_digit_string[0], true_digit_occurrences[0])
            last_digit = (temp_digit_string[-1], true_digit_occurrences[-1])
            for string_digit in string_to_digit_mapping.keys():
                string_digit_occurrences = [match.start() for match in re.finditer(string_digit, line)]
                if len(string_digit_occurrences) != 0:
                    if string_digit_occurrences[0] < first_digit[1]:
                        first_digit = (string_to_digit_mapping[string_digit], string_digit_occurrences[0])
                    if string_digit_occurrences[-1] > last_digit[1]:
                        last_digit = (string_to_digit_mapping[string_digit], string_digit_occurrences[-1])
            accumulator += int(first_digit[0] + last_digit[0])
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