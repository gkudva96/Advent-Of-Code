# Importing Libraries
from argparse import ArgumentParser
import numpy

# Dictionary to map the character to score
character_to_score_syntax = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
character_to_score_complete = {')' : 1, ']' : 2, '}' : 3, '>' : 4}

# Dictionary to map the opening and closing pairs
closing_to_opening = {')' : '(', ']' : '[', '}' : '{', '>' : '<'}
opening_to_closing = {v : k for k, v in closing_to_opening.items()}

# Helper function definitions
def parse_input(input_file_path):
    with open(input_file_path, 'r') as f:
        navigation_subsystem = [line.strip() for line in f.readlines()]
    return navigation_subsystem

def part_1_2(navigation_subsystem):
    autocomplete_scores, total_syntax_score = [], 0
    for line in navigation_subsystem:
        line_syntax_score, stack = 0, []
        for character in line:
            if character in [')', ']', '}', '>']:
                if closing_to_opening[character] == stack[-1]:
                    stack.pop()
                else:
                    line_syntax_score += character_to_score_syntax[character]
                    break
            else:
                stack.append(character)
        if line_syntax_score == 0:
            closing_sequence = [opening_to_closing[character] for character in stack[::-1]]
            autocomplete_score = 0
            for character in closing_sequence:
                autocomplete_score = autocomplete_score * 5 + character_to_score_complete[character]
            autocomplete_scores.append(autocomplete_score)
        else:
            total_syntax_score += line_syntax_score
    return total_syntax_score, int(numpy.median(autocomplete_scores))

# Primary function definition
def main(args):
    # Parsing the input text file
    navigation_subsystem = parse_input(args.input_file_path)
    # Obtaining the solution to Part 1 and 2
    part_1_solution, part_2_solution = part_1_2(navigation_subsystem)
    # Displaying the solution
    print(f"Part 1 Solution : {part_1_solution}")
    print(f"Part 2 Solution : {part_2_solution}")

# If the script is invoked as entrypoint
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str)
    args = parser.parse_args()
    main(args)