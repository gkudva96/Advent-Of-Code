# Importing Libraries
from collections import defaultdict

# Given Input
start_num = [2, 1, 10, 11, 0, 6]

# Dictionary to keep track of the turn numbers for each spoken number
num_turn_dict = defaultdict(list)

# List to keep track of the spoken numbers
spoken_numbers = []

# For each turn until the 2020th turn
for turn in range(1, 2021):

    # Starting off with the starting numbers
    if turn <= len(start_num):

        # Adding the turn of the spoken number to the dictionary
        num_turn_dict[str(start_num[turn - 1])].append(turn)

        # Adding the spoken number to the list
        spoken_numbers.append(start_num[turn - 1])

    # Once the starting numbers have been spoken
    else:

        # Obtaining the last spoken number
        last_spoken_number = spoken_numbers[-1]

        # If the last spoken number was only spoken once
        if len(num_turn_dict[str(last_spoken_number)]) == 1:

            # Newly spoken number
            newly_spoken_number = 0
        
        # If the last spoken number was spoken more than once
        elif len(num_turn_dict[str(last_spoken_number)]) > 1:

            # Obtaining the two most recent turns of the last spoken number
            turns_list = num_turn_dict[str(last_spoken_number)]
            turn1, turn2 = turns_list[-2], turns_list[-1]

            # Newly spoken number
            newly_spoken_number = turn2 - turn1
        
        # Adding the newly spoken number to the list
        spoken_numbers.append(newly_spoken_number)

        # Adding the turn number of the newly spoken number to the dictionary
        num_turn_dict[str(newly_spoken_number)].append(turn)

# Printing the number spoken on the 2020th turn
print(f"2020th Number : {spoken_numbers[-1]}")