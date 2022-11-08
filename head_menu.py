import sys
import sqlite3
import os

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton, QWidget
from PyQt5.QtCore import QTimer
from about_programm import About_Programm
from register_form import Register_form
from enter_form import Enter_form
from game_form import Game_form
from save_session import Save_session
from best_results import Best_Results
from result_error import Result_error


class Head_Menu(QMainWindow):
    def __init__(self):
        super(Head_Menu, self).__init__()
        uic.loadUi('head_menu.ui', self)
        if not os.path.exists("session_file.txt"):
            with open("session_file.txt", "w") as f:
                f.write('')
        self.connection = sqlite3.connect("for_typing_test.bd")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS results(  
                user_name TEXT PRIMARY Key,
                ru_result INT,
                eng_result INT);
                """)
        self.setWindowTitle("Главное меню")
        self.ENTER_SYSTEM = False
        self.session = Save_session()
        self.button_begin.hide()
        self.button_about_programm.clicked.connect(self.show_text_about_programm)
        self.button_come_in.clicked.connect(self.button_come_in_push)
        self.head_button_registr.clicked.connect(self.registr_push)
        self.button_begin.clicked.connect(self.button_begin_push)
        self.button_result_list.clicked.connect(self.show_results)
        self.best_results = Best_Results()
        self.timer = QTimer()

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

    def show_results(self):
        if self.ENTER_SYSTEM is False:
            self.timer.start(3000)
            self.result_error = Result_error()
            self.result_error.show()
            self.timer.timeout.connect(lambda: self.result_error.close())
        else:
            self.best_results.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Head_Menu()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
