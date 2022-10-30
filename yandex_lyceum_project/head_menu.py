import sys
import sqlite3
import os

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton, QWidget
from about_programm import About_Programm
from register_form import Register_form
from enter_form import Enter_form
from game_form import Game_form
from save_session import Save_session


class Head_Menu(QMainWindow):
    def __init__(self):
        if not os.path.exists("session_file.txt"):
            with open("session_file.txt", "w") as f:
                f.write('')
        self.connection = sqlite3.connect("for_typing_test.bd")
        self.cursor = self.connection.cursor()
        super(Head_Menu, self).__init__()
        uic.loadUi('head_menu.ui', self)
        self.ENTER_SYSTEM = False
        self.save_session = Save_session()
        self.button_begin.hide()
        self.button_about_programm.clicked.connect(self.show_text_about_programm)
        self.button_come_in.clicked.connect(self.button_come_in_push)
        self.head_button_registr.clicked.connect(self.registr_push)
        self.button_begin.clicked.connect(self.button_begin_push)

    def show_text_about_programm(self):
        self.about_programm = About_Programm()
        self.about_programm.show()

    def button_come_in_push(self):
        self.enter_form = Enter_form(self.button_begin, self)
        self.enter_form.show()

    def registr_push(self):
        self.registr_form = Register_form(self, self.button_begin)
        self.registr_form.show()

    def button_begin_push(self):
        if self.ENTER_SYSTEM is True:
            print("YES")
            self.game_form = Game_form(self)
            self.game_form.show()
            self.close()
        else:
            print("NO")



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Head_Menu()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())