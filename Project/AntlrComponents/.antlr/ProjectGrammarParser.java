// Generated from d:/Programy/3. ročník/6. semestr/PJP/Project/AntlrComponents/ProjectGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ProjectGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, INT_KEYWORD=12, FLOAT_KEYWORD=13, BOOL_KEYWORD=14, 
		STRING_KEYWORD=15, SEMI=16, COMMA=17, MUL=18, DIV=19, ADD=20, SUB=21, 
		MOD=22, AND=23, OR=24, NOT=25, EQUALS=26, NOT_EQUALS=27, LESS_THAN=28, 
		LESS_THAN_OR_EQUAL=29, GREATER_THAN=30, GREATER_THAN_OR_EQUAL=31, IDENTIFIER=32, 
		FLOAT=33, INT=34, BOOL=35, STRING=36, WS=37;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_expr = 2, RULE_writeExpr = 3, 
		RULE_readExpr = 4, RULE_statementList = 5, RULE_ifStatement = 6, RULE_whileStatement = 7, 
		RULE_primitiveType = 8, RULE_relationalOp = 9, RULE_logicalOp = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "expr", "writeExpr", "readExpr", "statementList", 
			"ifStatement", "whileStatement", "primitiveType", "relationalOp", "logicalOp"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'.'", "'('", "')'", "'='", "'write'", "'read'", "'if'", "'else'", 
			"'{'", "'}'", "'while'", "'int'", "'float'", "'bool'", "'string'", "';'", 
			"','", "'*'", "'/'", "'+'", "'-'", "'%'", "'&&'", "'||'", "'!'", "'=='", 
			"'!='", "'<'", "'<='", "'>'", "'>='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"INT_KEYWORD", "FLOAT_KEYWORD", "BOOL_KEYWORD", "STRING_KEYWORD", "SEMI", 
			"COMMA", "MUL", "DIV", "ADD", "SUB", "MOD", "AND", "OR", "NOT", "EQUALS", 
			"NOT_EQUALS", "LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", "GREATER_THAN_OR_EQUAL", 
			"IDENTIFIER", "FLOAT", "INT", "BOOL", "STRING", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ProjectGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ProjectGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ReadContext extends StatementContext {
		public ReadExprContext readExpr() {
			return getRuleContext(ReadExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(ProjectGrammarParser.SEMI, 0); }
		public ReadContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends StatementContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(ProjectGrammarParser.SEMI, 0); }
		public ExpressionContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class WhileContext extends StatementContext {
		public WhileStatementContext whileStatement() {
			return getRuleContext(WhileStatementContext.class,0);
		}
		public WhileContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationContext extends StatementContext {
		public PrimitiveTypeContext primitiveType() {
			return getRuleContext(PrimitiveTypeContext.class,0);
		}
		public List<TerminalNode> IDENTIFIER() { return getTokens(ProjectGrammarParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(ProjectGrammarParser.IDENTIFIER, i);
		}
		public TerminalNode SEMI() { return getToken(ProjectGrammarParser.SEMI, 0); }
		public List<TerminalNode> COMMA() { return getTokens(ProjectGrammarParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ProjectGrammarParser.COMMA, i);
		}
		public DeclarationContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class WriteContext extends StatementContext {
		public WriteExprContext writeExpr() {
			return getRuleContext(WriteExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(ProjectGrammarParser.SEMI, 0); }
		public WriteContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IfContext extends StatementContext {
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public IfContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class EmptyContext extends StatementContext {
		public TerminalNode SEMI() { return getToken(ProjectGrammarParser.SEMI, 0); }
		public EmptyContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		int _la;
		try {
			setState(47);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_KEYWORD:
			case FLOAT_KEYWORD:
			case BOOL_KEYWORD:
			case STRING_KEYWORD:
				_localctx = new DeclarationContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(24);
				primitiveType();
				setState(25);
				match(IDENTIFIER);
				setState(30);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(26);
					match(COMMA);
					setState(27);
					match(IDENTIFIER);
					}
					}
					setState(32);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(33);
				match(SEMI);
				}
				break;
			case T__4:
				_localctx = new WriteContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(35);
				writeExpr();
				setState(36);
				match(SEMI);
				}
				break;
			case T__5:
				_localctx = new ReadContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(38);
				readExpr();
				setState(39);
				match(SEMI);
				}
				break;
			case T__1:
			case NOT:
			case IDENTIFIER:
			case FLOAT:
			case INT:
			case BOOL:
			case STRING:
				_localctx = new ExpressionContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(41);
				expr(0);
				setState(42);
				match(SEMI);
				}
				break;
			case T__6:
				_localctx = new IfContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(44);
				ifStatement();
				}
				break;
			case T__10:
				_localctx = new WhileContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(45);
				whileStatement();
				}
				break;
			case SEMI:
				_localctx = new EmptyContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(46);
				match(SEMI);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IdentifierContext extends ExprContext {
		public TerminalNode IDENTIFIER() { return getToken(ProjectGrammarParser.IDENTIFIER, 0); }
		public IdentifierContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParensContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ParensContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ModContext extends ExprContext {
		public Token op;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MOD() { return getToken(ProjectGrammarParser.MOD, 0); }
		public ModContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BoolContext extends ExprContext {
		public TerminalNode BOOL() { return getToken(ProjectGrammarParser.BOOL, 0); }
		public BoolContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StringContext extends ExprContext {
		public TerminalNode STRING() { return getToken(ProjectGrammarParser.STRING, 0); }
		public StringContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ExprContext {
		public TerminalNode IDENTIFIER() { return getToken(ProjectGrammarParser.IDENTIFIER, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignmentContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AddSubContext extends ExprContext {
		public Token op;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ADD() { return getToken(ProjectGrammarParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(ProjectGrammarParser.SUB, 0); }
		public AddSubContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ConcatContext extends ExprContext {
		public List<TerminalNode> STRING() { return getTokens(ProjectGrammarParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(ProjectGrammarParser.STRING, i);
		}
		public ConcatContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FloatContext extends ExprContext {
		public TerminalNode FLOAT() { return getToken(ProjectGrammarParser.FLOAT, 0); }
		public FloatContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntContext extends ExprContext {
		public TerminalNode INT() { return getToken(ProjectGrammarParser.INT, 0); }
		public IntContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MulDivContext extends ExprContext {
		public Token op;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MUL() { return getToken(ProjectGrammarParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(ProjectGrammarParser.DIV, 0); }
		public MulDivContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LogicalContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public LogicalOpContext logicalOp() {
			return getRuleContext(LogicalOpContext.class,0);
		}
		public LogicalContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NotContext extends ExprContext {
		public TerminalNode NOT() { return getToken(ProjectGrammarParser.NOT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public NotContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RelationalContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public RelationalOpContext relationalOp() {
			return getRuleContext(RelationalOpContext.class,0);
		}
		public RelationalContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				_localctx = new NotContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(50);
				match(NOT);
				setState(51);
				expr(10);
				}
				break;
			case 2:
				{
				_localctx = new ConcatContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(52);
				match(STRING);
				setState(53);
				match(T__0);
				setState(54);
				match(STRING);
				}
				break;
			case 3:
				{
				_localctx = new IntContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(55);
				match(INT);
				}
				break;
			case 4:
				{
				_localctx = new FloatContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(56);
				match(FLOAT);
				}
				break;
			case 5:
				{
				_localctx = new BoolContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(57);
				match(BOOL);
				}
				break;
			case 6:
				{
				_localctx = new StringContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(58);
				match(STRING);
				}
				break;
			case 7:
				{
				_localctx = new IdentifierContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(59);
				match(IDENTIFIER);
				}
				break;
			case 8:
				{
				_localctx = new ParensContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(60);
				match(T__1);
				setState(61);
				expr(0);
				setState(62);
				match(T__2);
				}
				break;
			case 9:
				{
				_localctx = new AssignmentContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(64);
				match(IDENTIFIER);
				setState(65);
				match(T__3);
				setState(66);
				expr(1);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(88);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(86);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
					case 1:
						{
						_localctx = new MulDivContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(69);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(70);
						((MulDivContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
							((MulDivContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(71);
						expr(15);
						}
						break;
					case 2:
						{
						_localctx = new AddSubContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(72);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(73);
						((AddSubContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
							((AddSubContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(74);
						expr(14);
						}
						break;
					case 3:
						{
						_localctx = new ModContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(75);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(76);
						((ModContext)_localctx).op = match(MOD);
						setState(77);
						expr(13);
						}
						break;
					case 4:
						{
						_localctx = new RelationalContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(78);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(79);
						relationalOp();
						setState(80);
						expr(12);
						}
						break;
					case 5:
						{
						_localctx = new LogicalContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(82);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(83);
						logicalOp();
						setState(84);
						expr(10);
						}
						break;
					}
					} 
				}
				setState(90);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WriteExprContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(ProjectGrammarParser.STRING, 0); }
		public List<TerminalNode> COMMA() { return getTokens(ProjectGrammarParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ProjectGrammarParser.COMMA, i);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public WriteExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_writeExpr; }
	}

	public final WriteExprContext writeExpr() throws RecognitionException {
		WriteExprContext _localctx = new WriteExprContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_writeExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(T__4);
			setState(92);
			match(STRING);
			setState(97);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(93);
				match(COMMA);
				setState(94);
				expr(0);
				}
				}
				setState(99);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReadExprContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(ProjectGrammarParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(ProjectGrammarParser.IDENTIFIER, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(ProjectGrammarParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ProjectGrammarParser.COMMA, i);
		}
		public ReadExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_readExpr; }
	}

	public final ReadExprContext readExpr() throws RecognitionException {
		ReadExprContext _localctx = new ReadExprContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_readExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			match(T__5);
			setState(101);
			match(IDENTIFIER);
			setState(106);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(102);
				match(COMMA);
				setState(103);
				match(IDENTIFIER);
				}
				}
				setState(108);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementListContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public StatementListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statementList; }
	}

	public final StatementListContext statementList() throws RecognitionException {
		StatementListContext _localctx = new StatementListContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_statementList);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(110); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(109);
					statement();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(112); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStatementContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode SEMI() { return getToken(ProjectGrammarParser.SEMI, 0); }
		public List<StatementListContext> statementList() {
			return getRuleContexts(StatementListContext.class);
		}
		public StatementListContext statementList(int i) {
			return getRuleContext(StatementListContext.class,i);
		}
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_ifStatement);
		try {
			setState(137);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(114);
				match(T__6);
				setState(115);
				match(T__1);
				setState(116);
				expr(0);
				setState(117);
				match(T__2);
				setState(118);
				statement();
				setState(123);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
				case 1:
					{
					setState(119);
					match(T__7);
					setState(120);
					statement();
					setState(121);
					match(SEMI);
					}
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(125);
				match(T__6);
				setState(126);
				match(T__1);
				setState(127);
				expr(0);
				setState(128);
				match(T__2);
				setState(129);
				match(T__8);
				setState(130);
				statementList();
				setState(131);
				match(T__9);
				setState(132);
				match(T__7);
				setState(133);
				match(T__8);
				setState(134);
				statementList();
				setState(135);
				match(T__9);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStatementContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public StatementListContext statementList() {
			return getRuleContext(StatementListContext.class,0);
		}
		public WhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStatement; }
	}

	public final WhileStatementContext whileStatement() throws RecognitionException {
		WhileStatementContext _localctx = new WhileStatementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_whileStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			match(T__10);
			setState(140);
			match(T__1);
			setState(141);
			expr(0);
			setState(142);
			match(T__2);
			setState(143);
			statementList();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimitiveTypeContext extends ParserRuleContext {
		public Token type;
		public TerminalNode INT_KEYWORD() { return getToken(ProjectGrammarParser.INT_KEYWORD, 0); }
		public TerminalNode FLOAT_KEYWORD() { return getToken(ProjectGrammarParser.FLOAT_KEYWORD, 0); }
		public TerminalNode BOOL_KEYWORD() { return getToken(ProjectGrammarParser.BOOL_KEYWORD, 0); }
		public TerminalNode STRING_KEYWORD() { return getToken(ProjectGrammarParser.STRING_KEYWORD, 0); }
		public PrimitiveTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitiveType; }
	}

	public final PrimitiveTypeContext primitiveType() throws RecognitionException {
		PrimitiveTypeContext _localctx = new PrimitiveTypeContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_primitiveType);
		try {
			setState(149);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_KEYWORD:
				enterOuterAlt(_localctx, 1);
				{
				setState(145);
				((PrimitiveTypeContext)_localctx).type = match(INT_KEYWORD);
				}
				break;
			case FLOAT_KEYWORD:
				enterOuterAlt(_localctx, 2);
				{
				setState(146);
				((PrimitiveTypeContext)_localctx).type = match(FLOAT_KEYWORD);
				}
				break;
			case BOOL_KEYWORD:
				enterOuterAlt(_localctx, 3);
				{
				setState(147);
				((PrimitiveTypeContext)_localctx).type = match(BOOL_KEYWORD);
				}
				break;
			case STRING_KEYWORD:
				enterOuterAlt(_localctx, 4);
				{
				setState(148);
				((PrimitiveTypeContext)_localctx).type = match(STRING_KEYWORD);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RelationalOpContext extends ParserRuleContext {
		public TerminalNode EQUALS() { return getToken(ProjectGrammarParser.EQUALS, 0); }
		public TerminalNode NOT_EQUALS() { return getToken(ProjectGrammarParser.NOT_EQUALS, 0); }
		public TerminalNode LESS_THAN() { return getToken(ProjectGrammarParser.LESS_THAN, 0); }
		public TerminalNode LESS_THAN_OR_EQUAL() { return getToken(ProjectGrammarParser.LESS_THAN_OR_EQUAL, 0); }
		public TerminalNode GREATER_THAN() { return getToken(ProjectGrammarParser.GREATER_THAN, 0); }
		public TerminalNode GREATER_THAN_OR_EQUAL() { return getToken(ProjectGrammarParser.GREATER_THAN_OR_EQUAL, 0); }
		public RelationalOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relationalOp; }
	}

	public final RelationalOpContext relationalOp() throws RecognitionException {
		RelationalOpContext _localctx = new RelationalOpContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_relationalOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4227858432L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicalOpContext extends ParserRuleContext {
		public TerminalNode AND() { return getToken(ProjectGrammarParser.AND, 0); }
		public TerminalNode OR() { return getToken(ProjectGrammarParser.OR, 0); }
		public LogicalOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalOp; }
	}

	public final LogicalOpContext logicalOp() throws RecognitionException {
		LogicalOpContext _localctx = new LogicalOpContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_logicalOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			_la = _input.LA(1);
			if ( !(_la==AND || _la==OR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 14);
		case 1:
			return precpred(_ctx, 13);
		case 2:
			return precpred(_ctx, 12);
		case 3:
			return precpred(_ctx, 11);
		case 4:
			return precpred(_ctx, 9);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001%\u009c\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u0001\u001d\b\u0001\n"+
		"\u0001\f\u0001 \t\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u00010\b\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u0002D\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0005\u0002W\b\u0002\n\u0002\f\u0002Z\t\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u0003`\b\u0003\n\u0003\f\u0003"+
		"c\t\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004"+
		"i\b\u0004\n\u0004\f\u0004l\t\u0004\u0001\u0005\u0004\u0005o\b\u0005\u000b"+
		"\u0005\f\u0005p\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006|\b"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0003\u0006\u008a\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b"+
		"\u0096\b\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0000\u0001\u0004\u000b"+
		"\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0000\u0004\u0001"+
		"\u0000\u0012\u0013\u0001\u0000\u0014\u0015\u0001\u0000\u001a\u001f\u0001"+
		"\u0000\u0017\u0018\u00ac\u0000\u0016\u0001\u0000\u0000\u0000\u0002/\u0001"+
		"\u0000\u0000\u0000\u0004C\u0001\u0000\u0000\u0000\u0006[\u0001\u0000\u0000"+
		"\u0000\bd\u0001\u0000\u0000\u0000\nn\u0001\u0000\u0000\u0000\f\u0089\u0001"+
		"\u0000\u0000\u0000\u000e\u008b\u0001\u0000\u0000\u0000\u0010\u0095\u0001"+
		"\u0000\u0000\u0000\u0012\u0097\u0001\u0000\u0000\u0000\u0014\u0099\u0001"+
		"\u0000\u0000\u0000\u0016\u0017\u0003\u0002\u0001\u0000\u0017\u0001\u0001"+
		"\u0000\u0000\u0000\u0018\u0019\u0003\u0010\b\u0000\u0019\u001e\u0005 "+
		"\u0000\u0000\u001a\u001b\u0005\u0011\u0000\u0000\u001b\u001d\u0005 \u0000"+
		"\u0000\u001c\u001a\u0001\u0000\u0000\u0000\u001d \u0001\u0000\u0000\u0000"+
		"\u001e\u001c\u0001\u0000\u0000\u0000\u001e\u001f\u0001\u0000\u0000\u0000"+
		"\u001f!\u0001\u0000\u0000\u0000 \u001e\u0001\u0000\u0000\u0000!\"\u0005"+
		"\u0010\u0000\u0000\"0\u0001\u0000\u0000\u0000#$\u0003\u0006\u0003\u0000"+
		"$%\u0005\u0010\u0000\u0000%0\u0001\u0000\u0000\u0000&\'\u0003\b\u0004"+
		"\u0000\'(\u0005\u0010\u0000\u0000(0\u0001\u0000\u0000\u0000)*\u0003\u0004"+
		"\u0002\u0000*+\u0005\u0010\u0000\u0000+0\u0001\u0000\u0000\u0000,0\u0003"+
		"\f\u0006\u0000-0\u0003\u000e\u0007\u0000.0\u0005\u0010\u0000\u0000/\u0018"+
		"\u0001\u0000\u0000\u0000/#\u0001\u0000\u0000\u0000/&\u0001\u0000\u0000"+
		"\u0000/)\u0001\u0000\u0000\u0000/,\u0001\u0000\u0000\u0000/-\u0001\u0000"+
		"\u0000\u0000/.\u0001\u0000\u0000\u00000\u0003\u0001\u0000\u0000\u0000"+
		"12\u0006\u0002\uffff\uffff\u000023\u0005\u0019\u0000\u00003D\u0003\u0004"+
		"\u0002\n45\u0005$\u0000\u000056\u0005\u0001\u0000\u00006D\u0005$\u0000"+
		"\u00007D\u0005\"\u0000\u00008D\u0005!\u0000\u00009D\u0005#\u0000\u0000"+
		":D\u0005$\u0000\u0000;D\u0005 \u0000\u0000<=\u0005\u0002\u0000\u0000="+
		">\u0003\u0004\u0002\u0000>?\u0005\u0003\u0000\u0000?D\u0001\u0000\u0000"+
		"\u0000@A\u0005 \u0000\u0000AB\u0005\u0004\u0000\u0000BD\u0003\u0004\u0002"+
		"\u0001C1\u0001\u0000\u0000\u0000C4\u0001\u0000\u0000\u0000C7\u0001\u0000"+
		"\u0000\u0000C8\u0001\u0000\u0000\u0000C9\u0001\u0000\u0000\u0000C:\u0001"+
		"\u0000\u0000\u0000C;\u0001\u0000\u0000\u0000C<\u0001\u0000\u0000\u0000"+
		"C@\u0001\u0000\u0000\u0000DX\u0001\u0000\u0000\u0000EF\n\u000e\u0000\u0000"+
		"FG\u0007\u0000\u0000\u0000GW\u0003\u0004\u0002\u000fHI\n\r\u0000\u0000"+
		"IJ\u0007\u0001\u0000\u0000JW\u0003\u0004\u0002\u000eKL\n\f\u0000\u0000"+
		"LM\u0005\u0016\u0000\u0000MW\u0003\u0004\u0002\rNO\n\u000b\u0000\u0000"+
		"OP\u0003\u0012\t\u0000PQ\u0003\u0004\u0002\fQW\u0001\u0000\u0000\u0000"+
		"RS\n\t\u0000\u0000ST\u0003\u0014\n\u0000TU\u0003\u0004\u0002\nUW\u0001"+
		"\u0000\u0000\u0000VE\u0001\u0000\u0000\u0000VH\u0001\u0000\u0000\u0000"+
		"VK\u0001\u0000\u0000\u0000VN\u0001\u0000\u0000\u0000VR\u0001\u0000\u0000"+
		"\u0000WZ\u0001\u0000\u0000\u0000XV\u0001\u0000\u0000\u0000XY\u0001\u0000"+
		"\u0000\u0000Y\u0005\u0001\u0000\u0000\u0000ZX\u0001\u0000\u0000\u0000"+
		"[\\\u0005\u0005\u0000\u0000\\a\u0005$\u0000\u0000]^\u0005\u0011\u0000"+
		"\u0000^`\u0003\u0004\u0002\u0000_]\u0001\u0000\u0000\u0000`c\u0001\u0000"+
		"\u0000\u0000a_\u0001\u0000\u0000\u0000ab\u0001\u0000\u0000\u0000b\u0007"+
		"\u0001\u0000\u0000\u0000ca\u0001\u0000\u0000\u0000de\u0005\u0006\u0000"+
		"\u0000ej\u0005 \u0000\u0000fg\u0005\u0011\u0000\u0000gi\u0005 \u0000\u0000"+
		"hf\u0001\u0000\u0000\u0000il\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000"+
		"\u0000jk\u0001\u0000\u0000\u0000k\t\u0001\u0000\u0000\u0000lj\u0001\u0000"+
		"\u0000\u0000mo\u0003\u0002\u0001\u0000nm\u0001\u0000\u0000\u0000op\u0001"+
		"\u0000\u0000\u0000pn\u0001\u0000\u0000\u0000pq\u0001\u0000\u0000\u0000"+
		"q\u000b\u0001\u0000\u0000\u0000rs\u0005\u0007\u0000\u0000st\u0005\u0002"+
		"\u0000\u0000tu\u0003\u0004\u0002\u0000uv\u0005\u0003\u0000\u0000v{\u0003"+
		"\u0002\u0001\u0000wx\u0005\b\u0000\u0000xy\u0003\u0002\u0001\u0000yz\u0005"+
		"\u0010\u0000\u0000z|\u0001\u0000\u0000\u0000{w\u0001\u0000\u0000\u0000"+
		"{|\u0001\u0000\u0000\u0000|\u008a\u0001\u0000\u0000\u0000}~\u0005\u0007"+
		"\u0000\u0000~\u007f\u0005\u0002\u0000\u0000\u007f\u0080\u0003\u0004\u0002"+
		"\u0000\u0080\u0081\u0005\u0003\u0000\u0000\u0081\u0082\u0005\t\u0000\u0000"+
		"\u0082\u0083\u0003\n\u0005\u0000\u0083\u0084\u0005\n\u0000\u0000\u0084"+
		"\u0085\u0005\b\u0000\u0000\u0085\u0086\u0005\t\u0000\u0000\u0086\u0087"+
		"\u0003\n\u0005\u0000\u0087\u0088\u0005\n\u0000\u0000\u0088\u008a\u0001"+
		"\u0000\u0000\u0000\u0089r\u0001\u0000\u0000\u0000\u0089}\u0001\u0000\u0000"+
		"\u0000\u008a\r\u0001\u0000\u0000\u0000\u008b\u008c\u0005\u000b\u0000\u0000"+
		"\u008c\u008d\u0005\u0002\u0000\u0000\u008d\u008e\u0003\u0004\u0002\u0000"+
		"\u008e\u008f\u0005\u0003\u0000\u0000\u008f\u0090\u0003\n\u0005\u0000\u0090"+
		"\u000f\u0001\u0000\u0000\u0000\u0091\u0096\u0005\f\u0000\u0000\u0092\u0096"+
		"\u0005\r\u0000\u0000\u0093\u0096\u0005\u000e\u0000\u0000\u0094\u0096\u0005"+
		"\u000f\u0000\u0000\u0095\u0091\u0001\u0000\u0000\u0000\u0095\u0092\u0001"+
		"\u0000\u0000\u0000\u0095\u0093\u0001\u0000\u0000\u0000\u0095\u0094\u0001"+
		"\u0000\u0000\u0000\u0096\u0011\u0001\u0000\u0000\u0000\u0097\u0098\u0007"+
		"\u0002\u0000\u0000\u0098\u0013\u0001\u0000\u0000\u0000\u0099\u009a\u0007"+
		"\u0003\u0000\u0000\u009a\u0015\u0001\u0000\u0000\u0000\u000b\u001e/CV"+
		"Xajp{\u0089\u0095";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}