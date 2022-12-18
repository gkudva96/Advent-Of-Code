# Importing Libraries
from argparse import ArgumentParser
import numpy as np
import copy

# Function definition to parse input file
def parse_input_file(args):
    monkeys = []
    with open(args.input_file_path, 'r') as f:
        for line in f.readlines():
            if line.strip().startswith('Monkey'):
                monkeys.append({})
                monkeys[-1]['inspection_count'] = 0
            if line.strip().startswith('Starting'):
                monkeys[-1]['items'] = list(map(int, line.strip().split(':')[-1].strip().split(', ')))
            if line.strip().startswith('Operation'):
                monkeys[-1]['operation'] = line.strip().split(':')[-1].strip().split()[-2 : ]
            if line.strip().startswith('Test'):
                monkeys[-1]['test'] = int(line.strip().split(':')[-1].strip().split()[-1])
            if line.strip().startswith('If true'):
                monkeys[-1][True] = int(line.strip().split(':')[-1].strip().split()[-1])
            if line.strip().startswith('If false'):
                monkeys[-1][False] = int(line.strip().split(':')[-1].strip().split()[-1])
    return monkeys

# Function definition to return new worry level
def get_new_worry_level(old_worry_level, operation, reduce_worry_level, mod_num):
    factor = old_worry_level if operation[-1].isalpha() else int(operation[-1])
    if operation[0] == '*':
        if reduce_worry_level:
            return old_worry_level * factor
        else:
            return ((old_worry_level % mod_num) * (factor % mod_num)) % mod_num
    if operation[0] == '+':
        if reduce_worry_level:
            return old_worry_level + factor
        else:
            return ((old_worry_level % mod_num) + (factor % mod_num)) % mod_num

# Function definition for part 1
def part_1_2(monkeys, rounds, reduce_worry_level):
    if reduce_worry_level:
        mod_num = None
    else:
        mod_num = int(np.prod([monkey['test'] for monkey in monkeys]))
    for _ in range(rounds):
        for idx in range(len(monkeys)):
            for _ in range(len(monkeys[idx]['items'])):
                worry_level = monkeys[idx]['items'][0]
                monkeys[idx]['inspection_count'] += 1
                del monkeys[idx]['items'][0]
                worry_level = get_new_worry_level(worry_level, monkeys[idx]['operation'], reduce_worry_level, mod_num)
                if reduce_worry_level:
                    worry_level = worry_level // 3
                monkeys[monkeys[idx][worry_level % monkeys[idx]['test'] == 0]]['items'].append(worry_level)
    monkey_inspection_counts = sorted([x['inspection_count'] for x in monkeys], reverse = True)
    return monkey_inspection_counts[0] * monkey_inspection_counts[1]

# Primary function definition
def main(args):
    monkeys = parse_input_file(args)
    part_1_solution = part_1_2(copy.deepcopy(monkeys), 20, True)
    print(f"Solution to part 1 : {part_1_solution}")
    part_2_solution = part_1_2(copy.deepcopy(monkeys), 10000, False)
    print(f"Solution to part 2 : \n{part_2_solution}")

# If the script is invoked as entry-point
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str, default = 'input.txt')
    args = parser.parse_args()
    main(args)