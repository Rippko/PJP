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

    i = 0
    while i < len(infix):
        if infix[i].isdigit():
            num = ''
            while i < len(infix) and infix[i].isdigit():
                num += infix[i]
                i += 1
            output.append(num)
        elif infix[i] == '(':
            operators.append(infix[i])
            i += 1
        elif infix[i] == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()
            i += 1
        elif is_operator(infix[i]):
            if operators and infix[i] == operators[-1] and get_precedence(infix[i]) != 0:
                raise ValueError
            while operators and get_precedence(operators[-1]) >= get_precedence(infix[i]):
                output.append(operators.pop())
            operators.append(infix[i])
            i += 1
        else:
            i += 1

    while operators:
        output.append(operators.pop())

    return output

def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
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
