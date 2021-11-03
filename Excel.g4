grammar Excel;

/*
 * Parser Rules
 */

expr:
      '!' expr                                 # NotExpr
    | op=('++'|'--') expr                      # IncDecExpr
    | function                                 # FunExpr
    | CELL_NAME                                # CellRefExpr
    | left=expr op=('*'|'/') right=expr        # InfixExpr
    | left=expr op=('+'|'-') right=expr        # InfixExpr
    | left=expr op=('>'|'<'|'=') right=expr    # InfixExpr
    | (INT | FLOAT)                            # NumberExpr
    | '(' expr ')'                             # ParenExpr
    ;

function        :  name=OBJECT_NAME '(' args=function_args ')';
function_args   :  (function_arg (',' function_arg)*)?;
function_arg    :  expr;

/*
 * Lexer Rules
 */

fragment NATURAL    : [1-9] ;
fragment DIGIT      : [0-9] ;

INT        : DIGIT+ ;
FLOAT      : DIGIT+ ([.] DIGIT+)? ;
CHAR       : [a-zA-Z] ;
UPPERCHAR  : [A-Z] ;
LOWERCHAR  : [a-z] ;
WHITESPACE : [ \t]+ -> skip ;

// cell reference, e.g. F4 or A3
CELL_NAME   : UPPERCHAR DIGIT;

// actually only function is called an object
OBJECT_NAME: CHAR (CHAR | INT | '_')* ;
