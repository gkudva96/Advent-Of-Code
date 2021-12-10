# Importing Libraries
from collections import defaultdict
from argparse import ArgumentParser

# Helper function definitions
def parse_input(input_file_path):
    digital_displays, digital_outputs = [], []
    with open(input_file_path, 'r') as f:
        for line in f.readlines():
            line_comp = line.split('|')
            digital_displays.append([set(x) for x in line_comp[0].strip().split()])
            digital_outputs.append([set(x) for x in line_comp[1].strip().split()])
    return digital_displays, digital_outputs

def find_signal_digit(digital_display, signal_mapper, digits):
    for digit in digits:
        if digit == 6:
            signal_8 = signal_mapper[8]
            signal_1 = signal_mapper[1]
            _ = [signal_mapper[6].update(signal_8 - set(x)) for x in signal_1 if signal_8 - set(x) in digital_display]
        if digit == 5:
            signal_6 = signal_mapper[6]
            _ = [signal_mapper[5].update(signal_6 - set(x)) for x in signal_6 if signal_6 - set(x) in digital_display]
        if digit == 3:
            signal_1 = signal_mapper[1]
            _ = [signal_mapper[3].update(x) for x in digital_display if signal_1.issubset(x) and len(x) == 5]
        if digit == 2:
            _ = [signal_mapper[2].update(x) for x in digital_display if len(x) == 5 and x not in signal_mapper.values()]
        if digit == 9:
            signal_4 = signal_mapper[4]
            _ = [signal_mapper[9].update(x) for x in digital_display if len(x) == 6 and signal_4.issubset(x)]
        if digit == 0:
            _ = [signal_mapper[0].update(x) for x in digital_display if x not in signal_mapper.values()]

def part_1(digital_outputs):
    total = sum([1 for digital_output in digital_outputs for digit in digital_output if len(digit) in {2, 3, 4, 7}])
    return total

def part_2(digital_displays, digital_outputs):
    digit_len_mapper_inv = {2 : 1, 3 : 7, 4 : 4, 7 : 8}
    total = 0
    for digital_display, digital_output in zip(digital_displays, digital_outputs):
        signal_mapper = defaultdict(set)
        _ = [signal_mapper[digit_len_mapper_inv[len(digit)]].update(set(digit)) for digit in (digital_display + digital_output) if len(digit) in {2, 3, 4, 7}]
        find_signal_digit(digital_display, signal_mapper, [6, 5, 3, 2, 9, 0])
        total += int(''.join([str(k) for x in digital_output for k, v in signal_mapper.items() if v == x]))
    return total

# Primary function definition
def main(args):
    # Parsing the input text file
    digital_displays, digital_outputs = parse_input(args.input_file_path)
    # Obtaining the solution to Part 1
    part_1_solution = part_1(digital_outputs)
    # Obtaining the solution to Part 2
    part_2_solution = part_2(digital_displays, digital_outputs)
    # Displaying the solution
    print(f"Part 1 Solution : {part_1_solution}")
    print(f"Part 2 Solution : {part_2_solution}")

# If the script is invoked as entrypoint
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str)
    args = parser.parse_args()
    main(args)