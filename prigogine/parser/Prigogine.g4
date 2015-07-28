grammar Prigogine;

@lexer::members {
COMMENTS = 1
SPACES = 2
}

//filestart
  //  : (population | initglobal | create | runmodel)+ finalise*
    //;

filestart
    : model+ simulation*
    ;

model
    : 'model' ID '[' (parameterlist* variablelist equationlist population+) ']'
    ;

simulation
    : 'simulation' '[' codeinsert ']'
    ;

codeinsert
    //: (ESC|.)*?
    : ~('\n'|'\r')*?
    ;

equationlist
    : 'equations' '[' (elementwiseEquation | mapEquation)+ ']'
    ;

elementwiseEquation
    : ID '[t+1]' '=' expression (',' 'where' conditional)*
    | ID ('.' ID)* '[t+1]' '=' expression (',' 'where' conditional)*
    ;

mapEquation
    : ID '[t+1]' '[n]''=' expression (',' 'where' conditional)*
    | ID ('.' ID)* '[t+1]' '[n]' '=' expression (',' 'where' conditional)*
    ;

assignment
    : ID (('.' ID) | timeindex)* '=' expression
    ;

//population
 //   : 'population' ID '[' parameterlist variablelist statedef+ ']'
  //  | 'population' ID '[' statedef+ ']'
   // ;

population
    : 'population' ID '[' parameterlist* variablelist equationlist ']'
    ;

//initglobal
  //  : 'global' ID expression
    //;

//initvars
 //   : 'vars' ID expression
  //  ;

//initparams
 //   : 'params' ID expression
  //  ;

//initstates
 //   : 'startstates' expression
  //  ;

//create
 //   : 'create' ID INT createblock*
  //  ;

//createblock
  //  : '[' createline* ']'
  //  ;

//createline
  //   : (initvars | initstates | initparams)+
   //  ;

//runmodel
    //: 'runmodel' INT codeblock*
  //  : 'runmodel' INT '[' (initglobal | create)* ']'
    //;

//finalise
  //  : 'finalise' codeblock*
   // ;

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
    | '[' listdef ']'
    ;

tupledef
    : '(' ( (ID | number | string) (',' (ID | number | string) )* )* ')'
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
    : ('[' timevar (SUB INT)* ']' | '[:]')+
    ;

timevar
    : 't'
    | INT
    ;

dictindex
    : ('[' string ']')
    ;

//statedef
  //  : 'state' ID '[' (transition | update | updateglobal)* ']'
  //  ;

//transition
 //   : 'transition' ID 'where' conditional codeblock*
  //  ;

//update
 //   : 'update' ID (codeline | codeblock)
 //   ;

//updateglobal
 //   : 'updateglobal' ID (codeline | codeblock)
  //  ;

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

//argument
 //   : number
 //   | ID
  //  | func
  //  ;

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
