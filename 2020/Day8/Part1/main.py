# List for storing instructions and respective arguments
instructions, arguments = [], []

# Accumulator variable
accumulator = 0

# Reading from the input file
with open('input.txt', 'r') as f:
    # For each instruction
    for line in f:
        instruction, argument = line.strip().split()
        instructions.append(instruction)
        arguments.append(int(argument))

# List for keeping track of how many times an instruction has been visited
times_visited = [0] * len(instructions)

# Running the infinite loop
index = 0
while True:
    instruction, argument = instructions[index], arguments[index]
    times_visited[index] += 1
    if times_visited.count(2) == 1:
        break
    if instruction == 'acc':
        accumulator += argument
        index += 1
    elif instruction == 'jmp':
        index += argument
    elif instruction == 'nop':
        index += 1

# Printing the value of the accumulator variable
print("Accumulator Variable:", accumulator)