# Generated from Excel.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExcelParser import ExcelParser
else:
    from ExcelParser import ExcelParser

# This class defines a complete generic visitor for a parse tree produced by ExcelParser.

class ExcelVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExcelParser#NumberExpr.
    def visitNumberExpr(self, ctx:ExcelParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#NotExpr.
    def visitNotExpr(self, ctx:ExcelParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#IncDecExpr.
    def visitIncDecExpr(self, ctx:ExcelParser.IncDecExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#ParenExpr.
    def visitParenExpr(self, ctx:ExcelParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#InfixExpr.
    def visitInfixExpr(self, ctx:ExcelParser.InfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#FunExpr.
    def visitFunExpr(self, ctx:ExcelParser.FunExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#CellRefExpr.
    def visitCellRefExpr(self, ctx:ExcelParser.CellRefExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#function.
    def visitFunction(self, ctx:ExcelParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#function_args.
    def visitFunction_args(self, ctx:ExcelParser.Function_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#function_arg.
    def visitFunction_arg(self, ctx:ExcelParser.Function_argContext):
        return self.visitChildren(ctx)



del ExcelParser