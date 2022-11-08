import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton


class Result_form(QMainWindow):
    def __init__(self, result, accuracy):
        super().__init__()
        uic.loadUi('result_window.ui', self)
        self.result_label.setText(f"{result} знаков в минуту")
        self.accuracy_label.setText(f"{accuracy} %")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Result_form()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())