grammar Prigogine;

@lexer::members {
COMMENTS = 1
SPACES = 2
}

filestart
    : (population | initglobal | create | runmodel)+ finalise*
    ;

population
    : 'population' ID '[' parameterlist variablelist statedef* ']'
    ;

initglobal
    : 'initglobal' ID expression
    ;

initvars
    : 'initvars' ID expression
    ;

initparams
    : 'initparams' ID expression
    ;

initstates
    : 'initstates' expression
    ;

create
    : 'create' ID INT createblock*
    ;

createblock
    : '[' createline* ']'
    ;

createline
     : (initvars | initstates | initparams)+
     ;

runmodel
    : 'runmodel' INT codeblock*
    ;

finalise
    : 'finalise' codeblock*
    ;

parameterlist
    : 'parameters' '[' parameter* ']'
    ;

variablelist
    : 'variables' '[' variable* ']'
    ;

listcomp
    : '[' expression 'for' ID 'in' expression ']'
    ;

listdef
    : '[' ( (ID | number | string) (',' (ID | number | string) )* )* ']'
    ;

tupledef
    : '(' ( (ID | number | string) (',' (ID | number | string) )* )* ')'
    ;

variable
    : ID
    ;

parameter
    : ID
    ;

timeindex
    : '[' 't' (('-'|'+') INT)* ']'
    | '[:]'
    ;

timevar
    : 't'
    ;

dictindex
    : ('[' string ']')
    ;

statedef
    : 'state' ID '[' transition* update* ']'
    ;

transition
    : 'transition' ID 'where' conditional codeblock*
    ;

update
    : 'update' ID (codeline | codeblock)
    ;

expression
     : assignment
     | expression '.' expression
     | expression POWER expression
     | expression op=(MUL|DIV) expression
     | expression op=(ADD|SUB) expression
     | expression op=PIPE expression
     | 'print' string
     | 'print' expression
     | listdef
     | tupledef
     | string
     | number
     | func
     | listcomp
     | ID
     | timevar
     | lparen expression rparen
     | 'return' ID
     ;

assignment
    : ID '=' expression
    ;

codeblock
    : '[' codeline* ']'
    ;

codeline
    : expression
    ;

string
    : STRING
    ;

conditional
    : expression op=('<'|'>'|'>='|'<='|'=='|'!=') expression
    ;

lparen
    : '('
    ;

rparen
    : ')'
    ;

func
    : ID '(' (expression (',' expression)*)* ')'
    ;

argument
    : number
    | ID
    | func
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
