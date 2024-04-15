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
        4,1,39,180,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,4,0,34,8,0,11,0,12,0,35,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,55,8,1,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,72,
        8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,100,8,2,10,2,12,
        2,103,9,2,1,3,1,3,1,3,1,3,5,3,109,8,3,10,3,12,3,112,9,3,1,4,1,4,
        1,4,1,4,5,4,118,8,4,10,4,12,4,121,9,4,1,5,1,5,1,5,1,5,5,5,127,8,
        5,10,5,12,5,130,9,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,141,
        8,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,11,1,11,1,12,1,12,4,12,164,8,12,11,12,12,12,165,
        1,12,1,12,1,13,1,13,1,13,1,13,3,13,174,8,13,1,14,1,14,1,15,1,15,
        1,15,0,1,4,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,5,1,0,
        23,24,1,0,19,20,2,0,21,21,24,24,1,0,29,32,1,0,27,28,195,0,33,1,0,
        0,0,2,54,1,0,0,0,4,71,1,0,0,0,6,104,1,0,0,0,8,113,1,0,0,0,10,122,
        1,0,0,0,12,131,1,0,0,0,14,134,1,0,0,0,16,142,1,0,0,0,18,145,1,0,
        0,0,20,151,1,0,0,0,22,159,1,0,0,0,24,161,1,0,0,0,26,173,1,0,0,0,
        28,175,1,0,0,0,30,177,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,35,
        1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,0,37,38,5,0,0,1,
        38,1,1,0,0,0,39,40,3,6,3,0,40,41,5,17,0,0,41,55,1,0,0,0,42,43,3,
        8,4,0,43,44,5,17,0,0,44,55,1,0,0,0,45,46,3,10,5,0,46,47,5,17,0,0,
        47,55,1,0,0,0,48,55,3,12,6,0,49,55,3,14,7,0,50,55,3,18,9,0,51,55,
        3,20,10,0,52,55,3,24,12,0,53,55,5,17,0,0,54,39,1,0,0,0,54,42,1,0,
        0,0,54,45,1,0,0,0,54,48,1,0,0,0,54,49,1,0,0,0,54,50,1,0,0,0,54,51,
        1,0,0,0,54,52,1,0,0,0,54,53,1,0,0,0,55,3,1,0,0,0,56,57,6,2,-1,0,
        57,58,7,0,0,0,58,72,3,4,2,9,59,72,5,34,0,0,60,72,5,33,0,0,61,72,
        5,35,0,0,62,72,5,36,0,0,63,72,5,37,0,0,64,65,5,2,0,0,65,66,3,4,2,
        0,66,67,5,3,0,0,67,72,1,0,0,0,68,69,5,37,0,0,69,70,5,4,0,0,70,72,
        3,4,2,1,71,56,1,0,0,0,71,59,1,0,0,0,71,60,1,0,0,0,71,61,1,0,0,0,
        71,62,1,0,0,0,71,63,1,0,0,0,71,64,1,0,0,0,71,68,1,0,0,0,72,101,1,
        0,0,0,73,74,10,16,0,0,74,75,7,1,0,0,75,100,3,4,2,17,76,77,10,15,
        0,0,77,78,7,2,0,0,78,100,3,4,2,16,79,80,10,14,0,0,80,81,5,22,0,0,
        81,100,3,4,2,15,82,83,10,13,0,0,83,84,5,25,0,0,84,100,3,4,2,14,85,
        86,10,12,0,0,86,87,5,26,0,0,87,100,3,4,2,13,88,89,10,11,0,0,89,90,
        3,28,14,0,90,91,3,4,2,12,91,100,1,0,0,0,92,93,10,10,0,0,93,94,3,
        30,15,0,94,95,3,4,2,11,95,100,1,0,0,0,96,97,10,8,0,0,97,98,5,1,0,
        0,98,100,3,4,2,9,99,73,1,0,0,0,99,76,1,0,0,0,99,79,1,0,0,0,99,82,
        1,0,0,0,99,85,1,0,0,0,99,88,1,0,0,0,99,92,1,0,0,0,99,96,1,0,0,0,
        100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,5,1,0,0,0,103,
        101,1,0,0,0,104,105,3,26,13,0,105,110,5,37,0,0,106,107,5,18,0,0,
        107,109,5,37,0,0,108,106,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,
        110,111,1,0,0,0,111,7,1,0,0,0,112,110,1,0,0,0,113,114,5,5,0,0,114,
        119,3,4,2,0,115,116,5,18,0,0,116,118,3,4,2,0,117,115,1,0,0,0,118,
        121,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,9,1,0,0,0,121,119,
        1,0,0,0,122,123,5,6,0,0,123,128,3,4,2,0,124,125,5,18,0,0,125,127,
        3,4,2,0,126,124,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,
        1,0,0,0,129,11,1,0,0,0,130,128,1,0,0,0,131,132,3,4,2,0,132,133,5,
        17,0,0,133,13,1,0,0,0,134,135,5,7,0,0,135,136,5,2,0,0,136,137,3,
        4,2,0,137,138,3,22,11,0,138,140,3,2,1,0,139,141,3,16,8,0,140,139,
        1,0,0,0,140,141,1,0,0,0,141,15,1,0,0,0,142,143,5,8,0,0,143,144,3,
        2,1,0,144,17,1,0,0,0,145,146,5,9,0,0,146,147,5,2,0,0,147,148,3,4,
        2,0,148,149,3,22,11,0,149,150,3,2,1,0,150,19,1,0,0,0,151,152,5,10,
        0,0,152,153,3,2,1,0,153,154,5,9,0,0,154,155,5,2,0,0,155,156,3,4,
        2,0,156,157,3,22,11,0,157,158,5,17,0,0,158,21,1,0,0,0,159,160,5,
        3,0,0,160,23,1,0,0,0,161,163,5,11,0,0,162,164,3,2,1,0,163,162,1,
        0,0,0,164,165,1,0,0,0,165,163,1,0,0,0,165,166,1,0,0,0,166,167,1,
        0,0,0,167,168,5,12,0,0,168,25,1,0,0,0,169,174,5,13,0,0,170,174,5,
        14,0,0,171,174,5,15,0,0,172,174,5,16,0,0,173,169,1,0,0,0,173,170,
        1,0,0,0,173,171,1,0,0,0,173,172,1,0,0,0,174,27,1,0,0,0,175,176,7,
        3,0,0,176,29,1,0,0,0,177,178,7,4,0,0,178,31,1,0,0,0,11,35,54,71,
        99,101,110,119,128,140,165,173
    ]

