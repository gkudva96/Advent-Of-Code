# Importing Libraries
from argparse import ArgumentParser

# Function definition for part 1
def part_1_2(args, distinct_characters):
    with open(args.input_file_path, 'r') as f:
        datastream_buffer = f.readline()
    end_character = [x + distinct_characters for x in range(0, len(datastream_buffer.strip()) - distinct_characters) if len(set(datastream_buffer[x : x + distinct_characters])) == distinct_characters]
    return end_character[0]

# Primary function definition
def main(args):
    part_1_solution = part_1_2(args, 4)
    print(f"Solution to part 1 : {part_1_solution}")
    part_2_solution = part_1_2(args, 14)
    print(f"Solution to part 2 : {part_2_solution}")

# If the script is invoked as entry-point
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str, default = 'input.txt')
    args = parser.parse_args()
    main(args)