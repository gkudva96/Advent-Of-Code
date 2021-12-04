# Importing Libraries
from argparse import ArgumentParser
import numpy

# Helper function definitions
def parse_input(input_file_path):
    with open(input_file_path, 'r') as f:
        return numpy.array([[int(bit) for bit in line.strip()] for line in f.readlines()])

def part_1(diagnostics):
    one_count = numpy.sum(diagnostics, axis = 0)
    zero_count = diagnostics.shape[0] - one_count
    gamma_rate_bin = numpy.where((one_count > zero_count) == True, 1, 0)
    gamma_rate_dec = int(''.join([str(x) for x in gamma_rate_bin]), 2)
    epsilon_rate_bin = 1 - gamma_rate_bin
    epsilon_rate_dec = int(''.join([str(x) for x in epsilon_rate_bin]), 2)
    return gamma_rate_dec * epsilon_rate_dec
    
def part_2(diagnostics):
    oxygen_rating, bit_pos = numpy.copy(diagnostics), 0
    while(oxygen_rating.shape[0] != 1):
        one_count = numpy.sum(oxygen_rating, axis = 0)
        zero_count = oxygen_rating.shape[0] - one_count
        most_common_bit = numpy.where((one_count >= zero_count) == True, 1, 0)[bit_pos]
        row_idxs_del = tuple(row_idx for row_idx in range(0, oxygen_rating.shape[0]) if oxygen_rating[row_idx][bit_pos] != most_common_bit)
        oxygen_rating = numpy.delete(oxygen_rating, row_idxs_del, axis = 0)
        bit_pos += 1
    bit_pos, carbon_rating = 0, numpy.copy(diagnostics)
    while(carbon_rating.shape[0] != 1):
        one_count = numpy.sum(carbon_rating, axis = 0)
        zero_count = carbon_rating.shape[0] - one_count
        least_common_bit = numpy.where((zero_count <= one_count) == True, 0, 1)[bit_pos]
        row_idxs_del = tuple(row_idx for row_idx in range(0, carbon_rating.shape[0]) if carbon_rating[row_idx][bit_pos] != least_common_bit)
        carbon_rating = numpy.delete(carbon_rating, row_idxs_del, axis = 0)
        bit_pos += 1
    oxygen_rating_dec = int(''.join([str(x) for x in oxygen_rating.squeeze()]), 2)
    carbon_rating_dec = int(''.join([str(x) for x in carbon_rating.squeeze()]), 2)
    return oxygen_rating_dec * carbon_rating_dec

# Primary function definition
def main(args):
    # Parsing the input text file
    diagnostics = parse_input(args.input_file_path)
    # Solving Part 1
    part_1_solution = part_1(diagnostics)
    # Solving Part 2
    part_2_solution = part_2(diagnostics)
    # Displaying the solutions
    print(f"Part 1 Solution : {part_1_solution}")
    print(f"Part 2 Solution : {part_2_solution}")

# If the script is invoked as entrypoint
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_file_path', type = str)
    args = parser.parse_args()
    main(args)