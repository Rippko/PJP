# Generated from ./AntlrComponents/ProjectGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,38,244,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,1,0,1,1,
        1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,
        1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,
        1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,
        1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,
        1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,25,1,25,1,25,1,26,1,26,1,26,
        1,27,1,27,1,28,1,28,1,28,1,29,1,29,1,30,1,30,1,30,1,31,4,31,176,
        8,31,11,31,12,31,177,1,32,3,32,181,8,32,1,32,4,32,184,8,32,11,32,
        12,32,185,1,32,1,32,4,32,190,8,32,11,32,12,32,191,1,33,1,33,3,33,
        196,8,33,1,33,1,33,5,33,200,8,33,10,33,12,33,203,9,33,3,33,205,8,
        33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,3,34,216,8,34,1,
        35,1,35,5,35,220,8,35,10,35,12,35,223,9,35,1,35,1,35,1,36,1,36,1,
        36,1,36,5,36,231,8,36,10,36,12,36,234,9,36,1,36,1,36,1,37,4,37,239,
        8,37,11,37,12,37,240,1,37,1,37,0,0,38,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,
        37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,
        59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,1,0,6,2,0,
        65,90,97,122,1,0,48,57,1,0,49,57,1,0,34,34,2,0,10,10,13,13,3,0,9,
        10,13,13,32,32,254,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,
        0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,
        0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,
        0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,
        0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,
        0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,
        0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,
        0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,1,77,1,0,0,
        0,3,79,1,0,0,0,5,81,1,0,0,0,7,83,1,0,0,0,9,85,1,0,0,0,11,91,1,0,
        0,0,13,96,1,0,0,0,15,99,1,0,0,0,17,104,1,0,0,0,19,110,1,0,0,0,21,
        112,1,0,0,0,23,114,1,0,0,0,25,118,1,0,0,0,27,124,1,0,0,0,29,129,
        1,0,0,0,31,136,1,0,0,0,33,138,1,0,0,0,35,140,1,0,0,0,37,142,1,0,
        0,0,39,144,1,0,0,0,41,146,1,0,0,0,43,148,1,0,0,0,45,150,1,0,0,0,
        47,153,1,0,0,0,49,156,1,0,0,0,51,158,1,0,0,0,53,161,1,0,0,0,55,164,
        1,0,0,0,57,166,1,0,0,0,59,169,1,0,0,0,61,171,1,0,0,0,63,175,1,0,
        0,0,65,180,1,0,0,0,67,204,1,0,0,0,69,215,1,0,0,0,71,217,1,0,0,0,
        73,226,1,0,0,0,75,238,1,0,0,0,77,78,5,46,0,0,78,2,1,0,0,0,79,80,
        5,40,0,0,80,4,1,0,0,0,81,82,5,41,0,0,82,6,1,0,0,0,83,84,5,61,0,0,
        84,8,1,0,0,0,85,86,5,119,0,0,86,87,5,114,0,0,87,88,5,105,0,0,88,
        89,5,116,0,0,89,90,5,101,0,0,90,10,1,0,0,0,91,92,5,114,0,0,92,93,
        5,101,0,0,93,94,5,97,0,0,94,95,5,100,0,0,95,12,1,0,0,0,96,97,5,105,
        0,0,97,98,5,102,0,0,98,14,1,0,0,0,99,100,5,101,0,0,100,101,5,108,
        0,0,101,102,5,115,0,0,102,103,5,101,0,0,103,16,1,0,0,0,104,105,5,
        119,0,0,105,106,5,104,0,0,106,107,5,105,0,0,107,108,5,108,0,0,108,
        109,5,101,0,0,109,18,1,0,0,0,110,111,5,123,0,0,111,20,1,0,0,0,112,
        113,5,125,0,0,113,22,1,0,0,0,114,115,5,105,0,0,115,116,5,110,0,0,
        116,117,5,116,0,0,117,24,1,0,0,0,118,119,5,102,0,0,119,120,5,108,
        0,0,120,121,5,111,0,0,121,122,5,97,0,0,122,123,5,116,0,0,123,26,
        1,0,0,0,124,125,5,98,0,0,125,126,5,111,0,0,126,127,5,111,0,0,127,
        128,5,108,0,0,128,28,1,0,0,0,129,130,5,115,0,0,130,131,5,116,0,0,
        131,132,5,114,0,0,132,133,5,105,0,0,133,134,5,110,0,0,134,135,5,
        103,0,0,135,30,1,0,0,0,136,137,5,59,0,0,137,32,1,0,0,0,138,139,5,
        44,0,0,139,34,1,0,0,0,140,141,5,42,0,0,141,36,1,0,0,0,142,143,5,
        47,0,0,143,38,1,0,0,0,144,145,5,43,0,0,145,40,1,0,0,0,146,147,5,
        45,0,0,147,42,1,0,0,0,148,149,5,37,0,0,149,44,1,0,0,0,150,151,5,
        38,0,0,151,152,5,38,0,0,152,46,1,0,0,0,153,154,5,124,0,0,154,155,
        5,124,0,0,155,48,1,0,0,0,156,157,5,33,0,0,157,50,1,0,0,0,158,159,
        5,61,0,0,159,160,5,61,0,0,160,52,1,0,0,0,161,162,5,33,0,0,162,163,
        5,61,0,0,163,54,1,0,0,0,164,165,5,60,0,0,165,56,1,0,0,0,166,167,
        5,60,0,0,167,168,5,61,0,0,168,58,1,0,0,0,169,170,5,62,0,0,170,60,
        1,0,0,0,171,172,5,62,0,0,172,173,5,61,0,0,173,62,1,0,0,0,174,176,
        7,0,0,0,175,174,1,0,0,0,176,177,1,0,0,0,177,175,1,0,0,0,177,178,
        1,0,0,0,178,64,1,0,0,0,179,181,5,45,0,0,180,179,1,0,0,0,180,181,
        1,0,0,0,181,183,1,0,0,0,182,184,7,1,0,0,183,182,1,0,0,0,184,185,
        1,0,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,187,1,0,0,0,187,189,
        5,46,0,0,188,190,7,1,0,0,189,188,1,0,0,0,190,191,1,0,0,0,191,189,
        1,0,0,0,191,192,1,0,0,0,192,66,1,0,0,0,193,205,5,48,0,0,194,196,
        5,45,0,0,195,194,1,0,0,0,195,196,1,0,0,0,196,197,1,0,0,0,197,201,
        7,2,0,0,198,200,7,1,0,0,199,198,1,0,0,0,200,203,1,0,0,0,201,199,
        1,0,0,0,201,202,1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,204,193,
        1,0,0,0,204,195,1,0,0,0,205,68,1,0,0,0,206,207,5,116,0,0,207,208,
        5,114,0,0,208,209,5,117,0,0,209,216,5,101,0,0,210,211,5,102,0,0,
        211,212,5,97,0,0,212,213,5,108,0,0,213,214,5,115,0,0,214,216,5,101,
        0,0,215,206,1,0,0,0,215,210,1,0,0,0,216,70,1,0,0,0,217,221,5,34,
        0,0,218,220,8,3,0,0,219,218,1,0,0,0,220,223,1,0,0,0,221,219,1,0,
        0,0,221,222,1,0,0,0,222,224,1,0,0,0,223,221,1,0,0,0,224,225,5,34,
        0,0,225,72,1,0,0,0,226,227,5,47,0,0,227,228,5,47,0,0,228,232,1,0,
        0,0,229,231,8,4,0,0,230,229,1,0,0,0,231,234,1,0,0,0,232,230,1,0,
        0,0,232,233,1,0,0,0,233,235,1,0,0,0,234,232,1,0,0,0,235,236,6,36,
        0,0,236,74,1,0,0,0,237,239,7,5,0,0,238,237,1,0,0,0,239,240,1,0,0,
        0,240,238,1,0,0,0,240,241,1,0,0,0,241,242,1,0,0,0,242,243,6,37,0,
        0,243,76,1,0,0,0,12,0,177,180,185,191,195,201,204,215,221,232,240,
        1,6,0,0
    ]

class ProjectGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    INT_TYPE = 12
    FLOAT_TYPE = 13
    BOOL_TYPE = 14
    STRING_TYPE = 15
    SEMI = 16
    COMMA = 17
    MUL = 18
    DIV = 19
    ADD = 20
    SUB = 21
    MOD = 22
    AND = 23
    OR = 24
    NOT = 25
    EQUALS = 26
    NOT_EQUALS = 27
    LESS_THAN = 28
    LESS_THAN_OR_EQUAL = 29
    GREATER_THAN = 30
    GREATER_THAN_OR_EQUAL = 31
    ID = 32
    FLOAT = 33
    INT = 34
    BOOL = 35
    STRING = 36
    COMMENT = 37
    WS = 38

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.'", "'('", "')'", "'='", "'write'", "'read'", "'if'", "'else'", 
            "'while'", "'{'", "'}'", "'int'", "'float'", "'bool'", "'string'", 
            "';'", "','", "'*'", "'/'", "'+'", "'-'", "'%'", "'&&'", "'||'", 
            "'!'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>",
            "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", "STRING_TYPE", "SEMI", 
            "COMMA", "MUL", "DIV", "ADD", "SUB", "MOD", "AND", "OR", "NOT", 
            "EQUALS", "NOT_EQUALS", "LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", 
            "GREATER_THAN_OR_EQUAL", "ID", "FLOAT", "INT", "BOOL", "STRING", 
            "COMMENT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "INT_TYPE", "FLOAT_TYPE", 
                  "BOOL_TYPE", "STRING_TYPE", "SEMI", "COMMA", "MUL", "DIV", 
                  "ADD", "SUB", "MOD", "AND", "OR", "NOT", "EQUALS", "NOT_EQUALS", 
                  "LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", "GREATER_THAN_OR_EQUAL", 
                  "ID", "FLOAT", "INT", "BOOL", "STRING", "COMMENT", "WS" ]

    grammarFileName = "ProjectGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


