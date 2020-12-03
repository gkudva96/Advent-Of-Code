# Initializing lists for policies and passwords
policies, passwords = [], []

# To keep track of the total number of passwords and valid passwords
tot_passwords, val_passwords = 0, 0

# Reading the input file
with open('input.txt', 'r') as f:
    for line in f:
        policy, password = line.strip().split(':')
        policies.append(policy)
        passwords.append(password.strip())
        tot_passwords += 1

# For each input policy and password
for i in range(tot_passwords):
    # Separating the policy into target positions and target character
    pos_s, policy_char = policies[i].split()
    # Obtaining the two required positions of the target character
    pos1, pos2 = map(int, pos_s.split('-'))
    # Determining the validity of the password based on the XOR rule
    if pos1 - 1 < len(passwords[i]):
        condition1 = passwords[i][pos1 - 1] == policy_char
    else:
        condition1 = False
    if pos2 - 1 < len(passwords[i]):
        condition2 = passwords[i][pos2 - 1] == policy_char
    else:
        condition2 = False
    if condition1 ^ condition2:
        val_passwords += 1

# Displaying the total number of valid passwords
print("Number of Valid Passwords:", val_passwords)    