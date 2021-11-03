# Generated from Excel.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExcelParser import ExcelParser
else:
    from ExcelParser import ExcelParser

# This class defines a complete listener for a parse tree produced by ExcelParser.
class ExcelListener(ParseTreeListener):

    # Enter a parse tree produced by ExcelParser#NumberExpr.
    def enterNumberExpr(self, ctx:ExcelParser.NumberExprContext):
        pass

    # Exit a parse tree produced by ExcelParser#NumberExpr.
    def exitNumberExpr(self, ctx:ExcelParser.NumberExprContext):
        pass


    # Enter a parse tree produced by ExcelParser#NotExpr.
    def enterNotExpr(self, ctx:ExcelParser.NotExprContext):
        pass

    # Exit a parse tree produced by ExcelParser#NotExpr.
    def exitNotExpr(self, ctx:ExcelParser.NotExprContext):
        pass


    # Enter a parse tree produced by ExcelParser#IncDecExpr.
    def enterIncDecExpr(self, ctx:ExcelParser.IncDecExprContext):
        pass

    # Exit a parse tree produced by ExcelParser#IncDecExpr.
    def exitIncDecExpr(self, ctx:ExcelParser.IncDecExprContext):
        pass


    # Enter a parse tree produced by ExcelParser#ParenExpr.
    def enterParenExpr(self, ctx:ExcelParser.ParenExprContext):
        pass

    # Exit a parse tree produced by ExcelParser#ParenExpr.
    def exitParenExpr(self, ctx:ExcelParser.ParenExprContext):
        pass


    # Enter a parse tree produced by ExcelParser#InfixExpr.
    def enterInfixExpr(self, ctx:ExcelParser.InfixExprContext):
        pass

    # Exit a parse tree produced by ExcelParser#InfixExpr.
    def exitInfixExpr(self, ctx:ExcelParser.InfixExprContext):
        pass


    # Enter a parse tree produced by ExcelParser#FunExpr.
    def enterFunExpr(self, ctx:ExcelParser.FunExprContext):
        pass

    # Exit a parse tree produced by ExcelParser#FunExpr.
    def exitFunExpr(self, ctx:ExcelParser.FunExprContext):
        pass


    # Enter a parse tree produced by ExcelParser#CellRefExpr.
    def enterCellRefExpr(self, ctx:ExcelParser.CellRefExprContext):
        pass

    # Exit a parse tree produced by ExcelParser#CellRefExpr.
    def exitCellRefExpr(self, ctx:ExcelParser.CellRefExprContext):
        pass


    # Enter a parse tree produced by ExcelParser#function.
    def enterFunction(self, ctx:ExcelParser.FunctionContext):
        pass

    # Exit a parse tree produced by ExcelParser#function.
    def exitFunction(self, ctx:ExcelParser.FunctionContext):
        pass


    # Enter a parse tree produced by ExcelParser#function_args.
    def enterFunction_args(self, ctx:ExcelParser.Function_argsContext):
        pass

    # Exit a parse tree produced by ExcelParser#function_args.
    def exitFunction_args(self, ctx:ExcelParser.Function_argsContext):
        pass


    # Enter a parse tree produced by ExcelParser#function_arg.
    def enterFunction_arg(self, ctx:ExcelParser.Function_argContext):
        pass

    # Exit a parse tree produced by ExcelParser#function_arg.
    def exitFunction_arg(self, ctx:ExcelParser.Function_argContext):
        pass



del ExcelParser