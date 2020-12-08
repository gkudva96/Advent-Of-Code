# Class Definition for the Bag class
class Bag:

    # Constructor Method
    def __init__(self, name):
        self.name = name
        self.contents = {}
    
    # Method to add a bag
    def add_content(self, name, quantity):
        self.contents[name] = quantity
    
    # Method to check for bag
    def check_content(self, name, bag_dict):
        contains_flag = []
        for content in self.contents:
            if content == name:
                contains_flag.append(True)
                break
            elif content == "none":
                continue
            else:
                contains_flag.append(bag_dict[content].check_content(name, bag_dict))
        return any(contains_flag)