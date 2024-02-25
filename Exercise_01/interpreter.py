def is_operator(char):
    return char in {'+', '-', '*', '/'}

def get_precedence(operator):
    if operator in {'+', '-'}:
        return 1
    elif operator in {'*', '/'}:
        return 2
    return 0

def convert_to_postfix(infix):
    output = []
    operators = []

    for char in infix:
        if char.isdigit():
            output.append(char)
        elif char == '(':
            operators.append(char)
        elif char == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()
        elif is_operator(char):
            if operators and char == operators[-1] and get_precedence(char) != 0:
                raise ValueError
            while operators and get_precedence(operators[-1]) >= get_precedence(char):
                output.append(operators.pop())
            operators.append(char)


    while operators:
        output.append(operators.pop())

    return output

def evaluate_postfix(postfix):
    stack = []
    print("Evaluating postfix:", postfix)
    for token in postfix:
        print("Processing token:", token)
        if token.isdigit():
            stack.append(int(token))
        elif is_operator(token):
            if len(stack) < 2:
                raise ValueError
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                if operand2 == 0:
                    raise ZeroDivisionError
                stack.append(operand1 / operand2)

    if len(stack) != 1:
        raise ValueError

    return stack[0]

def parse_and_evaluate(expression):
    try:
        expression = expression.replace(" ", "")
        postfix = convert_to_postfix(expression)
        result = evaluate_postfix(postfix)
        return int(result)
    except (ValueError, ZeroDivisionError):
        return "ERROR"

if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        expression = input().strip()
        result = parse_and_evaluate(expression)
        print(result)
