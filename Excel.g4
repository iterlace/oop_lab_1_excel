grammar Excel;

/*
 * Parser Rules
 */

expr:
      '!' expr                                 # NotExpr
    | op=('++'|'--') expr                      # IncDecExpr
    | function                                 # FunExpr
    | left=expr op=('*'|'/') right=expr        # InfixExpr
    | left=expr op=('+'|'-') right=expr        # InfixExpr
    | left=expr op=('>'|'<'|'=') right=expr    # InfixExpr
    | (INT | FLOAT)                            # NumberExpr
    | '(' expr ')'                             # ParenExpr
    ;

function:       name=object_name '(' args=function_args ')';
function_args:  (function_arg (',' function_arg)*)?;
function_arg:   expr;

object_name: CHAR (CHAR | INT | '_')* ;

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
