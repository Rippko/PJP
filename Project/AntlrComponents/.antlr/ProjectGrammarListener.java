// Generated from c:/Programování/3.roèník/6.semestr/PJP/Project/AntlrComponents/ProjectGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ProjectGrammarParser}.
 */
public interface ProjectGrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ProjectGrammarParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ProjectGrammarParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ProjectGrammarParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ProjectGrammarParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ProjectGrammarParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(ProjectGrammarParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ProjectGrammarParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(ProjectGrammarParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code identifier}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(ProjectGrammarParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by the {@code identifier}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(ProjectGrammarParser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parens}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterParens(ProjectGrammarParser.ParensContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parens}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitParens(ProjectGrammarParser.ParensContext ctx);
	/**
	 * Enter a parse tree produced by the {@code mod}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMod(ProjectGrammarParser.ModContext ctx);
	/**
	 * Exit a parse tree produced by the {@code mod}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMod(ProjectGrammarParser.ModContext ctx);
	/**
	 * Enter a parse tree produced by the {@code comparison}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterComparison(ProjectGrammarParser.ComparisonContext ctx);
	/**
	 * Exit a parse tree produced by the {@code comparison}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitComparison(ProjectGrammarParser.ComparisonContext ctx);
	/**
	 * Enter a parse tree produced by the {@code bool}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterBool(ProjectGrammarParser.BoolContext ctx);
	/**
	 * Exit a parse tree produced by the {@code bool}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitBool(ProjectGrammarParser.BoolContext ctx);
	/**
	 * Enter a parse tree produced by the {@code string}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterString(ProjectGrammarParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by the {@code string}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitString(ProjectGrammarParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assignment}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(ProjectGrammarParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assignment}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(ProjectGrammarParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by the {@code addSub}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAddSub(ProjectGrammarParser.AddSubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code addSub}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAddSub(ProjectGrammarParser.AddSubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code unary}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterUnary(ProjectGrammarParser.UnaryContext ctx);
	/**
	 * Exit a parse tree produced by the {@code unary}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitUnary(ProjectGrammarParser.UnaryContext ctx);
	/**
	 * Enter a parse tree produced by the {@code concat}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterConcat(ProjectGrammarParser.ConcatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code concat}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitConcat(ProjectGrammarParser.ConcatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code float}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterFloat(ProjectGrammarParser.FloatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code float}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitFloat(ProjectGrammarParser.FloatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code int}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterInt(ProjectGrammarParser.IntContext ctx);
	/**
	 * Exit a parse tree produced by the {@code int}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitInt(ProjectGrammarParser.IntContext ctx);
	/**
	 * Enter a parse tree produced by the {@code mulDiv}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMulDiv(ProjectGrammarParser.MulDivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code mulDiv}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMulDiv(ProjectGrammarParser.MulDivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code logical}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLogical(ProjectGrammarParser.LogicalContext ctx);
	/**
	 * Exit a parse tree produced by the {@code logical}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLogical(ProjectGrammarParser.LogicalContext ctx);
	/**
	 * Enter a parse tree produced by the {@code relational}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterRelational(ProjectGrammarParser.RelationalContext ctx);
	/**
	 * Exit a parse tree produced by the {@code relational}
	 * labeled alternative in {@link ProjectGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitRelational(ProjectGrammarParser.RelationalContext ctx);
	/**
	 * Enter a parse tree produced by {@link ProjectGrammarParser#declar}.
	 * @param ctx the parse tree
	 */
	void enterDeclar(ProjectGrammarParser.DeclarContext ctx);
	/**
	 * Exit a parse tree produced by {@link ProjectGrammarParser#declar}.
	 * @param ctx the parse tree
	 */
	void exitDeclar(ProjectGrammarParser.DeclarContext ctx);
	/**
	 * Enter a parse tree produced by {@link ProjectGrammarParser#writeExpr}.
	 * @param ctx the parse tree
	 */
	void enterWriteExpr(ProjectGrammarParser.WriteExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ProjectGrammarParser#writeExpr}.
	 * @param ctx the parse tree
	 */
	void exitWriteExpr(ProjectGrammarParser.WriteExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ProjectGrammarParser#readExpr}.
	 * @param ctx the parse tree
	 */
	void enterReadExpr(ProjectGrammarParser.ReadExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ProjectGrammarParser#readExpr}.
	 * @param ctx the parse tree
	 */
	void exitReadExpr(ProjectGrammarParser.ReadExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ProjectGrammarParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(ProjectGrammarParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ProjectGrammarParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(ProjectGrammarParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ProjectGrammarParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(ProjectGrammarParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ProjectGrammarParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(ProjectGrammarParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ProjectGrammarParser#doWhileStatement}.
	 * @param ctx the parse tree
	 */
	void enterDoWhileStatement(ProjectGrammarParser.DoWhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ProjectGrammarParser#doWhileStatement}.
	 * @param ctx the parse tree
	 */
	void exitDoWhileStatement(ProjectGrammarParser.DoWhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ProjectGrammarParser#blockStatement}.
	 * @param ctx the parse tree
	 */
	void enterBlockStatement(ProjectGrammarParser.BlockStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ProjectGrammarParser#blockStatement}.
	 * @param ctx the parse tree
	 */
	void exitBlockStatement(ProjectGrammarParser.BlockStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ProjectGrammarParser#primitiveType}.
	 * @param ctx the parse tree
	 */
	void enterPrimitiveType(ProjectGrammarParser.PrimitiveTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ProjectGrammarParser#primitiveType}.
	 * @param ctx the parse tree
	 */
	void exitPrimitiveType(ProjectGrammarParser.PrimitiveTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ProjectGrammarParser#relationalOp}.
	 * @param ctx the parse tree
	 */
	void enterRelationalOp(ProjectGrammarParser.RelationalOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link ProjectGrammarParser#relationalOp}.
	 * @param ctx the parse tree
	 */
	void exitRelationalOp(ProjectGrammarParser.RelationalOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link ProjectGrammarParser#comparisonOp}.
	 * @param ctx the parse tree
	 */
	void enterComparisonOp(ProjectGrammarParser.ComparisonOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link ProjectGrammarParser#comparisonOp}.
	 * @param ctx the parse tree
	 */
	void exitComparisonOp(ProjectGrammarParser.ComparisonOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link ProjectGrammarParser#logicalOp}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOp(ProjectGrammarParser.LogicalOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link ProjectGrammarParser#logicalOp}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOp(ProjectGrammarParser.LogicalOpContext ctx);
}