# Importing libraries
import re

# Function Definitions
def check_birth_issue_exp_year(year : str, option : int) -> bool:
    # Determining the number of digits
    if len(year) == 4 and year.isdigit():
        # Converting from string to integer
        year = int(year)
        # Checking the range validity for birth year
        if option == 1:
            return True if year >= 1920 and year <= 2002 else False
        # Checking the range validity for issue year
        if option == 2:
            return True if year >= 2010 and year <= 2020 else False
        # Checking the range validity for expiration year
        if option == 3:
            return True if year >= 2020 and year <= 2030 else False
    else:
        return False

def check_height(height : str) -> bool:
    # If the suffix 'cm' is present in the string
    if height.endswith('cm'):
        try:
            height_cm = int(height[0 : -2])
            return True if height_cm >= 150 and height_cm <= 193 else False
        except:
            return False
    # If the suffix 'in' is present in the string
    elif height.endswith('in'):
        try:
            height_in = int(height[0 : -2])
            return True if height_in >= 59 and height_in <= 76 else False
        except:
            return False
    return False

def check_hair_colour(hair_colour : str) -> bool:
    # If the total length of the string is 7
    if len(hair_colour) == 7:
        return True if re.search('^#[0-9]+|[a-f]+', hair_colour) else False
    else:
        return False

def check_eye_colour(eye_colour : str) -> bool:
    # Return true if the eye colour has a value from the list
    valid_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return True if eye_colour in valid_colours else False

def check_passport_id(passport_id : str) -> bool:
    # If the length of the string is 9
    if len(passport_id) == 9 and passport_id.isdigit():
        return True
    else:
        return False

# Accumulator variable for total number of valid passports
inval_passports = 0

# Initializing a list for collecting passports
passport_list = []

# Initializing a temporary dictionary for one passport
temp_passport = {}

# Reading from the input file
with open('input.txt', 'r') as f:
    # For each line in the file
    for line in f:
        # If the line is not a blank line
        if line != '\n':
            # For each key-value pair on the line
            for x in line.strip().split():
                key, value = x.split(':')
                temp_passport[key] = value
        # If the line is a blank line (marks the end of one passport)
        else:
            # Adding to the list of passports
            passport_list.append(temp_passport)
            # Reinitializing the temporary passport dictionary
            temp_passport = {}

# For each passport in the list
for passport in passport_list:

    # Checking if all the required fields are present
    key_count_valid_flag = False
    num_keys = len(passport.keys())
    if num_keys == 8:
        key_count_valid_flag = True
    elif num_keys < 8:
        if num_keys == 7 and 'cid' not in passport.keys():
            key_count_valid_flag = True
    
    # Checking if all the present fields have valid values
    if key_count_valid_flag:
        # Validity list
        validity_list = []
        # For each given field of the passport
        for key, value in passport.items():
            # If the key is birth year
            if key == 'byr':
                validity_list.append(check_birth_issue_exp_year(value, 1))
            # If the key is issue year
            if key == 'iyr':
                validity_list.append(check_birth_issue_exp_year(value, 2))
            # If the key is expiration year
            if key == 'eyr':
                validity_list.append(check_birth_issue_exp_year(value, 3))
            # If the key is height
            if key == 'hgt':
                validity_list.append(check_height(value))
            # If the key is hair colour
            if key == 'hcl':
                validity_list.append(check_hair_colour(value))
            # If the key is eye colour
            if key == 'ecl':
                validity_list.append(check_eye_colour(value))
            # If the key is passport id
            if key == 'pid':
                validity_list.append(check_passport_id(value))
            # If the key is country id
            if key == 'cid':
                continue
        # If any given field is invalid
        if not all(validity_list):
            inval_passports += 1
    else:
        inval_passports += 1

# Printing the total number of valid passports
print("Total Number of Valid Passports:", len(passport_list) - inval_passports)