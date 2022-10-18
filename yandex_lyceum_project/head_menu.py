import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton, QWidget
from about_programm import About_Programm
from enter_form import Enter_form, ENTER_SYSTEM


class Head_Menu(QMainWindow):
    def __init__(self):
        self.connection = sqlite3.connect("for_typing_test.bd")
        self.cursor = self.connection.cursor()
        super(Head_Menu, self).__init__()
        uic.loadUi('head_menu.ui', self)
        self.button_about_programm.clicked.connect(self.show_text_about_programm)
        self.button_come_in.clicked.connect(self.button_come_in_push)

    def show_text_about_programm(self):
        self.about_programm = About_Programm()
        self.about_programm.show()

    def button_come_in_push(self):
        self.enter_form = Enter_form()
        self.enter_form.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Head_Menu()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())