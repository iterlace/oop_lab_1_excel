import logging
import re
from typing import List

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener

from dist.ExcelLexer import ExcelLexer
from dist.ExcelParser import ExcelParser
from table.visitor import ExcelVisitor
from typing import Tuple

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
        # self.calculated_matrix = [[None for _ in rows] for _ in cols]

    def calculate(self, formula: Formula) -> CalculatedValue:
        def recover(exc):
            raise exc

        try:
            data = InputStream(formula)
            # lexer
            lexer = ExcelLexer(data)
            lexer.recover = recover
            lexer.removeErrorListeners()
            lexer.addErrorListener(ErrorListener())
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

    def set(self, col: int, row: int, formula: Formula) -> CalculatedValue:
        value = self.calculate(formula)
        self.formula_matrix[col][row] = formula
        # self.calculated_matrix[h][w] = value
        return value

    def get_formula(self, col: int, row: int) -> Formula:
        return self.formula_matrix[col][row]

    def get_calculated(self, col: int, row: int) -> CalculatedValue:
        value = self.calculate(self.formula_matrix[col][row])
        return value

    def get_cell_formula(self, cell: CellRef) -> Formula:
        return self.get_formula(*self.cell_index(cell))

    def get_cell_calculated(self, cell: CellRef) -> CalculatedValue:
        return self.get_calculated(*self.cell_index(cell))

    @staticmethod
    def parse_cell_ref(cell: str) -> Tuple[str, str]:
        match = cell_ref_mask.match(cell)
        if not match:
            raise ValueError(f"Cell {cell} has invalid format")
        return match.group(1), match.group(2)

    def cell_index(self, cell: CellRef) -> CellIdx:
        if isinstance(cell, tuple):
            try:
                col = self.cols.index(cell[0])
                row = self.rows.index(cell[1])
            except IndexError:
                raise ValueError(f"Cell {cell} isn't present")
        else:
            match = self.parse_cell_ref(cell)
            try:
                col = self.cols.index(match[0])
                row = self.rows.index(match[1])
            except IndexError:
                raise ValueError(f"Cell {cell} isn't present")
        return col, row
