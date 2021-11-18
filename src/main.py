# This Python file uses the following encoding: utf-8
import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QMessageBox


from table.widgets import TableWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.table_widget = TableWidget()
        self.setCentralWidget(self.table_widget)
        self.init_actions()
        self.init_menubar()

    def init_actions(self):
        self.open_action = QAction(self.table_widget)
        self.open_action.setText("&Open")
        self.open_action.triggered.connect(self.table_widget.on_open)

        self.save_action = QAction(self.table_widget)
        self.save_action.setText("&Save")
        self.save_action.triggered.connect(self.table_widget.on_save)

        self.usage_action = QAction(self.table_widget)
        self.usage_action.setText("&Usage")
        self.usage_action.triggered.connect(self.on_usage)

    def init_menubar(self):
        menubar = self.menuBar()
        file_menu = QMenu("&File", self)
        menubar.addMenu(file_menu)

        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)

        file_menu = QMenu("&Help", self)
        menubar.addMenu(file_menu)
        file_menu.addAction(self.usage_action)

    def on_usage(self):
        QMessageBox.information(
            self,
            "Usage",
            f"Available data types, operators and functions:\n"
            f" - Available data types: integer and float\n"
            f" - Infix binary operators: 1+1, 1-1, 1*1, 1/1\n"
            f" - Prefix unary operators: ++1, --1\n"
            f" - NOT expression: !1\n"
            f" - Comparisons: 1<1, 1>1, 1=1\n"
            f" - Parenthesis: (1+1)\n"
            f" - Cell references: F11, E9\n"
            f" - Functions: max(1, 2), min(5, 1)",
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = MainWindow()
    table.show()
    sys.exit(app.exec())
