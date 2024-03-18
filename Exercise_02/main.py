from lexical_analyzer import LexicalAnalyzer
from token import Token
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        return

    file_path = sys.argv[1]
    
    try:
        with open(file_path, 'r') as file:
            input_text = file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return

    lexical_analyzer = LexicalAnalyzer()
    tokens = lexical_analyzer.tokenize(input_text)

    print("Tokens:")
    for token in tokens:
        print(token)

if __name__ == "__main__":
    main()