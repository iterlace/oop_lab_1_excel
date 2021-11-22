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
        self.open_action.setText("&Відкрити")
        self.open_action.triggered.connect(self.table_widget.on_open)

        self.save_action = QAction(self.table_widget)
        self.save_action.setText("&Зберегти")
        self.save_action.triggered.connect(self.table_widget.on_save)

        self.help_action = QAction(self.table_widget)
        self.help_action.setText("&Допомога")
        self.help_action.triggered.connect(self.on_help)

        self.about_action = QAction(self.table_widget)
        self.about_action.setText("&Про додаток")
        self.about_action.triggered.connect(self.on_about)

        self.add_row_action = QAction(self.table_widget)
        self.add_row_action.setText("&[+] рядок")
        self.add_row_action.triggered.connect(self.table_widget.on_add_row)

        self.add_col_action = QAction(self.table_widget)
        self.add_col_action.setText("&[+] колонка")
        self.add_col_action.triggered.connect(self.table_widget.on_add_column)

        self.remove_row_action = QAction(self.table_widget)
        self.remove_row_action.setText("&[-] рядок")
        self.remove_row_action.triggered.connect(self.table_widget.on_remove_row)

        self.remove_col_action = QAction(self.table_widget)
        self.remove_col_action.setText("&[-] колонка")
        self.remove_col_action.triggered.connect(self.table_widget.on_remove_column)

    def init_menubar(self):
        menubar = self.menuBar()

        file_menu = QMenu("&Файл", self)
        menubar.addMenu(file_menu)
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)

        table_menu = QMenu("&Таблиця", self)
        menubar.addMenu(table_menu)
        table_menu.addAction(self.add_col_action)
        table_menu.addAction(self.remove_col_action)
        table_menu.addAction(self.add_row_action)
        table_menu.addAction(self.remove_row_action)

        file_menu = QMenu("&Допомога", self)
        menubar.addMenu(file_menu)
        file_menu.addAction(self.about_action)
        file_menu.addAction(self.help_action)

    def on_about(self):
        QMessageBox.information(
            self,
            "Про програму",
            f"Версія: невизначена\n"
            f"Розроблено: Джоном Доу\n"
            f"Вихідний код: https://github.com/iterlace/oop_lab_1_excel",
        )

    def on_help(self):
        QMessageBox.information(
            self,
            "Допомога",
            f"Доступні типи даних, оператори та функції:\n"
            f" - Типи даних: integer and float\n"
            f" - Інфіксні бінарні оператори: 1+1, 1-1, 1*1, 1/1\n"
            f" - Префіксні унарні оператори: ++1, --1\n"
            f" - Вираз НЕ: !1\n"
            f" - Порівняння: 1<1, 1>1, 1=1\n"
            f" - Дужки: (1+1)\n"
            f" - Посилання на клітинки: F11, E9\n"
            f" - Функції: max(1, 2), min(5, 1)",
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = MainWindow()
    table.show()
    sys.exit(app.exec())
