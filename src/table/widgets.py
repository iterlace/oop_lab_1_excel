import functools
import string

from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QFileDialog, QErrorMessage, QMessageBox
from table import Table
from table.types import CalculatedValue, CalculationError
from table.serializer import Serializer, SerializationError, DeserializationError


class TableWidget(QTableWidget):
    def __init__(self):
        super(TableWidget, self).__init__()

        self.cols = list(string.ascii_uppercase)
        self.rows = [str(i) for i in range(1, 101)]
        self.table = Table(self.cols, self.rows)

        self.setRowCount(len(self.rows))
        self.setColumnCount(len(self.cols))

        self.setHorizontalHeaderLabels(self.cols)
        self.setVerticalHeaderLabels(self.rows)

        self.cellDoubleClicked.connect(self.on_enter)
        self.itemChanged.connect(self.on_change)
        self.currentCellChanged.connect(self.on_cell_change)

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
            QMessageBox.critical(self, "Error saving table", e.message),
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
            QMessageBox.critical(self, "Error loading table", e.message),
            return
        else:
            for row_idx, col in enumerate(table.formula_matrix):
                for col_idx, value in enumerate(col):
                    item = QTableWidgetItem()
                    item.setText(value)
                    self.setItem(row_idx, col_idx, item)

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
