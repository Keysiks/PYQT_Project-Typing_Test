import os
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer

import paths
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
        uic.loadUi(paths.ui("head_menu.ui"), self)
        if not os.path.exists(paths.SESSION_FILE):
            with open(paths.SESSION_FILE, "w") as f:
                f.write('')
        self.connection = sqlite3.connect(paths.DB_PATH)
        self.cursor = self.connection.cursor()
        self._init_db()
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

    def _init_db(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                user_name TEXT PRIMARY KEY,
                password_hash TEXT NOT NULL,
                salt BLOB NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS results(
                user_name TEXT PRIMARY KEY,
                ru_result INT DEFAULT 0,
                eng_result INT DEFAULT 0,
                FOREIGN KEY(user_name) REFERENCES users(user_name)
            )
        """)
        self.connection.commit()

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
            self.game_form = Game_form(self)
            self.game_form.show()
            self.close()

    def show_results(self):
        if self.ENTER_SYSTEM is False:
            self.timer.start(3000)
            self.result_error = Result_error()
            self.result_error.show()
            self.timer.timeout.connect(lambda: self.result_error.close())
        else:
            self.best_results.show()
