# Importing Libraries
import copy

# List for storing instructions and respective arguments
instructions, arguments = [], []

# Reading from the input file
with open('input.txt', 'r') as f:
    # For each instruction
    for line in f:
        instruction, argument = line.strip().split()
        instructions.append(instruction)
        arguments.append(int(argument))

# List for keeping track of how many times an instruction has been visited
times_visited = [0] * len(instructions)

# List to keep track of the instruction indices that might cause the infinite loop
inf_loop_instr_idxs = []

# Running the infinite loop once to check the indices of jmp and nop instructions upto the looping point
index = 0
while True:
    instruction, argument = instructions[index], arguments[index]
    times_visited[index] += 1
    if times_visited.count(2) == 1:
        break
    if instruction == 'acc':
        index += 1
    elif instruction == 'jmp':
        inf_loop_instr_idxs.append(index)
        index += argument
    elif instruction == 'nop':
        inf_loop_instr_idxs.append(index)
        index += 1

# Testing each jmp and nop instruction to see if they cause the infinite loop
for instr_idx in inf_loop_instr_idxs:
    times_visited = [0] * len(instructions)
    temp_instructions = copy.deepcopy(instructions)
    temp_instructions[instr_idx] = 'jmp' if temp_instructions[instr_idx] == 'nop' else 'nop'
    index = 0
    inf_loop_flag = False
    while True:
        instruction, argument = temp_instructions[index], arguments[index]
        times_visited[index] += 1
        if times_visited.count(2) == 1:
            inf_loop_flag = True
            break
        if instruction == 'acc':
            index += 1
        elif instruction == 'jmp':
            index += argument
        elif instruction == 'nop':
            index += 1
        if index >= len(instructions):
            break
    if not inf_loop_flag:
        instructions[instr_idx] = temp_instructions[instr_idx]

# Progressing through the modified instructions
index, accumulator = 0, 0
while index < len(instructions):
    instruction, argument = instructions[index], arguments[index]
    if instruction == 'acc':
        accumulator += argument
        index += 1
    elif instruction == 'jmp':
        index += argument
    elif instruction == 'nop':
        index += 1

# Printing the value of the accumulator variable
print("Accumulator Variable:", accumulator)