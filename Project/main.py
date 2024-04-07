import sys
from antlr4 import *
from AntlrComponents.ProjectGrammarLexer import ProjectGrammarLexer as GrammarLexer
from AntlrComponents.ProjectGrammarParser import ProjectGrammarParser as GrammarParser
from AntlrComponents.ProjectGrammarListener import ProjectGrammarListener as GrammarListener

from Components.Listeners.EvalListener import EvalListener
from Components.Listeners.ErrorListener import CustomErrorListener

def main(argv):
    if len(argv) < 2:
        print("Usage: python main.py <input file>")
        return
    
    input = FileStream(argv[1])
    lexer = GrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())
    prog = parser.program()
    
    if parser.getNumberOfSyntaxErrors() != 0:
        exit(0)
        
    walker = ParseTreeWalker()
    listener = EvalListener()
    walker.walk(listener, prog)
    
    if listener.has_error:
        exit(0)
        
    print('No errors found')
    
if __name__ == '__main__':
    main(sys.argv)