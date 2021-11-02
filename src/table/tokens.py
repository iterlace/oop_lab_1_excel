from dataclasses import dataclass

# 1,5,6,8,10
# +, -, *, /
# ++, --
# max(x, y), min(x, y)
# =, <, >
# !  (not)


# A1 > (A2)
#

grammar = """
<upper-letter>      ::= "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z"
<lower-letter>      ::= "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z"
<letter>            ::= <caps-letter> | <lower-letter>
<natural-digit>     ::= "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
<digit>             ::= "0" | <natural-digit>
<opt-whitespace>    ::= " " <opt-whitespace> | ""

<cell-ref>          ::= <caps-letter><digit>
<integer>           ::= <digit>+
<float>             ::= <digit>+ "." <digit>+
<number>            ::= <integer> | <float>

<object>            ::= <cell-ref> | <number> | <function>

<binary-operator>   ::= "+" | "-" | "*" | "/" | "=" | ">" | "<"
<prefix-operator>   ::= "++" | "--" | "!"
<function-name>     ::= <lower-letter>[(<letter> | <digit>)*]

<function>          ::= <function-name> "(" () ")"

"""  # noqa

GRAMMAR = '''
    @@grammar::CALC


    start = expression $ ;


    expression
        =
        | expression '+' term
        | expression '-' term
        | term
        ;


    term
        =
        | term '*' factor
        | term '/' factor
        | factor
        ;


    factor
        =
        | '(' expression ')'
        | number
        ;


    number = /\d+/ ;
'''

GRAMMAR2 = """
#     start = expression
# 
#     expression          = (expression "+" term) / (expression "-" term) / term
# 
#     term                = (term "*" factor) / (term "/" factor) / factor
# 
#     factor              = ("(" expression ")") / number
# 
#     natural_digit       = "1" / "2" / "3" / "4" / "5" / "6" / "7" / "8" / "9"
#     digit               = "0" / natural_digit 
#     number              = digit+
# """

GRAMMAR2 = r"""
    start = expression
    
    expression          = term / (expression "+" term) / (expression "-" term)
    
    term                = factor / (term "*" factor) / (term "/" factor)

    factor              = ("(" expression ")") / number

    natural_digit       = "1" / "2" / "3" / "4" / "5" / "6" / "7" / "8" / "9"
    digit               = "0" / natural_digit 
    number              = ~"\d+"i
    opt_whitespace      = (" "*)?
"""


if __name__ == '__main__':
    import json
    import tatsu

    expr = "3 + 5 * ( 10 - 20 )"
    # t = tatsu.parse(GRAMMAR, expr)
    # print()

    from parsimonious.grammar import Grammar
    g = Grammar(GRAMMAR2).default("start")
    r = g.parse("1+1")
    print()


class Token:

    def __init__(self):
        pass

