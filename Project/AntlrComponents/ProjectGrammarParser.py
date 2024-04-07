# Generated from ./AntlrComponents/ProjectGrammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,160,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,4,0,
        28,8,0,11,0,12,0,29,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,50,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,67,8,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,5,2,93,8,2,10,2,12,2,96,9,2,1,3,1,3,1,3,1,3,5,3,102,
        8,3,10,3,12,3,105,9,3,1,4,1,4,1,4,1,4,5,4,111,8,4,10,4,12,4,114,
        9,4,1,5,1,5,1,5,1,5,5,5,120,8,5,10,5,12,5,123,9,5,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,3,6,132,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,4,8,142,
        8,8,11,8,12,8,143,1,8,1,8,1,9,1,9,1,9,1,9,3,9,152,8,9,1,10,1,10,
        1,11,1,11,1,12,1,12,1,12,0,1,4,13,0,2,4,6,8,10,12,14,16,18,20,22,
        24,0,6,1,0,22,23,1,0,18,19,2,0,20,20,23,23,1,0,28,31,1,0,26,27,1,
        0,24,25,176,0,27,1,0,0,0,2,49,1,0,0,0,4,66,1,0,0,0,6,97,1,0,0,0,
        8,106,1,0,0,0,10,115,1,0,0,0,12,124,1,0,0,0,14,133,1,0,0,0,16,139,
        1,0,0,0,18,151,1,0,0,0,20,153,1,0,0,0,22,155,1,0,0,0,24,157,1,0,
        0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,1,0,0,0,29,30,
        1,0,0,0,30,31,1,0,0,0,31,32,5,0,0,1,32,1,1,0,0,0,33,34,3,6,3,0,34,
        35,5,16,0,0,35,50,1,0,0,0,36,37,3,8,4,0,37,38,5,16,0,0,38,50,1,0,
        0,0,39,40,3,10,5,0,40,41,5,16,0,0,41,50,1,0,0,0,42,43,3,4,2,0,43,
        44,5,16,0,0,44,50,1,0,0,0,45,50,3,12,6,0,46,50,3,14,7,0,47,50,3,
        16,8,0,48,50,5,16,0,0,49,33,1,0,0,0,49,36,1,0,0,0,49,39,1,0,0,0,
        49,42,1,0,0,0,49,45,1,0,0,0,49,46,1,0,0,0,49,47,1,0,0,0,49,48,1,
        0,0,0,50,3,1,0,0,0,51,52,6,2,-1,0,52,53,7,0,0,0,53,67,3,4,2,10,54,
        67,5,33,0,0,55,67,5,32,0,0,56,67,5,34,0,0,57,67,5,35,0,0,58,67,5,
        36,0,0,59,60,5,2,0,0,60,61,3,4,2,0,61,62,5,3,0,0,62,67,1,0,0,0,63,
        64,5,36,0,0,64,65,5,4,0,0,65,67,3,4,2,1,66,51,1,0,0,0,66,54,1,0,
        0,0,66,55,1,0,0,0,66,56,1,0,0,0,66,57,1,0,0,0,66,58,1,0,0,0,66,59,
        1,0,0,0,66,63,1,0,0,0,67,94,1,0,0,0,68,69,10,15,0,0,69,70,7,1,0,
        0,70,93,3,4,2,16,71,72,10,14,0,0,72,73,7,2,0,0,73,93,3,4,2,15,74,
        75,10,13,0,0,75,76,5,21,0,0,76,93,3,4,2,14,77,78,10,12,0,0,78,79,
        3,20,10,0,79,80,3,4,2,13,80,93,1,0,0,0,81,82,10,11,0,0,82,83,3,22,
        11,0,83,84,3,4,2,12,84,93,1,0,0,0,85,86,10,9,0,0,86,87,3,24,12,0,
        87,88,3,4,2,10,88,93,1,0,0,0,89,90,10,8,0,0,90,91,5,1,0,0,91,93,
        3,4,2,9,92,68,1,0,0,0,92,71,1,0,0,0,92,74,1,0,0,0,92,77,1,0,0,0,
        92,81,1,0,0,0,92,85,1,0,0,0,92,89,1,0,0,0,93,96,1,0,0,0,94,92,1,
        0,0,0,94,95,1,0,0,0,95,5,1,0,0,0,96,94,1,0,0,0,97,98,3,18,9,0,98,
        103,5,36,0,0,99,100,5,17,0,0,100,102,5,36,0,0,101,99,1,0,0,0,102,
        105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,7,1,0,0,0,105,103,
        1,0,0,0,106,107,5,5,0,0,107,112,3,4,2,0,108,109,5,17,0,0,109,111,
        3,4,2,0,110,108,1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,
        1,0,0,0,113,9,1,0,0,0,114,112,1,0,0,0,115,116,5,6,0,0,116,121,5,
        36,0,0,117,118,5,17,0,0,118,120,5,36,0,0,119,117,1,0,0,0,120,123,
        1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,11,1,0,0,0,123,121,1,
        0,0,0,124,125,5,7,0,0,125,126,5,2,0,0,126,127,3,4,2,0,127,128,5,
        3,0,0,128,131,3,2,1,0,129,130,5,8,0,0,130,132,3,2,1,0,131,129,1,
        0,0,0,131,132,1,0,0,0,132,13,1,0,0,0,133,134,5,9,0,0,134,135,5,2,
        0,0,135,136,3,4,2,0,136,137,5,3,0,0,137,138,3,2,1,0,138,15,1,0,0,
        0,139,141,5,10,0,0,140,142,3,2,1,0,141,140,1,0,0,0,142,143,1,0,0,
        0,143,141,1,0,0,0,143,144,1,0,0,0,144,145,1,0,0,0,145,146,5,11,0,
        0,146,17,1,0,0,0,147,152,5,12,0,0,148,152,5,13,0,0,149,152,5,14,
        0,0,150,152,5,15,0,0,151,147,1,0,0,0,151,148,1,0,0,0,151,149,1,0,
        0,0,151,150,1,0,0,0,152,19,1,0,0,0,153,154,7,3,0,0,154,21,1,0,0,
        0,155,156,7,4,0,0,156,23,1,0,0,0,157,158,7,5,0,0,158,25,1,0,0,0,
        11,29,49,66,92,94,103,112,121,131,143,151
    ]

