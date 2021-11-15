import logging
import re
from typing import List

from antlr4 import CommonTokenStream, InputStream

from dist.ExcelLexer import ExcelLexer
from dist.ExcelParser import ExcelParser
from table.visitor import ExcelVisitor

from .types import CalculatedValue, CalculationError, CellIdx, CellRef, Formula

# 1,5,6,8,10
# +, -, *, /
# ++, --
# max(x, y), min(x, y)
# =, <, >
# !  (not)

# ++(!((1+1)*(1)*min(5, 4)) > (1) = max(A1*1.0+1, 5)*2)
# ++(!((1+1)*(1)*min(5, 4)) > (1))

__all__ = ["Table"]
logger = logging.getLogger(__name__)

cell_ref_mask = re.compile(r"^([A-Z]*)(\d*)$")


class Table:
    def __init__(self, cols: List[str], rows: List[str]):
        self.cols = cols.copy()
        self.rows = rows.copy()
        self.ncols = len(cols)
        self.nrows = len(rows)
        self.formula_matrix = [["" for _ in rows] for _ in cols]
        self.calculated_matrix = [[None for _ in rows] for _ in cols]

    def calculate(self, formula: Formula) -> CalculatedValue:
        try:
            data = InputStream(formula)
            # lexer
            lexer = ExcelLexer(data)
            stream = CommonTokenStream(lexer)
            # parser
            parser = ExcelParser(stream)
            tree = parser.expr()
            # evaluator
            visitor = ExcelVisitor(self)
            output = visitor.visit(tree)
            return output
        except Exception as e:
            logger.warning(f"Got parsing error: {e}")
            return CalculationError

    def set(self, h: int, w: int, formula: Formula) -> CalculatedValue:
        value = self.calculate(formula)
        self.formula_matrix[h][w] = formula
        self.calculated_matrix[h][w] = value
        return value

    def get_formula(self, h: int, w: int) -> Formula:
        return self.formula_matrix[h][w]

    def get_calculated(self, h: int, w: int) -> CalculatedValue:
        return self.calculated_matrix[h][w]

    def get_cell_formula(self, cell: CellRef) -> Formula:
        return self.get_formula(*self.cell_index(cell))

    def get_cell_calculated(self, cell: CellRef) -> CalculatedValue:
        return self.get_calculated(*self.cell_index(cell))

    def cell_index(self, cell: CellRef) -> CellIdx:
        if isinstance(cell, tuple):
            try:
                w = self.cols.index(cell[0])
                h = self.rows.index(cell[1])
            except IndexError:
                raise ValueError(f"Cell {cell} isn't present")
        else:
            match = cell_ref_mask.match(cell)
            if not match:
                raise ValueError(f"Cell {cell} has invalid format")
            try:
                w = self.cols.index(match.group(1))
                h = self.rows.index(match.group(2))
            except IndexError:
                raise ValueError(f"Cell {cell} isn't present")
        return h, w
