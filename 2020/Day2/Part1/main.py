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
    # Separating the policy into min-max and target character
    min_max_s, policy_char = policies[i].split()
    # Obtaining the minimum and maximum count of the target character
    min_count, max_count = map(int, min_max_s.split('-'))
    # Determining the validity of the password
    policy_char_count = passwords[i].count(policy_char)
    if policy_char_count >= min_count and policy_char_count <= max_count:
        val_passwords += 1

# Displaying the total number of valid passwords
print("Number of Valid Passwords:", val_passwords)    