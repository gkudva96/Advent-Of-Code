# Function definition to evaluate an expression
def evaluate_expression(operators, operands):
    for operator in operators:
        op1, op2 = operands[0], operands[1]
        del operands[ : 2]
        new_operand = op1 + op2 if operator == '+' else op1 * op2
        operands = [new_operand] + operands
    return operands[0]

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