grammar ProjectGrammar;

/** The start rule; begin parsing here. */
program: statement+ EOF;

statement
    : declar SEMI
    | writeExpr SEMI
    | readExpr SEMI
    | expression
    | ifStatement
    | whileStatement
    | doWhileStatement
    | blockStatement
    | SEMI
    ;

expr: expr op=(MUL|DIV) expr                # mulDiv
    | expr op=(ADD|SUB) expr                # addSub
    | expr op=MOD expr                      # mod
    | expr op=AND expr                      # and
    | expr op=OR expr                       # or
    | expr op=relationalOp expr             # relational
    | expr op=comparisonOp expr             # comparison
    | op=(SUB|NOT) expr                     # unary
    | expr '.' expr                         # concat
    | INT                                   # int
    | FLOAT                                 # float
    | BOOL                                  # bool
    | STRING                                # string
    | ID                                    # identifier
    | '(' expr ')'                          # parens
    | <assoc=right> ID '=' expr             # assignment
    ;

declar: 
    primitiveType ID (',' ID)*
    ;

writeExpr: 'write' expr (',' expr)*
    ;

readExpr: 'read' expr (',' expr)*
    ;

expression
    : expr SEMI
    ;

ifStatement
    : 'if' '(' expr rpar statement (elseStatement)?
    ;

elseStatement
    : 'else' statement
    ;

whileStatement
    : 'while' '(' expr rpar statement
    ;

doWhileStatement
    : 'do' statement 'while' '(' expr rpar SEMI
    ;

rpar 
    : ')'
    ;

blockStatement
    : '{' statement+ '}'
    ;

primitiveType
    : type=INT_TYPE
    | type=FLOAT_TYPE
    | type=BOOL_TYPE
    | type=STRING_TYPE
    ;

relationalOp
    : LESS_THAN
    | LESS_THAN_OR_EQUAL
    | GREATER_THAN
    | GREATER_THAN_OR_EQUAL
    ;

comparisonOp
    : EQUALS
    | NOT_EQUALS
    ;

INT_TYPE : 'int';
FLOAT_TYPE : 'float';
BOOL_TYPE : 'bool';
STRING_TYPE : 'string';

SEMI:  ';';
COMMA: ',';
MUL : '*' ; 
DIV : '/' ;
ADD : '+' ;
MOD : '%' ;

NOT : '!' ;
SUB : '-' ;

AND : '&&';
OR : '||';



EQUALS : '==';
NOT_EQUALS : '!=';
LESS_THAN : '<';
LESS_THAN_OR_EQUAL : '<=';
GREATER_THAN : '>';
GREATER_THAN_OR_EQUAL : '>=';

FLOAT : [0-9]+'.'[0-9]+ ;
INT : '0' | [1-9][0-9]* ;
BOOL : 'true' | 'false' ;
STRING: '"' (~["\\])* '"' ;
ID : [a-zA-Z_][a-zA-Z0-9_]* ; 

COMMENT : '//' ~[\r\n]* -> skip ;
WS : [ \t\r\n]+ -> skip ; // toss out whitespace