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
		T__9=10, T__10=11, INT_TYPE=12, FLOAT_TYPE=13, BOOL_TYPE=14, STRING_TYPE=15, 
		SEMI=16, COMMA=17, MUL=18, DIV=19, ADD=20, MOD=21, NOT=22, SUB=23, AND=24, 
		OR=25, EQUALS=26, NOT_EQUALS=27, LESS_THAN=28, LESS_THAN_OR_EQUAL=29, 
		GREATER_THAN=30, GREATER_THAN_OR_EQUAL=31, FLOAT=32, INT=33, BOOL=34, 
		STRING=35, ID=36, COMMENT=37, WS=38;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_expr = 2, RULE_declar = 3, 
		RULE_writeExpr = 4, RULE_readExpr = 5, RULE_ifStatement = 6, RULE_whileStatement = 7, 
		RULE_blockStatement = 8, RULE_primitiveType = 9, RULE_relationalOp = 10, 
		RULE_comparisonOp = 11, RULE_logicalOp = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "expr", "declar", "writeExpr", "readExpr", "ifStatement", 
			"whileStatement", "blockStatement", "primitiveType", "relationalOp", 
			"comparisonOp", "logicalOp"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'.'", "'('", "')'", "'='", "'write'", "'read'", "'if'", "'else'", 
			"'while'", "'{'", "'}'", "'int'", "'float'", "'bool'", "'string'", "';'", 
			"','", "'*'", "'/'", "'+'", "'%'", "'!'", "'-'", "'&&'", "'||'", "'=='", 
			"'!='", "'<'", "'<='", "'>'", "'>='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", "STRING_TYPE", "SEMI", "COMMA", 
			"MUL", "DIV", "ADD", "MOD", "NOT", "SUB", "AND", "OR", "EQUALS", "NOT_EQUALS", 
			"LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", "GREATER_THAN_OR_EQUAL", 
			"FLOAT", "INT", "BOOL", "STRING", "ID", "COMMENT", "WS"
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
		public TerminalNode EOF() { return getToken(ProjectGrammarParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(26);
				statement();
				}
				}
				setState(29); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 133156697828L) != 0) );
			setState(31);
			match(EOF);
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
		public DeclarContext declar() {
			return getRuleContext(DeclarContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(ProjectGrammarParser.SEMI, 0); }
		public WriteExprContext writeExpr() {
			return getRuleContext(WriteExprContext.class,0);
		}
		public ReadExprContext readExpr() {
			return getRuleContext(ReadExprContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public WhileStatementContext whileStatement() {
			return getRuleContext(WhileStatementContext.class,0);
		}
		public BlockStatementContext blockStatement() {
			return getRuleContext(BlockStatementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(49);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_TYPE:
			case FLOAT_TYPE:
			case BOOL_TYPE:
			case STRING_TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(33);
				declar();
				setState(34);
				match(SEMI);
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(36);
				writeExpr();
				setState(37);
				match(SEMI);
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 3);
				{
				setState(39);
				readExpr();
				setState(40);
				match(SEMI);
				}
				break;
			case T__1:
			case NOT:
			case SUB:
			case FLOAT:
			case INT:
			case BOOL:
			case STRING:
			case ID:
				enterOuterAlt(_localctx, 4);
				{
				setState(42);
				expr(0);
				setState(43);
				match(SEMI);
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 5);
				{
				setState(45);
				ifStatement();
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 6);
				{
				setState(46);
				whileStatement();
				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 7);
				{
				setState(47);
				blockStatement();
				}
				break;
			case SEMI:
				enterOuterAlt(_localctx, 8);
				{
				setState(48);
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
		public TerminalNode ID() { return getToken(ProjectGrammarParser.ID, 0); }
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
	public static class ComparisonContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ComparisonOpContext comparisonOp() {
			return getRuleContext(ComparisonOpContext.class,0);
		}
		public ComparisonContext(ExprContext ctx) { copyFrom(ctx); }
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
		public TerminalNode ID() { return getToken(ProjectGrammarParser.ID, 0); }
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
	public static class UnaryContext extends ExprContext {
		public Token op;
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SUB() { return getToken(ProjectGrammarParser.SUB, 0); }
		public TerminalNode NOT() { return getToken(ProjectGrammarParser.NOT, 0); }
		public UnaryContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ConcatContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
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
			setState(66);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				_localctx = new UnaryContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(52);
				((UnaryContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==NOT || _la==SUB) ) {
					((UnaryContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(53);
				expr(10);
				}
				break;
			case 2:
				{
				_localctx = new IntContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(54);
				match(INT);
				}
				break;
			case 3:
				{
				_localctx = new FloatContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(55);
				match(FLOAT);
				}
				break;
			case 4:
				{
				_localctx = new BoolContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(56);
				match(BOOL);
				}
				break;
			case 5:
				{
				_localctx = new StringContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(57);
				match(STRING);
				}
				break;
			case 6:
				{
				_localctx = new IdentifierContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(58);
				match(ID);
				}
				break;
			case 7:
				{
				_localctx = new ParensContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(59);
				match(T__1);
				setState(60);
				expr(0);
				setState(61);
				match(T__2);
				}
				break;
			case 8:
				{
				_localctx = new AssignmentContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(63);
				match(ID);
				setState(64);
				match(T__3);
				setState(65);
				expr(1);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(94);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(92);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
					case 1:
						{
						_localctx = new MulDivContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(68);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(69);
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
						setState(70);
						expr(16);
						}
						break;
					case 2:
						{
						_localctx = new AddSubContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(71);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(72);
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
						setState(73);
						expr(15);
						}
						break;
					case 3:
						{
						_localctx = new ModContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(74);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(75);
						((ModContext)_localctx).op = match(MOD);
						setState(76);
						expr(14);
						}
						break;
					case 4:
						{
						_localctx = new RelationalContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(77);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(78);
						relationalOp();
						setState(79);
						expr(13);
						}
						break;
					case 5:
						{
						_localctx = new ComparisonContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(81);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(82);
						comparisonOp();
						setState(83);
						expr(12);
						}
						break;
					case 6:
						{
						_localctx = new LogicalContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(85);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(86);
						logicalOp();
						setState(87);
						expr(10);
						}
						break;
					case 7:
						{
						_localctx = new ConcatContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(89);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(90);
						match(T__0);
						setState(91);
						expr(9);
						}
						break;
					}
					} 
				}
				setState(96);
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
	public static class DeclarContext extends ParserRuleContext {
		public PrimitiveTypeContext primitiveType() {
			return getRuleContext(PrimitiveTypeContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(ProjectGrammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(ProjectGrammarParser.ID, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(ProjectGrammarParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ProjectGrammarParser.COMMA, i);
		}
		public DeclarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declar; }
	}

	public final DeclarContext declar() throws RecognitionException {
		DeclarContext _localctx = new DeclarContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_declar);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			primitiveType();
			setState(98);
			match(ID);
			setState(103);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(99);
				match(COMMA);
				setState(100);
				match(ID);
				}
				}
				setState(105);
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
		enterRule(_localctx, 8, RULE_writeExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(T__4);
			setState(107);
			match(STRING);
			setState(112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(108);
				match(COMMA);
				setState(109);
				expr(0);
				}
				}
				setState(114);
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
		public List<TerminalNode> ID() { return getTokens(ProjectGrammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(ProjectGrammarParser.ID, i);
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
		enterRule(_localctx, 10, RULE_readExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			match(T__5);
			setState(116);
			match(ID);
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(117);
				match(COMMA);
				setState(118);
				match(ID);
				}
				}
				setState(123);
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
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_ifStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			match(T__6);
			setState(125);
			match(T__1);
			setState(126);
			expr(0);
			setState(127);
			match(T__2);
			setState(128);
			statement();
			setState(131);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				setState(129);
				match(T__7);
				setState(130);
				statement();
				}
				break;
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
	public static class WhileStatementContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
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
			setState(133);
			match(T__8);
			setState(134);
			match(T__1);
			setState(135);
			expr(0);
			setState(136);
			match(T__2);
			setState(137);
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
	public static class BlockStatementContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blockStatement; }
	}

	public final BlockStatementContext blockStatement() throws RecognitionException {
		BlockStatementContext _localctx = new BlockStatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_blockStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			match(T__9);
			setState(141); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(140);
				statement();
				}
				}
				setState(143); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 133156697828L) != 0) );
			setState(145);
			match(T__10);
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
		public TerminalNode INT_TYPE() { return getToken(ProjectGrammarParser.INT_TYPE, 0); }
		public TerminalNode FLOAT_TYPE() { return getToken(ProjectGrammarParser.FLOAT_TYPE, 0); }
		public TerminalNode BOOL_TYPE() { return getToken(ProjectGrammarParser.BOOL_TYPE, 0); }
		public TerminalNode STRING_TYPE() { return getToken(ProjectGrammarParser.STRING_TYPE, 0); }
		public PrimitiveTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitiveType; }
	}

	public final PrimitiveTypeContext primitiveType() throws RecognitionException {
		PrimitiveTypeContext _localctx = new PrimitiveTypeContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_primitiveType);
		try {
			setState(151);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(147);
				((PrimitiveTypeContext)_localctx).type = match(INT_TYPE);
				}
				break;
			case FLOAT_TYPE:
				enterOuterAlt(_localctx, 2);
				{
				setState(148);
				((PrimitiveTypeContext)_localctx).type = match(FLOAT_TYPE);
				}
				break;
			case BOOL_TYPE:
				enterOuterAlt(_localctx, 3);
				{
				setState(149);
				((PrimitiveTypeContext)_localctx).type = match(BOOL_TYPE);
				}
				break;
			case STRING_TYPE:
				enterOuterAlt(_localctx, 4);
				{
				setState(150);
				((PrimitiveTypeContext)_localctx).type = match(STRING_TYPE);
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
		enterRule(_localctx, 20, RULE_relationalOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4026531840L) != 0)) ) {
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
	public static class ComparisonOpContext extends ParserRuleContext {
		public TerminalNode EQUALS() { return getToken(ProjectGrammarParser.EQUALS, 0); }
		public TerminalNode NOT_EQUALS() { return getToken(ProjectGrammarParser.NOT_EQUALS, 0); }
		public ComparisonOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparisonOp; }
	}

	public final ComparisonOpContext comparisonOp() throws RecognitionException {
		ComparisonOpContext _localctx = new ComparisonOpContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_comparisonOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			_la = _input.LA(1);
			if ( !(_la==EQUALS || _la==NOT_EQUALS) ) {
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
		enterRule(_localctx, 24, RULE_logicalOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
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
			return precpred(_ctx, 15);
		case 1:
			return precpred(_ctx, 14);
		case 2:
			return precpred(_ctx, 13);
		case 3:
			return precpred(_ctx, 12);
		case 4:
			return precpred(_ctx, 11);
		case 5:
			return precpred(_ctx, 9);
		case 6:
			return precpred(_ctx, 8);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001&\u00a0\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0001\u0000\u0004\u0000\u001c\b\u0000\u000b\u0000\f\u0000\u001d"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0003\u00012\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002"+
		"C\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0005\u0002]\b\u0002\n\u0002\f\u0002`\t\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u0003f\b\u0003\n\u0003\f\u0003"+
		"i\t\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004"+
		"o\b\u0004\n\u0004\f\u0004r\t\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0005\u0005x\b\u0005\n\u0005\f\u0005{\t\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0003\u0006\u0084\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0004\b\u008e\b\b\u000b\b\f\b"+
		"\u008f\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0003\t\u0098\b"+
		"\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0000"+
		"\u0001\u0004\r\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0018\u0000\u0006\u0001\u0000\u0016\u0017\u0001\u0000\u0012\u0013\u0002"+
		"\u0000\u0014\u0014\u0017\u0017\u0001\u0000\u001c\u001f\u0001\u0000\u001a"+
		"\u001b\u0001\u0000\u0018\u0019\u00b0\u0000\u001b\u0001\u0000\u0000\u0000"+
		"\u00021\u0001\u0000\u0000\u0000\u0004B\u0001\u0000\u0000\u0000\u0006a"+
		"\u0001\u0000\u0000\u0000\bj\u0001\u0000\u0000\u0000\ns\u0001\u0000\u0000"+
		"\u0000\f|\u0001\u0000\u0000\u0000\u000e\u0085\u0001\u0000\u0000\u0000"+
		"\u0010\u008b\u0001\u0000\u0000\u0000\u0012\u0097\u0001\u0000\u0000\u0000"+
		"\u0014\u0099\u0001\u0000\u0000\u0000\u0016\u009b\u0001\u0000\u0000\u0000"+
		"\u0018\u009d\u0001\u0000\u0000\u0000\u001a\u001c\u0003\u0002\u0001\u0000"+
		"\u001b\u001a\u0001\u0000\u0000\u0000\u001c\u001d\u0001\u0000\u0000\u0000"+
		"\u001d\u001b\u0001\u0000\u0000\u0000\u001d\u001e\u0001\u0000\u0000\u0000"+
		"\u001e\u001f\u0001\u0000\u0000\u0000\u001f \u0005\u0000\u0000\u0001 \u0001"+
		"\u0001\u0000\u0000\u0000!\"\u0003\u0006\u0003\u0000\"#\u0005\u0010\u0000"+
		"\u0000#2\u0001\u0000\u0000\u0000$%\u0003\b\u0004\u0000%&\u0005\u0010\u0000"+
		"\u0000&2\u0001\u0000\u0000\u0000\'(\u0003\n\u0005\u0000()\u0005\u0010"+
		"\u0000\u0000)2\u0001\u0000\u0000\u0000*+\u0003\u0004\u0002\u0000+,\u0005"+
		"\u0010\u0000\u0000,2\u0001\u0000\u0000\u0000-2\u0003\f\u0006\u0000.2\u0003"+
		"\u000e\u0007\u0000/2\u0003\u0010\b\u000002\u0005\u0010\u0000\u00001!\u0001"+
		"\u0000\u0000\u00001$\u0001\u0000\u0000\u00001\'\u0001\u0000\u0000\u0000"+
		"1*\u0001\u0000\u0000\u00001-\u0001\u0000\u0000\u00001.\u0001\u0000\u0000"+
		"\u00001/\u0001\u0000\u0000\u000010\u0001\u0000\u0000\u00002\u0003\u0001"+
		"\u0000\u0000\u000034\u0006\u0002\uffff\uffff\u000045\u0007\u0000\u0000"+
		"\u00005C\u0003\u0004\u0002\n6C\u0005!\u0000\u00007C\u0005 \u0000\u0000"+
		"8C\u0005\"\u0000\u00009C\u0005#\u0000\u0000:C\u0005$\u0000\u0000;<\u0005"+
		"\u0002\u0000\u0000<=\u0003\u0004\u0002\u0000=>\u0005\u0003\u0000\u0000"+
		">C\u0001\u0000\u0000\u0000?@\u0005$\u0000\u0000@A\u0005\u0004\u0000\u0000"+
		"AC\u0003\u0004\u0002\u0001B3\u0001\u0000\u0000\u0000B6\u0001\u0000\u0000"+
		"\u0000B7\u0001\u0000\u0000\u0000B8\u0001\u0000\u0000\u0000B9\u0001\u0000"+
		"\u0000\u0000B:\u0001\u0000\u0000\u0000B;\u0001\u0000\u0000\u0000B?\u0001"+
		"\u0000\u0000\u0000C^\u0001\u0000\u0000\u0000DE\n\u000f\u0000\u0000EF\u0007"+
		"\u0001\u0000\u0000F]\u0003\u0004\u0002\u0010GH\n\u000e\u0000\u0000HI\u0007"+
		"\u0002\u0000\u0000I]\u0003\u0004\u0002\u000fJK\n\r\u0000\u0000KL\u0005"+
		"\u0015\u0000\u0000L]\u0003\u0004\u0002\u000eMN\n\f\u0000\u0000NO\u0003"+
		"\u0014\n\u0000OP\u0003\u0004\u0002\rP]\u0001\u0000\u0000\u0000QR\n\u000b"+
		"\u0000\u0000RS\u0003\u0016\u000b\u0000ST\u0003\u0004\u0002\fT]\u0001\u0000"+
		"\u0000\u0000UV\n\t\u0000\u0000VW\u0003\u0018\f\u0000WX\u0003\u0004\u0002"+
		"\nX]\u0001\u0000\u0000\u0000YZ\n\b\u0000\u0000Z[\u0005\u0001\u0000\u0000"+
		"[]\u0003\u0004\u0002\t\\D\u0001\u0000\u0000\u0000\\G\u0001\u0000\u0000"+
		"\u0000\\J\u0001\u0000\u0000\u0000\\M\u0001\u0000\u0000\u0000\\Q\u0001"+
		"\u0000\u0000\u0000\\U\u0001\u0000\u0000\u0000\\Y\u0001\u0000\u0000\u0000"+
		"]`\u0001\u0000\u0000\u0000^\\\u0001\u0000\u0000\u0000^_\u0001\u0000\u0000"+
		"\u0000_\u0005\u0001\u0000\u0000\u0000`^\u0001\u0000\u0000\u0000ab\u0003"+
		"\u0012\t\u0000bg\u0005$\u0000\u0000cd\u0005\u0011\u0000\u0000df\u0005"+
		"$\u0000\u0000ec\u0001\u0000\u0000\u0000fi\u0001\u0000\u0000\u0000ge\u0001"+
		"\u0000\u0000\u0000gh\u0001\u0000\u0000\u0000h\u0007\u0001\u0000\u0000"+
		"\u0000ig\u0001\u0000\u0000\u0000jk\u0005\u0005\u0000\u0000kp\u0005#\u0000"+
		"\u0000lm\u0005\u0011\u0000\u0000mo\u0003\u0004\u0002\u0000nl\u0001\u0000"+
		"\u0000\u0000or\u0001\u0000\u0000\u0000pn\u0001\u0000\u0000\u0000pq\u0001"+
		"\u0000\u0000\u0000q\t\u0001\u0000\u0000\u0000rp\u0001\u0000\u0000\u0000"+
		"st\u0005\u0006\u0000\u0000ty\u0005$\u0000\u0000uv\u0005\u0011\u0000\u0000"+
		"vx\u0005$\u0000\u0000wu\u0001\u0000\u0000\u0000x{\u0001\u0000\u0000\u0000"+
		"yw\u0001\u0000\u0000\u0000yz\u0001\u0000\u0000\u0000z\u000b\u0001\u0000"+
		"\u0000\u0000{y\u0001\u0000\u0000\u0000|}\u0005\u0007\u0000\u0000}~\u0005"+
		"\u0002\u0000\u0000~\u007f\u0003\u0004\u0002\u0000\u007f\u0080\u0005\u0003"+
		"\u0000\u0000\u0080\u0083\u0003\u0002\u0001\u0000\u0081\u0082\u0005\b\u0000"+
		"\u0000\u0082\u0084\u0003\u0002\u0001\u0000\u0083\u0081\u0001\u0000\u0000"+
		"\u0000\u0083\u0084\u0001\u0000\u0000\u0000\u0084\r\u0001\u0000\u0000\u0000"+
		"\u0085\u0086\u0005\t\u0000\u0000\u0086\u0087\u0005\u0002\u0000\u0000\u0087"+
		"\u0088\u0003\u0004\u0002\u0000\u0088\u0089\u0005\u0003\u0000\u0000\u0089"+
		"\u008a\u0003\u0002\u0001\u0000\u008a\u000f\u0001\u0000\u0000\u0000\u008b"+
		"\u008d\u0005\n\u0000\u0000\u008c\u008e\u0003\u0002\u0001\u0000\u008d\u008c"+
		"\u0001\u0000\u0000\u0000\u008e\u008f\u0001\u0000\u0000\u0000\u008f\u008d"+
		"\u0001\u0000\u0000\u0000\u008f\u0090\u0001\u0000\u0000\u0000\u0090\u0091"+
		"\u0001\u0000\u0000\u0000\u0091\u0092\u0005\u000b\u0000\u0000\u0092\u0011"+
		"\u0001\u0000\u0000\u0000\u0093\u0098\u0005\f\u0000\u0000\u0094\u0098\u0005"+
		"\r\u0000\u0000\u0095\u0098\u0005\u000e\u0000\u0000\u0096\u0098\u0005\u000f"+
		"\u0000\u0000\u0097\u0093\u0001\u0000\u0000\u0000\u0097\u0094\u0001\u0000"+
		"\u0000\u0000\u0097\u0095\u0001\u0000\u0000\u0000\u0097\u0096\u0001\u0000"+
		"\u0000\u0000\u0098\u0013\u0001\u0000\u0000\u0000\u0099\u009a\u0007\u0003"+
		"\u0000\u0000\u009a\u0015\u0001\u0000\u0000\u0000\u009b\u009c\u0007\u0004"+
		"\u0000\u0000\u009c\u0017\u0001\u0000\u0000\u0000\u009d\u009e\u0007\u0005"+
		"\u0000\u0000\u009e\u0019\u0001\u0000\u0000\u0000\u000b\u001d1B\\^gpy\u0083"+
		"\u008f\u0097";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}