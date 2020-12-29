# Importing Libraries
from collections import defaultdict, Counter

# Function definition to check one-to-one mapping of ingredient and allergen
def check_one_to_one_allergen_ingredient(allergen_ingredients_dict):
    for allergen in allergen_ingredients_dict:
        if len(allergen_ingredients_dict[allergen]) > 1:
            return False
    return True

# Dictionary to store the ingredients per allergen
allergen_ingredients_dict = defaultdict(list)

# List to store all the ingredients encountered
overall_ingredients = []

# Reading the input file
with open('input.txt', 'r') as f:
    # For each line
    for line in f:
        # Splitting the line into ingredients and allergens
        ingredients, allergens = line.strip().split('(contains')
        # Adding the ingredients to the list of ingredients
        ingredients_list = ingredients.strip().split()
        overall_ingredients += ingredients_list
        # Assigning the ingredients to each allergen encountered
        for allergen in allergens.strip()[0:-1].split(', '):
            allergen_ingredients_dict[allergen].append(ingredients_list)

# Obtaining the common ingredients encountered per allergen
for allergen in allergen_ingredients_dict:
    temp_set = set()
    for idx, ingredients_list in enumerate(allergen_ingredients_dict[allergen]):
        if idx == 0:
            temp_set = set(ingredients_list)
        else:
            temp_set = temp_set.intersection(ingredients_list)
    allergen_ingredients_dict[allergen] = list(temp_set)

# List to store the allergens that have been mapped to their respective ingredients
eliminated_allergens = []

# Loop until all the allergens have been mapped to their respective ingredient
while not check_one_to_one_allergen_ingredient(allergen_ingredients_dict):
    # Obtaining any new allergen that has been mapped to its ingredient 
    for allergen in allergen_ingredients_dict:
        if (len(allergen_ingredients_dict[allergen]) == 1) and (allergen not in eliminated_allergens):
            eliminated_allergens.append(allergen)
    # For each new allergen that has been mapped
    for eliminated_allergen in eliminated_allergens:
        # Obtaining the mapped ingredient
        allergen_ingredient = allergen_ingredients_dict[eliminated_allergen][0]
        # Removing the mapped ingredient from the list of candidate ingredients per allergen
        for allergen in allergen_ingredients_dict:
            # Only targeting those allergens that haven't been mapped yet
            if allergen not in eliminated_allergens:
                # If the mapped ingredient is in the list of candidate ingredients
                if allergen_ingredient in allergen_ingredients_dict[allergen]:
                    allergen_ingredients_dict[allergen].remove(allergen_ingredient)

# List to store the unsafe ingredients
unsafe_ingredients = []
for allergen in allergen_ingredients_dict:
    unsafe_ingredients.append(allergen_ingredients_dict[allergen][0])

# Obtaining the safe ingredients
safe_ingredients = list(set(overall_ingredients) - set(unsafe_ingredients))

# Counting the number of occurrences of each ingredient
c = Counter(overall_ingredients)

# Finding the sum of occurrences of safe ingredients
s = 0
for safe_ingredient in safe_ingredients:
    s += c[safe_ingredient]
print(f"Safe Ingredients Occurrence Sum : {s}")