class ProjectGrammarParser ( Parser ):

    grammarFileName = "ProjectGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'('", "')'", "'='", "'write'", 
                     "'read'", "'if'", "'else'", "'while'", "'do'", "'{'", 
                     "'}'", "'int'", "'float'", "'bool'", "'string'", "';'", 
                     "','", "'*'", "'/'", "'+'", "'%'", "'!'", "'-'", "'&&'", 
                     "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", 
                      "STRING_TYPE", "SEMI", "COMMA", "MUL", "DIV", "ADD", 
                      "MOD", "NOT", "SUB", "AND", "OR", "EQUALS", "NOT_EQUALS", 
                      "LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", 
                      "GREATER_THAN_OR_EQUAL", "FLOAT", "INT", "BOOL", "STRING", 
                      "ID", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_declar = 3
    RULE_writeExpr = 4
    RULE_readExpr = 5
    RULE_expression = 6
    RULE_ifStatement = 7
    RULE_elseStatement = 8
    RULE_whileStatement = 9
    RULE_doWhileStatement = 10
    RULE_rpar = 11
    RULE_blockStatement = 12
    RULE_primitiveType = 13
    RULE_relationalOp = 14
    RULE_comparisonOp = 15

    ruleNames =  [ "program", "statement", "expr", "declar", "writeExpr", 
                   "readExpr", "expression", "ifStatement", "elseStatement", 
                   "whileStatement", "doWhileStatement", "rpar", "blockStatement", 
                   "primitiveType", "relationalOp", "comparisonOp" ]

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
    T__11=12
    INT_TYPE=13
    FLOAT_TYPE=14
    BOOL_TYPE=15
    STRING_TYPE=16
    SEMI=17
    COMMA=18
    MUL=19
    DIV=20
    ADD=21
    MOD=22
    NOT=23
    SUB=24
    AND=25
    OR=26
    EQUALS=27
    NOT_EQUALS=28
    LESS_THAN=29
    LESS_THAN_OR_EQUAL=30
    GREATER_THAN=31
    GREATER_THAN_OR_EQUAL=32
    FLOAT=33
    INT=34
    BOOL=35
    STRING=36
    ID=37
    COMMENT=38
    WS=39

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
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.statement()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 266313395940) != 0)):
                    break

            self.state = 37
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


        def expression(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExpressionContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(ProjectGrammarParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(ProjectGrammarParser.WhileStatementContext,0)


        def doWhileStatement(self):
            return self.getTypedRuleContext(ProjectGrammarParser.DoWhileStatementContext,0)


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
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.declar()
                self.state = 40
                self.match(ProjectGrammarParser.SEMI)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.writeExpr()
                self.state = 43
                self.match(ProjectGrammarParser.SEMI)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.readExpr()
                self.state = 46
                self.match(ProjectGrammarParser.SEMI)
                pass
            elif token in [2, 23, 24, 33, 34, 35, 36, 37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.expression()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 49
                self.ifStatement()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 6)
                self.state = 50
                self.whileStatement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 7)
                self.state = 51
                self.doWhileStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 8)
                self.state = 52
                self.blockStatement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 9)
                self.state = 53
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


    class OrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def OR(self):
            return self.getToken(ProjectGrammarParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)


    class ComparisonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # ComparisonOpContext
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


    class AndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def AND(self):
            return self.getToken(ProjectGrammarParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)


    class RelationalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # RelationalOpContext
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
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = ProjectGrammarParser.UnaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 57
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 58
                self.expr(9)
                pass

            elif la_ == 2:
                localctx = ProjectGrammarParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.match(ProjectGrammarParser.INT)
                pass

            elif la_ == 3:
                localctx = ProjectGrammarParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                self.match(ProjectGrammarParser.FLOAT)
                pass

            elif la_ == 4:
                localctx = ProjectGrammarParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 61
                self.match(ProjectGrammarParser.BOOL)
                pass

            elif la_ == 5:
                localctx = ProjectGrammarParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 62
                self.match(ProjectGrammarParser.STRING)
                pass

            elif la_ == 6:
                localctx = ProjectGrammarParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.match(ProjectGrammarParser.ID)
                pass

            elif la_ == 7:
                localctx = ProjectGrammarParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.match(ProjectGrammarParser.T__1)
                self.state = 65
                self.expr(0)
                self.state = 66
                self.match(ProjectGrammarParser.T__2)
                pass

            elif la_ == 8:
                localctx = ProjectGrammarParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 68
                self.match(ProjectGrammarParser.ID)
                self.state = 69
                self.match(ProjectGrammarParser.T__3)
                self.state = 70
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 99
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ProjectGrammarParser.MulDivContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 73
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 74
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 75
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = ProjectGrammarParser.AddSubContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 76
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 77
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==24):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 78
                        self.expr(16)
                        pass

                    elif la_ == 3:
                        localctx = ProjectGrammarParser.ModContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 79
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 80
                        localctx.op = self.match(ProjectGrammarParser.MOD)
                        self.state = 81
                        self.expr(15)
                        pass

                    elif la_ == 4:
                        localctx = ProjectGrammarParser.AndContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 82
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 83
                        localctx.op = self.match(ProjectGrammarParser.AND)
                        self.state = 84
                        self.expr(14)
                        pass

                    elif la_ == 5:
                        localctx = ProjectGrammarParser.OrContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 86
                        localctx.op = self.match(ProjectGrammarParser.OR)
                        self.state = 87
                        self.expr(13)
                        pass

                    elif la_ == 6:
                        localctx = ProjectGrammarParser.RelationalContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 88
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 89
                        localctx.op = self.relationalOp()
                        self.state = 90
                        self.expr(12)
                        pass

                    elif la_ == 7:
                        localctx = ProjectGrammarParser.ComparisonContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 92
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 93
                        localctx.op = self.comparisonOp()
                        self.state = 94
                        self.expr(11)
                        pass

                    elif la_ == 8:
                        localctx = ProjectGrammarParser.ConcatContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 96
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 97
                        self.match(ProjectGrammarParser.T__0)
                        self.state = 98
                        self.expr(9)
                        pass

             
                self.state = 103
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
            self.state = 104
            self.primitiveType()
            self.state = 105
            self.match(ProjectGrammarParser.ID)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 106
                self.match(ProjectGrammarParser.COMMA)
                self.state = 107
                self.match(ProjectGrammarParser.ID)
                self.state = 112
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
            self.state = 113
            self.match(ProjectGrammarParser.T__4)
            self.state = 114
            self.expr(0)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 115
                self.match(ProjectGrammarParser.COMMA)
                self.state = 116
                self.expr(0)
                self.state = 121
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
            self.state = 122
            self.match(ProjectGrammarParser.T__5)
            self.state = 123
            self.expr(0)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 124
                self.match(ProjectGrammarParser.COMMA)
                self.state = 125
                self.expr(0)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(ProjectGrammarParser.SEMI, 0)

        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = ProjectGrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.expr(0)
            self.state = 132
            self.match(ProjectGrammarParser.SEMI)
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


        def rpar(self):
            return self.getTypedRuleContext(ProjectGrammarParser.RparContext,0)


        def statement(self):
            return self.getTypedRuleContext(ProjectGrammarParser.StatementContext,0)


        def elseStatement(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ElseStatementContext,0)


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
        self.enterRule(localctx, 14, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(ProjectGrammarParser.T__6)
            self.state = 135
            self.match(ProjectGrammarParser.T__1)
            self.state = 136
            self.expr(0)
            self.state = 137
            self.rpar()
            self.state = 138
            self.statement()
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 139
                self.elseStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ProjectGrammarParser.StatementContext,0)


        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_elseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseStatement" ):
                listener.enterElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseStatement" ):
                listener.exitElseStatement(self)




    def elseStatement(self):

        localctx = ProjectGrammarParser.ElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(ProjectGrammarParser.T__7)
            self.state = 143
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


        def rpar(self):
            return self.getTypedRuleContext(ProjectGrammarParser.RparContext,0)


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
        self.enterRule(localctx, 18, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(ProjectGrammarParser.T__8)
            self.state = 146
            self.match(ProjectGrammarParser.T__1)
            self.state = 147
            self.expr(0)
            self.state = 148
            self.rpar()
            self.state = 149
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ProjectGrammarParser.StatementContext,0)


        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)


        def rpar(self):
            return self.getTypedRuleContext(ProjectGrammarParser.RparContext,0)


        def SEMI(self):
            return self.getToken(ProjectGrammarParser.SEMI, 0)

        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_doWhileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileStatement" ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileStatement" ):
                listener.exitDoWhileStatement(self)




    def doWhileStatement(self):

        localctx = ProjectGrammarParser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(ProjectGrammarParser.T__9)
            self.state = 152
            self.statement()
            self.state = 153
            self.match(ProjectGrammarParser.T__8)
            self.state = 154
            self.match(ProjectGrammarParser.T__1)
            self.state = 155
            self.expr(0)
            self.state = 156
            self.rpar()
            self.state = 157
            self.match(ProjectGrammarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RparContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_rpar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRpar" ):
                listener.enterRpar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRpar" ):
                listener.exitRpar(self)




    def rpar(self):

        localctx = ProjectGrammarParser.RparContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_rpar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(ProjectGrammarParser.T__2)
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
        self.enterRule(localctx, 24, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(ProjectGrammarParser.T__10)
            self.state = 163 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 162
                self.statement()
                self.state = 165 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 266313395940) != 0)):
                    break

            self.state = 167
            self.match(ProjectGrammarParser.T__11)
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
        self.enterRule(localctx, 26, self.RULE_primitiveType)
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                localctx.type_ = self.match(ProjectGrammarParser.INT_TYPE)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                localctx.type_ = self.match(ProjectGrammarParser.FLOAT_TYPE)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 171
                localctx.type_ = self.match(ProjectGrammarParser.BOOL_TYPE)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 172
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
        self.enterRule(localctx, 28, self.RULE_relationalOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063680) != 0)):
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
        self.enterRule(localctx, 30, self.RULE_comparisonOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
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
                return self.precpred(self._ctx, 16)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 8)
         




