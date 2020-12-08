# Importing libraries
from bag import Bag

# Dictionary to keep track of bags encountered
bag_dict = {}

# Reading from input file
with open('input.txt', 'r') as f:

    # For each rule
    for rule in f:

        # Obtaining the name of the outer bag
        outer_bag_name = '_'.join(rule.strip().split('contain')[0].split()[0:-1])

        # Creating a Bag object of name outer bag
        outer_bag = Bag(outer_bag_name)

        # Adding to the dictionary of encountered bags
        bag_dict[outer_bag_name] = outer_bag

        # Obtaining the names of the inner bags
        inner_bags = rule.strip().split('contain')[1].split(',')
        for inner_bag in inner_bags:
            inner_bag_name = inner_bag.split()
            if inner_bag_name[0] != 'no':
                inner_bag_quantity = int(inner_bag_name[0])
                inner_bag_name = '_'.join(inner_bag_name[1:-1])
            else:
                inner_bag_quantity = 0
                inner_bag_name = "none"
            outer_bag.add_content(inner_bag_name, inner_bag_quantity)

# Counting the total number of bags that are contained within one shiny gold bag
print("Total Bags:", bag_dict['shiny_gold'].count_content(bag_dict))