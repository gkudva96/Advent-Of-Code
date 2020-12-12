# Importing Libraries
from collections import Counter

# List for storing the joltages
adapter_joltages = []

# Reading from input file
with open('input.txt', 'r') as f:
    # For each line
    for line in f:
        adapter_joltages.append(int(line.strip()))

# Sorting the adapter joltages
adapter_joltages.sort()
adapter_joltages.append(adapter_joltages[-1] + 3)

# Forming the adapter linkage
init_joltage = 0
joltage_differences = []
for joltage in adapter_joltages:
    joltage_differences.append(joltage - init_joltage)
    init_joltage = joltage

# Forming a counter object
c = Counter(joltage_differences)
print("Joltage Differences:", c[1] * c[3])