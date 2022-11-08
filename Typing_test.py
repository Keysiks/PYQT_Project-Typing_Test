import sys
import sqlite3

from PyQt5.QtWidgets import QApplication
from head_menu import Head_Menu


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Head_Menu()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())