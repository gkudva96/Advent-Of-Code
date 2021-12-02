# Importing Libraries
import numpy as np
from functools import reduce

# Function definition to evaluate an expression
def evaluate_expression(operators, operands):
    # Finding all the positions of the '+' operator
    add_positions = np.where(np.array(operators) == '+')[0].tolist()
    # Until all the '+' operators have been removed
    while len(add_positions) != 0:
        insertion_index = add_positions[0]
        op1, op2 = operands[insertion_index], operands[insertion_index + 1]
        del operands[insertion_index : insertion_index + 2]
        new_operand = op1 + op2
        operands.insert(insertion_index, new_operand)
        operators.pop(insertion_index)
        add_positions = np.where(np.array(operators) == '+')[0].tolist()
    # Evaluating the expression consisting of only the '*' operators
    return reduce(lambda x, y : x * y, operands)

# Function definition to parse an expression
def parse_expression(expression):
    # List to store the operands and operators
    operands, operators = [], []
    # For each character in the expression
    for char in expression.strip():
        # If the character is an operand
        if char.isdigit():
            operands.append(int(char))
        # If the character is an operator
        if char in ['+', '*', '(']:
            operators.append(char)
            if char == '(':
                operands.append(char)
        # If the character is a closing parenthesis
        elif char == ')':
            # Temporary lists to store the operators and operands within the parenthesis
            temp_operands, temp_operators = [], []
            temp_operand, temp_operator = operands.pop(), operators.pop()
            # Until the matching opening parenthesis is reached
            while temp_operand != '(':
                temp_operands = [temp_operand] + temp_operands
                temp_operand = operands.pop()
            while temp_operator != '(':
                temp_operators = [temp_operator] + temp_operators
                temp_operator = operators.pop()
            # Evaluating the expression within the parenthesis
            expr_result = evaluate_expression(temp_operators, temp_operands)
            # Adding the result of the parenthesised expression to the overall list of operands
            operands.append(expr_result)
    # Final evaluation of the simplified expression (devoid of parenthesis)
    return evaluate_expression(operators, operands)

# List to store the contents of each line
lines = []

# Reading from the input file
with open('input.txt', 'r') as f:
    # Reading all the lines
    lines = f.readlines()

# Computing the values of all the expressions in the file
expression_values = list(map(parse_expression, lines))

# Computing the final sum
print(f"Sum of Expression Values : {sum(expression_values)}")