from typing import Tuple

from dist.ExcelParser import ExcelParser
from dist.ExcelVisitor import ExcelVisitor as GeneratedVisitor
from table.functions import FunctionExecutor


class ExcelVisitor(GeneratedVisitor):
    def __init__(self, table):
        self.table = table
        super(ExcelVisitor, self).__init__()

    # Visit a parse tree produced by ExcelParser#NumberExpr.
    def visitNumberExpr(self, ctx: ExcelParser.NumberExprContext):
        value = ctx.getText()
        return float(value)

    # Visit a parse tree produced by ExcelParser#NotExpr.
    def visitNotExpr(self, ctx: ExcelParser.NotExprContext) -> int:
        value = self.visit(ctx.expr())
        return int(not bool(value))

    # Visit a parse tree produced by ExcelParser#IncDecExpr.
    def visitIncDecExpr(self, ctx: ExcelParser.IncDecExprContext) -> Tuple[int, float]:
        value = self.visit(ctx.expr())
        op = ctx.op.text
        operation = {
            "++": lambda: value + 1,
            "--": lambda: value - 1,
        }
        return operation.get(op, lambda: None)()

    # Visit a parse tree produced by ExcelParser#ParenExpr.
    def visitParenExpr(self, ctx: ExcelParser.ParenExprContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by ExcelParser#InfixExpr.
    def visitInfixExpr(self, ctx: ExcelParser.InfixExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        op = ctx.op.text
        operation = {
            "+": lambda: left + right,
            "-": lambda: left - right,
            "*": lambda: left * right,
            "/": lambda: left / right,
            "<": lambda: int(left < right),
            ">": lambda: int(left > right),
            "=": lambda: int(left == right),
        }
        return operation.get(op, lambda: None)()

    # Visit a parse tree produced by ExcelParser#FunExpr.
    def visitFunExpr(self, ctx: ExcelParser.FunExprContext):
        return self.visit(ctx.function())

    # Visit a parse tree produced by ExcelParser#CellRefExpr.
    def visitCellRefExpr(self, ctx: ExcelParser.CellRefExprContext):
        cell = ctx.CELL_NAME().getText()
        h, w = self.table.cell_index(cell)
        return self.table.get_calculated(h, w)

    # Visit a parse tree produced by ExcelParser#function.
    def visitFunction(self, ctx: ExcelParser.FunctionContext):
        function_name = ctx.name.text
        args = self.visit(ctx.function_args())
        result = FunctionExecutor.execute(function_name, args)
        return result

    # Visit a parse tree produced by ExcelParser#function_args.
    def visitFunction_args(self, ctx: ExcelParser.Function_argsContext):
        result = []
        for arg in ctx.function_arg():
            result.append(self.visit(arg))
        return result

    # Visit a parse tree produced by ExcelParser#function_arg.
    def visitFunction_arg(self, ctx: ExcelParser.Function_argContext):
        return self.visit(ctx.expr())


del ExcelParser
