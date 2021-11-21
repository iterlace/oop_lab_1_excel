import string
import functools

from PyQt6.QtWidgets import QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem

from table import Table
from table.serializer import DeserializationError, SerializationError, Serializer
from table.types import CalculatedValue, CalculationError
from table.utils import cols_generator, int_to_col, rows_generator


class TableWidget(QTableWidget):
    def __init__(self):
        super(TableWidget, self).__init__()

        self.cols = cols_generator(26)
        self.rows = rows_generator(100)
        self.table = Table(self.cols, self.rows)

        self.setRowCount(len(self.rows))
        self.setColumnCount(len(self.cols))

        self.setHorizontalHeaderLabels(self.cols)
        self.setVerticalHeaderLabels(self.rows)

        self.cellDoubleClicked.connect(self.on_enter)
        self.itemChanged.connect(self.on_change)
        self.currentCellChanged.connect(self.on_cell_change)
        self._set_debug_callbacks()

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

    def on_save(self):
        filepath, _ = QFileDialog().getSaveFileName(
            parent=self,
            caption="Select a save path",
            filter="JSON (*.json)",
        )
        if not filepath:
            return

        try:
            Serializer.save(self.table, filepath)
        except SerializationError as e:
            QMessageBox.critical(self, "Error saving table", e.message)
            return

    def on_open(self):
        filepath, _ = QFileDialog().getOpenFileName(
            parent=self,
            caption="Select a .json dump",
            filter="JSON (*.json)",
        )
        if not filepath:
            return

        try:
            table = Serializer.load(filepath, self.cols, self.rows)
        except DeserializationError as e:
            QMessageBox.critical(self, "Error loading table", e.message)
            return
        else:
            for row_idx, col in enumerate(table.formula_matrix):
                for col_idx, value in enumerate(col):
                    item = QTableWidgetItem()
                    item.setText(value)
                    self.setItem(row_idx, col_idx, item)

    def on_enter(self, row, col):
        value = self.table.get_formula(col, row)
        if item := self.item(row, col):
            self.set(item, value)

    def on_change(self, item: QTableWidgetItem):
        value = item.text()
        if not value:
            return
        col, row = item.column(), item.row()
        result = self.table.set(col, row, value)
        self.set(item, self.represent(result))

    def on_cell_change(self, new_row, new_col, old_row, old_col):
        old_item = self.item(old_row, old_col)
        if not old_item:
            return
        if not old_item.text():
            return
        # re-calculate the cell
        result = self.table.set(
            old_col,
            old_row,
            self.table.get_formula(old_col, old_row),
        )
        self.set(old_item, self.represent(result))

    def resize_table(self, new_cols, new_rows):
        table = Table(new_cols, new_rows)
        for col_id, col in enumerate(self.table.formula_matrix):
            for row_id, value in enumerate(col):
                print(col_id, row_id, value)
                try:
                    table.set(col_id, row_id, value)
                except IndexError:
                    continue
        self.table = table

    def on_add_column(self):
        columns = cols_generator(len(self.cols) + 1)
        self.setColumnCount(len(columns))
        self.setHorizontalHeaderLabels(columns)
        self.resize_table(columns, self.rows)
        self.cols = columns

    def on_add_row(self):
        rows = rows_generator(len(self.rows) + 1)
        self.setRowCount(len(rows))
        self.setVerticalHeaderLabels(rows)
        self.resize_table(rows, self.cols)
        self.rows = rows

    def on_remove_column(self):
        if len(self.cols) <= 1:
            return
        columns = cols_generator(len(self.cols) - 1)
        self.setColumnCount(len(columns))
        self.setHorizontalHeaderLabels(columns)
        self.resize_table(columns, self.rows)
        self.cols = columns

    def on_remove_row(self):
        if len(self.rows) <= 1:
            return
        rows = rows_generator(len(self.rows) - 1)
        self.setRowCount(len(rows))
        self.setVerticalHeaderLabels(rows)
        self.resize_table(self.cols, rows)
        self.rows = rows

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
