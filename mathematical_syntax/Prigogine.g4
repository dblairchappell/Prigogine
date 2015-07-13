grammar Prigogine;

filestart
    : (equation | initvar | initparam)+ command+ //{import Prigogine as pr}
    ;

command
    : expression //';'
    ;

expression
     : expression '^' expression
     | expression op=('*'|'/') expression
     | expression op=('+'|'-') expression
     | expression '|' expression
     | expression op=('<'|'>'|'>='|'<='|'=='|'!=') expression
     | number
     | ID
     | func
     | deflist
     | getvar
     | '(' expression ')'
     ;

initvar
    : ID '=' listcomp //';'
    ;

initparam
    : ID '=' expression //';'
    ;

getvar
    : ID ('[' timestep ((SUB|ADD) number)* ']')
    | ID '[' INT ']'
    ;

listcomp
    : '[' expression 'for' ID 'in' deflist ']'
    ;

equation
    : ID ('[' timestep ((SUB|ADD) number)* ']') '=' expression //';' //{print("getting variable $varId")}
    ;

timestep
    : 't'
    ;

func
    : funcId = ID '(' expression (',' expression)* ')' //{print("calling function $funcId")}
    ;

number
    : INT
    | FLOAT
    ;

deflist
    : '[' (ID|number) (',' (ID|number))* ']'
    | '[' (ID|number) ':' (ID|number) ']'
    ;

LineComment
  : '#' ~[\r\n]* -> channel(HIDDEN)
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
    : [ \t\r\n]+ -> skip
    ;

MUL :   '*' ;
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;