class ProjectGrammarParser ( Parser ):

    grammarFileName = "ProjectGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'('", "')'", "'='", "'write'", 
                     "'read'", "'if'", "'else'", "'while'", "'{'", "'}'", 
                     "'int'", "'float'", "'bool'", "'string'", "';'", "','", 
                     "'*'", "'/'", "'+'", "'%'", "'!'", "'-'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", "STRING_TYPE", 
                      "SEMI", "COMMA", "MUL", "DIV", "ADD", "MOD", "NOT", 
                      "SUB", "AND", "OR", "EQUALS", "NOT_EQUALS", "LESS_THAN", 
                      "LESS_THAN_OR_EQUAL", "GREATER_THAN", "GREATER_THAN_OR_EQUAL", 
                      "FLOAT", "INT", "BOOL", "STRING", "ID", "COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_declar = 3
    RULE_writeExpr = 4
    RULE_readExpr = 5
    RULE_ifStatement = 6
    RULE_whileStatement = 7
    RULE_blockStatement = 8
    RULE_primitiveType = 9
    RULE_relationalOp = 10
    RULE_comparisonOp = 11
    RULE_logicalOp = 12

    ruleNames =  [ "program", "statement", "expr", "declar", "writeExpr", 
                   "readExpr", "ifStatement", "whileStatement", "blockStatement", 
                   "primitiveType", "relationalOp", "comparisonOp", "logicalOp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    INT_TYPE=12
    FLOAT_TYPE=13
    BOOL_TYPE=14
    STRING_TYPE=15
    SEMI=16
    COMMA=17
    MUL=18
    DIV=19
    ADD=20
    MOD=21
    NOT=22
    SUB=23
    AND=24
    OR=25
    EQUALS=26
    NOT_EQUALS=27
    LESS_THAN=28
    LESS_THAN_OR_EQUAL=29
    GREATER_THAN=30
    GREATER_THAN_OR_EQUAL=31
    FLOAT=32
    INT=33
    BOOL=34
    STRING=35
    ID=36
    COMMENT=37
    WS=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ProjectGrammarParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ProjectGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.statement()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 133156697828) != 0)):
                    break

            self.state = 31
            self.match(ProjectGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declar(self):
            return self.getTypedRuleContext(ProjectGrammarParser.DeclarContext,0)


        def SEMI(self):
            return self.getToken(ProjectGrammarParser.SEMI, 0)

        def writeExpr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.WriteExprContext,0)


        def readExpr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ReadExprContext,0)


        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(ProjectGrammarParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(ProjectGrammarParser.WhileStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(ProjectGrammarParser.BlockStatementContext,0)


        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ProjectGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 13, 14, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.declar()
                self.state = 34
                self.match(ProjectGrammarParser.SEMI)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.writeExpr()
                self.state = 37
                self.match(ProjectGrammarParser.SEMI)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.readExpr()
                self.state = 40
                self.match(ProjectGrammarParser.SEMI)
                pass
            elif token in [2, 22, 23, 32, 33, 34, 35, 36]:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.expr(0)
                self.state = 43
                self.match(ProjectGrammarParser.SEMI)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 45
                self.ifStatement()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 6)
                self.state = 46
                self.whileStatement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 7)
                self.state = 47
                self.blockStatement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 8)
                self.state = 48
                self.match(ProjectGrammarParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IdentifierContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ProjectGrammarParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class ModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def MOD(self):
            return self.getToken(ProjectGrammarParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMod" ):
                listener.enterMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMod" ):
                listener.exitMod(self)


    class ComparisonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def comparisonOp(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ComparisonOpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)


    class BoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(ProjectGrammarParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ProjectGrammarParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class AssignmentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ProjectGrammarParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def ADD(self):
            return self.getToken(ProjectGrammarParser.ADD, 0)
        def SUB(self):
            return self.getToken(ProjectGrammarParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class UnaryContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)

        def SUB(self):
            return self.getToken(ProjectGrammarParser.SUB, 0)
        def NOT(self):
            return self.getToken(ProjectGrammarParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)


    class ConcatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcat" ):
                listener.enterConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcat" ):
                listener.exitConcat(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(ProjectGrammarParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ProjectGrammarParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def MUL(self):
            return self.getToken(ProjectGrammarParser.MUL, 0)
        def DIV(self):
            return self.getToken(ProjectGrammarParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class LogicalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def logicalOp(self):
            return self.getTypedRuleContext(ProjectGrammarParser.LogicalOpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical" ):
                listener.enterLogical(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical" ):
                listener.exitLogical(self)


    class RelationalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def relationalOp(self):
            return self.getTypedRuleContext(ProjectGrammarParser.RelationalOpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational" ):
                listener.enterRelational(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational" ):
                listener.exitRelational(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ProjectGrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = ProjectGrammarParser.UnaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 52
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 53
                self.expr(10)
                pass

            elif la_ == 2:
                localctx = ProjectGrammarParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 54
                self.match(ProjectGrammarParser.INT)
                pass

            elif la_ == 3:
                localctx = ProjectGrammarParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 55
                self.match(ProjectGrammarParser.FLOAT)
                pass

            elif la_ == 4:
                localctx = ProjectGrammarParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 56
                self.match(ProjectGrammarParser.BOOL)
                pass

            elif la_ == 5:
                localctx = ProjectGrammarParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 57
                self.match(ProjectGrammarParser.STRING)
                pass

            elif la_ == 6:
                localctx = ProjectGrammarParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 58
                self.match(ProjectGrammarParser.ID)
                pass

            elif la_ == 7:
                localctx = ProjectGrammarParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.match(ProjectGrammarParser.T__1)
                self.state = 60
                self.expr(0)
                self.state = 61
                self.match(ProjectGrammarParser.T__2)
                pass

            elif la_ == 8:
                localctx = ProjectGrammarParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.match(ProjectGrammarParser.ID)
                self.state = 64
                self.match(ProjectGrammarParser.T__3)
                self.state = 65
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 92
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ProjectGrammarParser.MulDivContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 68
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 69
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 70
                        self.expr(16)
                        pass

                    elif la_ == 2:
                        localctx = ProjectGrammarParser.AddSubContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 71
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 72
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==23):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 73
                        self.expr(15)
                        pass

                    elif la_ == 3:
                        localctx = ProjectGrammarParser.ModContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 74
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 75
                        localctx.op = self.match(ProjectGrammarParser.MOD)
                        self.state = 76
                        self.expr(14)
                        pass

                    elif la_ == 4:
                        localctx = ProjectGrammarParser.RelationalContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 77
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 78
                        self.relationalOp()
                        self.state = 79
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = ProjectGrammarParser.ComparisonContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 81
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 82
                        self.comparisonOp()
                        self.state = 83
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = ProjectGrammarParser.LogicalContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 86
                        self.logicalOp()
                        self.state = 87
                        self.expr(10)
                        pass

                    elif la_ == 7:
                        localctx = ProjectGrammarParser.ConcatContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 89
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 90
                        self.match(ProjectGrammarParser.T__0)
                        self.state = 91
                        self.expr(9)
                        pass

             
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DeclarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(ProjectGrammarParser.PrimitiveTypeContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectGrammarParser.ID)
            else:
                return self.getToken(ProjectGrammarParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectGrammarParser.COMMA)
            else:
                return self.getToken(ProjectGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_declar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclar" ):
                listener.enterDeclar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclar" ):
                listener.exitDeclar(self)




    def declar(self):

        localctx = ProjectGrammarParser.DeclarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.primitiveType()
            self.state = 98
            self.match(ProjectGrammarParser.ID)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 99
                self.match(ProjectGrammarParser.COMMA)
                self.state = 100
                self.match(ProjectGrammarParser.ID)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectGrammarParser.COMMA)
            else:
                return self.getToken(ProjectGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_writeExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteExpr" ):
                listener.enterWriteExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteExpr" ):
                listener.exitWriteExpr(self)




    def writeExpr(self):

        localctx = ProjectGrammarParser.WriteExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_writeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(ProjectGrammarParser.T__4)
            self.state = 107
            self.expr(0)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 108
                self.match(ProjectGrammarParser.COMMA)
                self.state = 109
                self.expr(0)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectGrammarParser.ID)
            else:
                return self.getToken(ProjectGrammarParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectGrammarParser.COMMA)
            else:
                return self.getToken(ProjectGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_readExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadExpr" ):
                listener.enterReadExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadExpr" ):
                listener.exitReadExpr(self)




    def readExpr(self):

        localctx = ProjectGrammarParser.ReadExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_readExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(ProjectGrammarParser.T__5)
            self.state = 116
            self.match(ProjectGrammarParser.ID)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 117
                self.match(ProjectGrammarParser.COMMA)
                self.state = 118
                self.match(ProjectGrammarParser.ID)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = ProjectGrammarParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(ProjectGrammarParser.T__6)
            self.state = 125
            self.match(ProjectGrammarParser.T__1)
            self.state = 126
            self.expr(0)
            self.state = 127
            self.match(ProjectGrammarParser.T__2)
            self.state = 128
            self.statement()
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 129
                self.match(ProjectGrammarParser.T__7)
                self.state = 130
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)


        def statement(self):
            return self.getTypedRuleContext(ProjectGrammarParser.StatementContext,0)


        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = ProjectGrammarParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(ProjectGrammarParser.T__8)
            self.state = 134
            self.match(ProjectGrammarParser.T__1)
            self.state = 135
            self.expr(0)
            self.state = 136
            self.match(ProjectGrammarParser.T__2)
            self.state = 137
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_blockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)




    def blockStatement(self):

        localctx = ProjectGrammarParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(ProjectGrammarParser.T__9)
            self.state = 141 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 140
                self.statement()
                self.state = 143 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 133156697828) != 0)):
                    break

            self.state = 145
            self.match(ProjectGrammarParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None # Token

        def INT_TYPE(self):
            return self.getToken(ProjectGrammarParser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(ProjectGrammarParser.FLOAT_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(ProjectGrammarParser.BOOL_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(ProjectGrammarParser.STRING_TYPE, 0)

        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_primitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveType" ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveType" ):
                listener.exitPrimitiveType(self)




    def primitiveType(self):

        localctx = ProjectGrammarParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_primitiveType)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                localctx.type_ = self.match(ProjectGrammarParser.INT_TYPE)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                localctx.type_ = self.match(ProjectGrammarParser.FLOAT_TYPE)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
                localctx.type_ = self.match(ProjectGrammarParser.BOOL_TYPE)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 150
                localctx.type_ = self.match(ProjectGrammarParser.STRING_TYPE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS_THAN(self):
            return self.getToken(ProjectGrammarParser.LESS_THAN, 0)

        def LESS_THAN_OR_EQUAL(self):
            return self.getToken(ProjectGrammarParser.LESS_THAN_OR_EQUAL, 0)

        def GREATER_THAN(self):
            return self.getToken(ProjectGrammarParser.GREATER_THAN, 0)

        def GREATER_THAN_OR_EQUAL(self):
            return self.getToken(ProjectGrammarParser.GREATER_THAN_OR_EQUAL, 0)

        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_relationalOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalOp" ):
                listener.enterRelationalOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalOp" ):
                listener.exitRelationalOp(self)




    def relationalOp(self):

        localctx = ProjectGrammarParser.RelationalOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_relationalOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4026531840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(ProjectGrammarParser.EQUALS, 0)

        def NOT_EQUALS(self):
            return self.getToken(ProjectGrammarParser.NOT_EQUALS, 0)

        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_comparisonOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOp" ):
                listener.enterComparisonOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOp" ):
                listener.exitComparisonOp(self)




    def comparisonOp(self):

        localctx = ProjectGrammarParser.ComparisonOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_comparisonOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(ProjectGrammarParser.AND, 0)

        def OR(self):
            return self.getToken(ProjectGrammarParser.OR, 0)

        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_logicalOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOp" ):
                listener.enterLogicalOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOp" ):
                listener.exitLogicalOp(self)




    def logicalOp(self):

        localctx = ProjectGrammarParser.LogicalOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_logicalOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         




