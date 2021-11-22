import pytest
from antlr4 import CommonTokenStream, InputStream

from dist.ExcelLexer import ExcelLexer
from dist.ExcelParser import ExcelParser
from table.table import Table
from table.types import CalculatedValue
from table.visitor import ExcelVisitor


@pytest.fixture(scope="function")
def cols():
    return ["A", "B", "C", "D", "E", "F", "G"]


@pytest.fixture(scope="function")
def rows():
    return ["1", "2", "3", "4", "5", "6", "7"]


@pytest.fixture(scope="function")
def table(cols, rows):
    t = Table(cols, rows)
    yield t


class TestParser:
    @staticmethod
    def calc(table: Table, formula: str) -> CalculatedValue:
        data = InputStream(formula)
        # lexer
        lexer = ExcelLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = ExcelParser(stream)
        tree = parser.expr()
        # evaluator
        visitor = ExcelVisitor(table)
        output = visitor.visit(tree)
        return output

    def test_funcs(self, table):
        assert self.calc(table, "max(5, -1)") == 5
        assert self.calc(table, "min(-6, -999.5)") == -999.5

    def test_comparison_operators(self, table):
        assert self.calc(table, "5 = 5") == 1
        assert self.calc(table, "5.0 = 5") == 1
        assert self.calc(table, "4 = 5") == 0

        assert self.calc(table, "5.1 > 5") == 1
        assert self.calc(table, "5 > 5") == 0

        assert self.calc(table, "5 < 6") == 1
        assert self.calc(table, "5.1 < 5") == 0
        assert self.calc(table, "5 < 5") == 0

    def test_not_operator(self, table):
        assert self.calc(table, "!0") == 1
        assert self.calc(table, "!5") == 0
        assert self.calc(table, "!1") == 0
        assert self.calc(table, "!(-1)") == 0
