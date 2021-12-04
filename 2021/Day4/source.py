# Importing Libraries
from argparse import ArgumentParser
import numpy

# Helper function definitions
def parse_input(input_file_path):
    boards = []
    with open(input_file_path, 'r') as f:
        for idx, line in enumerate(f.readlines()):
            if idx == 0:
                random_draws = [int(x) for x in line.strip().split(',')]
            else:
                if line.strip().split() != []:
                    boards.append([int(x) for x in line.strip().split()])
    return (random_draws, numpy.array(boards))

def part_1(random_draws, boards):
    marked, bingo_board_idx, bingo_random_draw = numpy.zeros_like(boards), None, None
    for random_draw in random_draws:
        marked[boards == random_draw] = 1
        for board_idx in range(marked.shape[0]):
            temp_board = marked[board_idx, :, :].squeeze()
            row_sums = numpy.sum(temp_board, axis = 1)
            col_sums = numpy.sum(temp_board, axis = 0)
            if (boards.shape[1] in row_sums) or (boards.shape[1] in col_sums):
                bingo_board_idx = board_idx
                break
        if bingo_board_idx is not None:
            bingo_random_draw = random_draw
            break
    bingo_board = boards[bingo_board_idx, :, :].squeeze()
    unmarked_sum = numpy.sum(bingo_board[marked[bingo_board_idx, :, :] != 1])
    return unmarked_sum * bingo_random_draw
    
def part_2(random_draws, boards):
    marked, bingo_board_idxs, bingo_random_draw = numpy.zeros_like(boards), [], None
    for random_draw in random_draws:
        marked[boards == random_draw] = 1
        for board_idx in range(marked.shape[0]):
            temp_board = marked[board_idx, :, :].squeeze()
            row_sums = numpy.sum(temp_board, axis = 1)
            col_sums = numpy.sum(temp_board, axis = 0)
            if (boards.shape[1] in row_sums) or (boards.shape[1] in col_sums):
                if board_idx not in bingo_board_idxs:
                    bingo_board_idxs.append(board_idx)
                    if len(bingo_board_idxs) == marked.shape[0]:
                        break
                else:
                    continue
        if len(bingo_board_idxs) == marked.shape[0]:
            bingo_random_draw = random_draw
            break
    last_bingo_board = boards[bingo_board_idxs[-1], :, :].squeeze()
    unmarked_sum = numpy.sum(last_bingo_board[marked[bingo_board_idxs[-1], :, :] != 1])
    return unmarked_sum * bingo_random_draw

# Primary function definition
def main(args):
    # Parsing the input text file
    random_draws, boards = parse_input(args.input_file_path)
    boards = numpy.reshape(boards, (-1, boards.shape[1], boards.shape[1]))
    # Solving Part 1
    part_1_solution = part_1(random_draws, boards)
    # Solving Part 2
    part_2_solution = part_2(random_draws, boards)
    # Displaying the solutions
    print(f"Part 1 Solution : {part_1_solution}")
    print(f"Part 2 Solution : {part_2_solution}")

# If the script is invoked as entrypoint
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str)
    args = parser.parse_args()
    main(args)