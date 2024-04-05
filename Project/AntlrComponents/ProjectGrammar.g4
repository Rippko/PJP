grammar ProjectGrammar;

/** The start rule; begin parsing here. */
program: statement;

statement
    : primitiveType IDENTIFIER (',' IDENTIFIER)* SEMI # declaration
    | writeExpr SEMI                                  # write
    | readExpr SEMI                                   # read
    | expr SEMI                                       # expression
    | ifStatement                                     # if
    | whileStatement                                  # while
    | SEMI                                            # empty
    ;

expr: expr op=(MUL|DIV) expr                # mulDiv
    | expr op=(ADD|SUB) expr                # addSub
    | expr op=MOD expr                      # mod
    | expr relationalOp expr                # relational
    | NOT expr                              # not
    | expr logicalOp expr                   # logical
    | STRING '.' STRING                     # concat
    | INT                                   # int
    | FLOAT                                 # float
    | BOOL                                  # bool
    | STRING                                # string
    | IDENTIFIER                            # identifier
    | '(' expr ')'                          # parens
    | <assoc=right> IDENTIFIER '=' expr     # assignment
    ;

writeExpr: 'write' STRING (',' expr)*
    ;

readExpr: 'read' IDENTIFIER (',' IDENTIFIER)*
    ;

statementList: statement+
    ;

ifStatement
    : 'if' '(' expr ')' statement ( 'else' statement SEMI )?
    | 'if' '(' expr ')' '{' statementList '}' 'else' '{' statementList '}'
    ;

whileStatement
    : 'while' '(' expr ')' statementList
    ;

primitiveType
    : type=INT_KEYWORD
    | type=FLOAT_KEYWORD
    | type=BOOL_KEYWORD
    | type=STRING_KEYWORD
    ;

relationalOp
    : EQUALS
    | NOT_EQUALS
    | LESS_THAN
    | LESS_THAN_OR_EQUAL
    | GREATER_THAN
    | GREATER_THAN_OR_EQUAL
    ;

logicalOp
    : AND
    | OR
    ;


INT_KEYWORD : 'int';
FLOAT_KEYWORD : 'float';
BOOL_KEYWORD : 'bool';
STRING_KEYWORD : 'string';

SEMI:  ';';
COMMA: ',';
MUL : '*' ; 
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
MOD : '%' ;

AND : '&&';
OR : '||';
NOT : '!' ;

EQUALS : '==';
NOT_EQUALS : '!=';
LESS_THAN : '<';
LESS_THAN_OR_EQUAL : '<=';
GREATER_THAN : '>';
GREATER_THAN_OR_EQUAL : '>=';


IDENTIFIER : [a-zA-Z]+ ; 
FLOAT : '-'? [0-9]+'.'[0-9]+ ;
INT : '-'? [0-9]+ ;
BOOL : 'true' | 'false' ;
STRING: '"' (~["])* '"' ;
WS : [ \t\r\n]+ -> skip ; // toss out whitespace