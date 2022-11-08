import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton


class Result_error(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('result_error_window.ui', self)
        self.setWindowTitle("Ошибка")
        self.error_label.setText("Войдите, чтобы увидеть результаты")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Result_error()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())