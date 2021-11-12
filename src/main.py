# This Python file uses the following encoding: utf-8
import io
import sys
from typing import Iterable
import time
import functools
import string

from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt6.QtGui import QFont, QAction, QKeyEvent
from PyQt6.QtCore import QPoint, QModelIndex, pyqtBoundSignal, QEvent
from antlr4 import *

from table.table import Table
from table.types import CalculationError, CalculatedValue, Formula
from dist.ExcelLexer import ExcelLexer
from dist.ExcelParser import ExcelParser
from table.visitor import ExcelVisitor


class TableWidget(QTableWidget):

    def __init__(self):
        super(TableWidget, self).__init__()

        cols = list(string.ascii_uppercase)
        rows = [str(i) for i in range(1, 101)]
        self.table = Table(rows, cols)

        self.setRowCount(len(rows))
        self.setColumnCount(len(cols))

        self.setHorizontalHeaderLabels(cols)
        self.setVerticalHeaderLabels(rows)

        self._set_debug_callbacks()
        self.cellDoubleClicked.connect(self.on_enter)
        self.itemChanged.connect(self.on_change)
        self.currentCellChanged.connect(self.on_cell_change)

    def _set_debug_callbacks(self):
        actions = [i for i in dir(self)
                   if "signal" in type(getattr(self, i)).__name__.lower()]
        for action in actions:
            def l(__action):
                @functools.wraps(l)
                def inner(*args, **kwargs):
                    print(__action, args, kwargs)

                return inner

            getattr(self, action).connect(l(action))

    def on_enter(self, x, y):
        value = self.table.get_formula(x, y)
        if item := self.item(x, y):
            self.set(item, value)

    def on_change(self, item: QTableWidgetItem):
        value = item.text()
        if not value:
            return
        h, w = item.row(), item.column()
        result = self.table.set(h, w, value)
        self.set(item, self.represent(result))

    def on_cell_change(self, new_h, new_w, old_h, old_w):
        old_item = self.item(old_h, old_w)
        if not old_item:
            return
        if not old_item.text():
            return
        # re-calculate the cell
        result = self.table.set(
            old_h,
            old_w,
            self.table.get_formula(old_h, old_w),
        )
        self.set(old_item, self.represent(result))

    def set(self, item: QTableWidgetItem, value: str):
        self.blockSignals(True)
        item.setText(value)
        self.blockSignals(False)

    def represent(self, value: CalculatedValue) -> str:
        if value is CalculationError:
            return "%#ERR"
        if value is None:
            return ""

        return str(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = TableWidget()
    table.show()
    sys.exit(app.exec())
