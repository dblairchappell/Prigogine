grammar Prigogine;

@lexer::members {
COMMENTS = 1
SPACES = 2
}

filestart
    : population+ //experiment*
    ;

//modeldef
  //  : 'model' string '[' population+ ']'
    //;

population
    : 'population' string '[' attributelist statedef* ']'
    ;

//createpopulation
//    : 'create' ID INT startstate initvar* 'end'
//    ;

//experiment
  //  : 'experiment' string codeblock*
    //;

//startstate
  //  : 'startstate' ID
    //;

//runmodel
//    : 'runmodel' INT ('[' expression* ']')*
//    ;

//initvar
  //  : 'init' attrsget (codeline | codeblock)
    //;

attributelist
    : 'attributes' '[' attribute* ']'
    ;

listcomp
    : '[' expression 'for' ID 'in' expression ']'
    ;

attribute
    : string
    ;

attrsget
    : 'attributes' dictindex timeindex
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
    : 'state' string '[' transition* action* ']'
    ;

transition
    : 'transition to' string 'if' conditional
    | 'transition to' string 'if' conditional '[' action* ']'
    ;

action
    : 'action' (codeline | codeblock)
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
     | string
     | number
     | attrsget
     | func
     | listcomp
     | ID
     | timevar
     | lparen expression rparen
     ;

assignment
    : (ID|attrsget) '=' expression
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
    ;
//fragment
ESC
    : '\\"' | '\\\\'
    ;

SPACE: [ ]-> channel(2);
