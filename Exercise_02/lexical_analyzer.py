from token import Token
import re


def tokenize(input_text):
    identifier_regex = re.compile(r'^[a-zA-Z][a-zA-Z0-9]*$')
    number_regex = re.compile(r'^-?\d+$')
    operator_regex = re.compile(r'^[+\-*/]$')
    delimiter_regex = re.compile(r'^[();]$')
    keyword_regex = re.compile(r'^(div|mod)$')

    lines = input_text.split('\n')
    tokens = []

    for line in lines:
        line_without_comments = re.sub(r'\/\/.*', '', line)
        
        symbols = re.findall(r'[a-zA-Z0-9]+|[^a-zA-Z0-9\s]', line_without_comments)

        for symbol in symbols:
            if symbol.isspace():
                continue
            elif identifier_regex.match(symbol) and not keyword_regex.match(symbol):
                tokens.append(Token('ID', symbol))
            elif number_regex.match(symbol):
                tokens.append(Token('NUM', symbol))
            elif operator_regex.match(symbol):
                tokens.append(Token('OP', symbol))
            elif delimiter_regex.match(symbol):
                if symbol == ';':
                    tokens.append(Token('SEMICOLON', None))
                elif symbol == '(':
                    tokens.append(Token('LPAR', None))
                else:
                    tokens.append(Token('RPAR', None))
            elif keyword_regex.match(symbol):
                if symbol == 'div':
                    tokens.append(Token('DIV', None))
                else:
                    tokens.append(Token('MOD', None))
            else:
                print(f'Unknown token: {symbol}')

    return tokens

print("Enter the input:")
input_text = ""
while True:
    line = input()
    if not line:
        break
    input_text += line + "\n"

tokens = tokenize(input_text)

print("\nTokens:")
for token in tokens:
    print(token)
