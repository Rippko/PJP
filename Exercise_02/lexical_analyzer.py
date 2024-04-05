from token import Token
import re
import sys

class LexicalAnalyzer:
    def __init__(self):
        self.identifier_regex = re.compile(r'^[a-zA-Z][a-zA-Z0-9]*$')
        self.number_regex = re.compile(r'^-?\d+$')
        self.operator_regex = re.compile(r'^[+\-*/]$')
        self.delimiter_regex = re.compile(r'^[();]$')
        self.keyword_regex = re.compile(r'^(div|mod)$')

    def tokenize(self, input_text):
        lines = input_text.split('\n')
        tokens = []

        for line in lines:
            line_without_comments = re.sub(r'\/\/.*', '', line)
            
            symbols = re.findall(r'[a-zA-Z0-9]+|[^a-zA-Z0-9\s]', line_without_comments)

            for symbol in symbols:
                if symbol.isspace():
                    continue
                elif self.identifier_regex.match(symbol) and not self.keyword_regex.match(symbol):
                    tokens.append(Token('ID', symbol))
                elif self.number_regex.match(symbol):
                    tokens.append(Token('NUM', symbol))
                elif self.operator_regex.match(symbol):
                    tokens.append(Token('OP', symbol))
                elif self.delimiter_regex.match(symbol):
                    if symbol == ';':
                        tokens.append(Token('SEMICOLON', None))
                    elif symbol == '(':
                        tokens.append(Token('LPAR', None))
                    else:
                        tokens.append(Token('RPAR', None))
                elif self.keyword_regex.match(symbol):
                    if symbol == 'div':
                        tokens.append(Token('DIV', None))
                    else:
                        tokens.append(Token('MOD', None))
                else:
                    print(f'Unknown token: {symbol}')

        return tokens