# Importing Libraries
from argparse import ArgumentParser

# Dictionaries to map the encryption
opponent_code = {'A' : 'Rock', 'B' : 'Paper', 'C' : 'Scissors'}
score_per_choice = {'Rock' : 1, 'Paper' : 2, 'Scissors' : 3}
score_per_outcome = {'Loss' : 0, 'Draw' : 3, 'Win' : 6}

# Function definition for part 1
def part_1(args):
    personal_code = {'X' : 'Rock', 'Y' : 'Paper', 'Z' : 'Scissors'}
    outcomes = {('Rock', 'Rock') : 'Draw', ('Paper', 'Rock') : 'Loss', ('Scissors', 'Rock') : 'Win',
            ('Rock', 'Paper') : 'Win', ('Paper', 'Paper') : 'Draw', ('Scissors', 'Paper') : 'Loss',
            ('Rock', 'Scissors') : 'Loss', ('Paper', 'Scissors') : 'Win', ('Scissors', 'Scissors') : 'Draw'}
    total_score = 0
    with open(args.input_file_path, 'r') as f:
        for line in f.readlines():
            moves = line.strip().split()
            total_score += (score_per_choice[personal_code[moves[1]]]) + (score_per_outcome[outcomes[(opponent_code[moves[0]], personal_code[moves[1]])]])
    return total_score

# Function definition for part 2
def part_2(args):
    personal_code = {'X' : 'Loss', 'Y' : 'Draw', 'Z' : 'Win'}
    outcomes = {'Rock' : {'Loss' : 'Scissors', 'Draw' : 'Rock', 'Win' : 'Paper'},
            'Paper' : {'Loss' : 'Rock', 'Draw' : 'Paper', 'Win' : 'Scissors'},
            'Scissors' : {'Loss' : 'Paper', 'Draw' : 'Scissors', 'Win' : 'Rock'}}
    total_score = 0
    with open(args.input_file_path, 'r') as f:
        for line in f.readlines():
            moves = line.strip().split()
            total_score += score_per_choice[outcomes[opponent_code[moves[0]]][personal_code[moves[1]]]] + score_per_outcome[personal_code[moves[1]]]
    return total_score
        
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