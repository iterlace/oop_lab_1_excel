# This Python file uses the following encoding: utf-8
import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu

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

    def init_menubar(self):
        menubar = self.menuBar()
        file_menu = QMenu("&File", self)
        menubar.addMenu(file_menu)

        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = MainWindow()
    table.show()
    sys.exit(app.exec())
