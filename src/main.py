# This Python file uses the following encoding: utf-8
import sys
from typing import Iterable
import time
import functools

from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt6.QtGui import QFont, QAction
from PyQt6.QtCore import QPoint, QModelIndex


class TableWindow(QTableWidget):

    def __init__(self):
        super(TableWindow, self).__init__()

        self.setRowCount(5)
        self.setColumnCount(5)

        self.setHorizontalHeaderLabels(["A", "B", "C", "D", "E"])
        self.setVerticalHeaderLabels(["1", "2", "3", "4", "5"])

        self._set_debug_callbacks()

    def _set_debug_callbacks(self):
        for action in ['activated', 'cellActivated', 'cellClicked', 'cellDoubleClicked',
                       'cellEntered', 'cellPressed', 'clicked', 'destroyed', 'doubleClicked',
                       'entered', 'itemActivated', 'itemClicked', 'itemDoubleClicked',
                       'itemEntered', 'itemPressed', 'itemSelectionChanged', 'objectNameChanged',
                       'pressed', 'cellChanged']:
            def l(__action):
                @functools.wraps(l)
                def inner(*args, ** kwargs):
                    print(__action, args, kwargs)
                return inner

            getattr(self, action).connect(l(action))

    # def setData(self):
    #     for n, key in enumerate(sorted(self.data.keys())):
    #         for m, item in enumerate(self.data[key]):
    #             newitem = QTableWidgetItem(item)
    #             self.setItem(m, n, newitem)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = TableWindow()
    table.show()
    sys.exit(app.exec())
