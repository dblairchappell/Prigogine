grammar Prigogine;

@lexer::members {
COMMENTS = 1
SPACES = 2
}

filestart
    : population+ createpopulation*
    ;

population
    : 'population' ID attributelist statedef* 'end'
    ;

createpopulation
    : 'create' ID INT startstate initvar* 'end'
    ;

startstate
    : 'startstate' ID
    ;

//runmodel
//    : 'runmodel' INT ('[' expression* ']')*
//    ;

initvar
    : 'init' attrsget (codeline | codeblock)
    ;

attributelist
    : 'attributes' attribute* 'end'
    ;

listcomp
    : '[' expression 'for' ID 'in' ID ']'
    ;

attribute
    : ID
    ;

attrsget
    : ID timeindex
    ;

timeindex
    : '[' 't' (('-'|'+') INT)* ']'
    | '[:]'
    ;

statedef
    : 'state' ID transition* update* 'end'
    ;

transition
    : 'transition to' ID 'if' conditional
    | 'transition to' ID 'if' conditional 'begin' update* 'end'
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
     | number
     | attrsget
     | func
     | listcomp
     | ID
     | lparen expression rparen
     ;


assignment
    : (ID|attrsget) '=' expression
    ;

codeblock
    : 'begin' codeline* 'end'
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
    ;
//fragment
ESC
    : '\\"' | '\\\\'
    ;

SPACE: [ ]-> channel(2);
