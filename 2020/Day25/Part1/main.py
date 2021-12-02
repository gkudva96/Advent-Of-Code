# Initializing the constant divisor
CONST = 20201227

# Function definition to determine the loop size
def determine_loop_size(final_value, subject_number = 7):
    # Initializing the initial value and initial loop count
    value, loop_count = 1, 1
    # Until the new value matches the final value
    while True:
        value *= subject_number
        value %= CONST
        if value == final_value:
            break
        loop_count += 1
    # Returning the loop size
    return loop_count

# Function definition to determine the final value
def determine_final_value(loop_size, subject_number = 7):
    # Initializing the initial_value and initial loop count
    value, loop_count = 1, 1
    # Until the loop size is reached
    while loop_count <= loop_size:
        value *= subject_number
        value %= CONST
        loop_count += 1
    # Returning the final value
    return value

# Given input
public_key_dict = {'card' : 8421034, 'door' : 15993936}

# Determining the loop size of the card
card_loop_size = determine_loop_size(public_key_dict['card'])

# Determining the loop size of the door
door_loop_size = determine_loop_size(public_key_dict['door'])

# Determining the encryption key
encryption_key = determine_final_value(card_loop_size, public_key_dict['door'])
print(f"Encryption Key : {encryption_key}")