/* 
    Gramatica Little Duck
    Compiladores
    Tarea 3.2
    Diego Fernando Montaño Pérez
*/

grammar LittleDuckGrammar;

//Tokens
INT: 'int';
FLOAT: 'float';
EQUAL: '=';
TIMES: '*';
DIV: '/';
PLUS: '+';
MINUS: '-';
DIFF: '<>';
GREATER: '>';
SMALLER: '<';
L_BRACE: '(';
R_BRACE: ')';
L_BRK: '{';
R_BRK: '}';
COMMA: ',';
SEMICOLON: ';';
COLON: ':';
PROGRAM: 'program';
IF: 'if';
ELSE: 'else';
VAR: 'var';
PRINT: 'print';
ID: ([A-Z]|[a-z]) ([A-Z]|[a-z]|[0-9])*;
CTEI: ('0'|([1-9]([0-9])*));
CTEF: ('0'|([1-9]([0-9])*))'.'([0-9]+)(('e'|'E')('+'|'-')?('0'|([1-9]([0-9])*)))? ;
STRING: '"' ('\\' ["\\] | ~["\\\r\n])* '"';
WHITESPACE : [ \t\r\n]+ -> skip ;

//Gramatic Rules
program
: PROGRAM ID SEMICOLON bloque
| PROGRAM ID SEMICOLON vars bloque;

vars
: VAR vars2;

vars2
: vars3 COLON tipo SEMICOLON vars2
| vars3 COLON tipo SEMICOLON;

vars3
: ID
| ID COMMA vars3;

tipo
: INT
| FLOAT;

bloque
: L_BRK estatuto2 R_BRK
| L_BRK R_BRK;

estatuto2
: estatuto
| estatuto2 estatuto;

estatuto
: asignacion
| condicion
| escritura;

asignacion
: ID EQUAL expresion SEMICOLON;

condicion
: IF L_BRACE expresion R_BRACE bloque SEMICOLON
| IF L_BRACE expresion R_BRACE bloque ELSE bloque SEMICOLON;

escritura
: PRINT L_BRACE escrituraGram R_BRACE SEMICOLON;

escrituraGram
: expresion
| expresion COMMA escrituraGram
| varcte
| varcte COMMA escrituraGram;

expresion
: exp
| exp GREATER exp
| exp SMALLER exp
| exp DIFF exp;

exp
: termino
| termino exp2;

exp2
: PLUS exp
| MINUS exp;

termino
: factor
| factor termino2;

termino2
: TIMES termino
| DIV termino;

factor
: L_BRACE expresion R_BRACE
| PLUS varcte
| MINUS varcte
| varcte;

varcte
: ID
| CTEF
| CTEI
| STRING;




