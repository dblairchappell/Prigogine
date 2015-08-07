grammar Prigogine;

@lexer::members {
COMMENTS = 1
SPACES = 2
}

filestart
    : model+ simulation*
    ;

model
    : 'model' ID '[' (msgboardlist* variablelist equationlist population+) ']'
    ;

simulation
    : 'simulation' '[' codeinsert ']'
    ;

codeinsert
    //: (ESC|.)*?
    : ~('\n'|'\r')*?
    ;

equationlist
    : 'equations' '[' (elementwiseEquation | mapEquation | nIndexedEquation)* ']'
    ;

elementwiseEquation
    : ID '[t+1]' '=' expression (',' 'where' conditional)*
    | ID ('.' ID)* '[t+1]' '=' expression (',' 'where' conditional)*
    ;

mapEquation
    : ID '[t+1]' '[:]''=' expression (',' 'where' conditional)*
    | ID ('.' ID)* '[t+1]' '[:]' '=' expression (',' 'where' conditional)*
    ;

nIndexedEquation
    : ID '[t+1]' '[n]''=' expression (',' 'where' conditional)*
    | ID ('.' ID)* '[t+1]' '[n]' '=' expression (',' 'where' conditional)*
    ;

assignment
    : ID (('.' ID) | timeindex)* '=' expression
    ;

population
    : 'population' ID '[' parameterlist* variablelist equationlist ']'
    ;

parameterlist
    : 'parameters' '[' parameter* ']'
    ;

variablelist
    : 'variables' '[' variable* ']'
    ;

msgboardlist
    : 'messageboards' '[' msgboarddef* ']'
    ;

msgboarddef
    : ID numbertuple
    ;

listcomp
    : '[' expression 'for' ID 'in' expression ']'
    ;

listdef
    : '[' ( (ID | number | string) (',' (ID | number | string) )* )* ']'
    | '[' listdef ']'
    ;

tupledef
    : '(' ( (ID | number | string) (',' (ID | number | string) )* )* ')'
    ;

numbertuple
    : '(' ( number (',' number )* )* ')'
    ;

variable
    : ID
    ;

indexedvariable
    : ID timeindex
    ;

parameter
    : ID
    ;

timeindex
    : ('[' timevar (SUB INT)* ']' | '[:]' | '[n]')+
    ;

timevar
    : 't'
    | INT
    ;

dictindex
    : ('[' string ']')
    ;

expression
     : assignment
     | expression '.' expression
     | expression POWER expression
     | expression op=(MUL|DIV) expression
     | expression op=(ADD|SUB) expression
     | expression op=PIPE expression
     | pyforloop
     | 'print' string
     | 'print' string ','
     | 'print' expression
     | listdef
     | tupledef
     | string
     | number
     | func
     | listcomp
     | ID
     | ':'
     | indexedvariable
     | timevar
     | lparen expression rparen
     | 'return' ID
     ;

codeblock
    : '[' (codeline | pyforloop)* ']'
    ;

codeline
    : expression
    ;

pyforloop
    : 'for' (ID | timevar) 'in' (ID | func) ':'
    ;

string
    : STRING
    ;

conditional
    : lparen* expression op=('<'|'>'|'>='|'<='|'=='|'!=') expression rparen* (('&' | '|') conditional)*
    ;

lparen
    : '('
    ;

rparen
    : ')'
    ;

func
    : ID '(' lparen* (expression (',' expression)*)* rparen* ')'
    ;

number
    : INT
    | FLOAT
    ;

LineComment
    : '#' ~[\r\n]* -> channel(1)
    ;

NEWLINE
    : [\r\n]
    ;

ML_COMMENT
    :  '##' .*? '##' -> channel(1)
    ;

INT
    : [0-9]+
    ;

FLOAT
    : INT* '.' INT*
    ;

ID
    : [_a-zA-Z0-9]+
    ;
WS 
    : [\t\r\n]+ -> skip
    ;

MUL :   '*' ;
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
PIPE : '|' ;
POWER : '^' ;

STRING
    : '"' (ESC|.)*? '"'
    | '\'' (ESC|.)*? '\''
    ;

ESC
    : '\\"' | '\\\\'
    ;

SPACE: [ ]-> channel(2);
