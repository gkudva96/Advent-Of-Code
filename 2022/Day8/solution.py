# Importing Libraries
from argparse import ArgumentParser
import numpy as np

# Function definition for parsing input file
def parse_input_file(args):
    with open(args.input_file_path, 'r') as f:
        grid = np.array([list(map(int, list(x.strip()))) for x in f.readlines()])
    return grid

# Function definition for part 1
def part_1(grid):
    visible_tree_count = 0
    for row in range(1, grid.shape[0] - 1):
        for col in range(1, grid.shape[1] - 1):
            top_visible = all(grid[0 : row, col] < grid[row, col])
            bot_visible = all(grid[row + 1 : , col] < grid[row, col])
            left_visible = all(grid[row, 0 : col] < grid[row, col])
            right_visible = all(grid[row, col + 1 : ] < grid[row, col])
            if any([top_visible, bot_visible, left_visible, right_visible]):
                visible_tree_count += 1
    return visible_tree_count + (grid.shape[0] * 2 + (grid.shape[1] - 2) * 2)
    
# Function definition for part 2
def part_2(grid):
    highest_scenic_score = 0
    for row in range(1, grid.shape[0] - 1):
        for col in range(1, grid.shape[1] - 1):
            top_scenic_score = [i for i, x in enumerate(grid[0 : row, col] >= grid[row, col]) if x == True]
            top_scenic_score = row if len(top_scenic_score) == 0 else row - top_scenic_score[-1]
            bot_scenic_score = [i for i, x in enumerate(grid[row + 1 : , col] >= grid[row, col]) if x == True]
            bot_scenic_score = grid.shape[0] - row - 1 if len(bot_scenic_score) == 0 else bot_scenic_score[0] + 1
            left_scenic_score = [i for i, x in enumerate(grid[row, 0 : col] >= grid[row, col]) if x == True]
            left_scenic_score = col if len(left_scenic_score) == 0 else col - left_scenic_score[-1]
            right_scenic_score = [i for i, x in enumerate(grid[row, col + 1 : ] >= grid[row, col]) if x == True]
            right_scenic_score = grid.shape[1] - col - 1 if len(right_scenic_score) == 0 else right_scenic_score[0] + 1
            temp_scenic_score = top_scenic_score * bot_scenic_score * left_scenic_score * right_scenic_score
            if (temp_scenic_score > highest_scenic_score):
                highest_scenic_score = temp_scenic_score
    return highest_scenic_score

# Primary function definition
def main(args):
    grid = parse_input_file(args)
    print(grid)
    part_1_solution = part_1(grid)
    print(f"Solution to part 1 : {part_1_solution}")
    part_2_solution = part_2(grid)
    print(f"Solution to part 2 : {part_2_solution}")

# If the script is invoked as entry-point
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str, default = 'input.txt')
    args = parser.parse_args()
    main(args)