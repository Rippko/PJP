# Generated from ./AntlrComponents/ProjectGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ProjectGrammarParser import ProjectGrammarParser
else:
    from ProjectGrammarParser import ProjectGrammarParser

# This class defines a complete listener for a parse tree produced by ProjectGrammarParser.
class ProjectGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by ProjectGrammarParser#program.
    def enterProgram(self, ctx:ProjectGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#program.
    def exitProgram(self, ctx:ProjectGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#statement.
    def enterStatement(self, ctx:ProjectGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#statement.
    def exitStatement(self, ctx:ProjectGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#identifier.
    def enterIdentifier(self, ctx:ProjectGrammarParser.IdentifierContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#identifier.
    def exitIdentifier(self, ctx:ProjectGrammarParser.IdentifierContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#parens.
    def enterParens(self, ctx:ProjectGrammarParser.ParensContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#parens.
    def exitParens(self, ctx:ProjectGrammarParser.ParensContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#mod.
    def enterMod(self, ctx:ProjectGrammarParser.ModContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#mod.
    def exitMod(self, ctx:ProjectGrammarParser.ModContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#comparison.
    def enterComparison(self, ctx:ProjectGrammarParser.ComparisonContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#comparison.
    def exitComparison(self, ctx:ProjectGrammarParser.ComparisonContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#bool.
    def enterBool(self, ctx:ProjectGrammarParser.BoolContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#bool.
    def exitBool(self, ctx:ProjectGrammarParser.BoolContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#string.
    def enterString(self, ctx:ProjectGrammarParser.StringContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#string.
    def exitString(self, ctx:ProjectGrammarParser.StringContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#assignment.
    def enterAssignment(self, ctx:ProjectGrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#assignment.
    def exitAssignment(self, ctx:ProjectGrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#addSub.
    def enterAddSub(self, ctx:ProjectGrammarParser.AddSubContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#addSub.
    def exitAddSub(self, ctx:ProjectGrammarParser.AddSubContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#unary.
    def enterUnary(self, ctx:ProjectGrammarParser.UnaryContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#unary.
    def exitUnary(self, ctx:ProjectGrammarParser.UnaryContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#concat.
    def enterConcat(self, ctx:ProjectGrammarParser.ConcatContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#concat.
    def exitConcat(self, ctx:ProjectGrammarParser.ConcatContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#float.
    def enterFloat(self, ctx:ProjectGrammarParser.FloatContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#float.
    def exitFloat(self, ctx:ProjectGrammarParser.FloatContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#int.
    def enterInt(self, ctx:ProjectGrammarParser.IntContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#int.
    def exitInt(self, ctx:ProjectGrammarParser.IntContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#mulDiv.
    def enterMulDiv(self, ctx:ProjectGrammarParser.MulDivContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#mulDiv.
    def exitMulDiv(self, ctx:ProjectGrammarParser.MulDivContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#logical.
    def enterLogical(self, ctx:ProjectGrammarParser.LogicalContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#logical.
    def exitLogical(self, ctx:ProjectGrammarParser.LogicalContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#relational.
    def enterRelational(self, ctx:ProjectGrammarParser.RelationalContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#relational.
    def exitRelational(self, ctx:ProjectGrammarParser.RelationalContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#declar.
    def enterDeclar(self, ctx:ProjectGrammarParser.DeclarContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#declar.
    def exitDeclar(self, ctx:ProjectGrammarParser.DeclarContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#writeExpr.
    def enterWriteExpr(self, ctx:ProjectGrammarParser.WriteExprContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#writeExpr.
    def exitWriteExpr(self, ctx:ProjectGrammarParser.WriteExprContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#readExpr.
    def enterReadExpr(self, ctx:ProjectGrammarParser.ReadExprContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#readExpr.
    def exitReadExpr(self, ctx:ProjectGrammarParser.ReadExprContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#ifStatement.
    def enterIfStatement(self, ctx:ProjectGrammarParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#ifStatement.
    def exitIfStatement(self, ctx:ProjectGrammarParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#whileStatement.
    def enterWhileStatement(self, ctx:ProjectGrammarParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#whileStatement.
    def exitWhileStatement(self, ctx:ProjectGrammarParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#blockStatement.
    def enterBlockStatement(self, ctx:ProjectGrammarParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#blockStatement.
    def exitBlockStatement(self, ctx:ProjectGrammarParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#primitiveType.
    def enterPrimitiveType(self, ctx:ProjectGrammarParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#primitiveType.
    def exitPrimitiveType(self, ctx:ProjectGrammarParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#relationalOp.
    def enterRelationalOp(self, ctx:ProjectGrammarParser.RelationalOpContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#relationalOp.
    def exitRelationalOp(self, ctx:ProjectGrammarParser.RelationalOpContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#comparisonOp.
    def enterComparisonOp(self, ctx:ProjectGrammarParser.ComparisonOpContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#comparisonOp.
    def exitComparisonOp(self, ctx:ProjectGrammarParser.ComparisonOpContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#logicalOp.
    def enterLogicalOp(self, ctx:ProjectGrammarParser.LogicalOpContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#logicalOp.
    def exitLogicalOp(self, ctx:ProjectGrammarParser.LogicalOpContext):
        pass



del ProjectGrammarParser