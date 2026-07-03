import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer

import paths
from save_session import Save_session
from password_utils import verify_password


class Enter_form(QMainWindow):
    def __init__(self, button_begin, parent):
        super(Enter_form, self).__init__()
        uic.loadUi(paths.ui("enter_form.ui"), self)
        self.connection = sqlite3.connect(paths.DB_PATH)
        self.setWindowTitle("Войти")
        self.cursor = self.connection.cursor()
        self.timer = QTimer()
        self.button_begin = button_begin
        self.parent = parent
        self.session = Save_session()
        self.res = self.session.check_session()
        if self.res is not False:
            self.login_line.setText(self.res)
        self.enter_button.clicked.connect(self.check_enter)

    def check_enter(self):
        login = self.login_line.text()
        password = self.password_line.text()
        res = self.cursor.execute("SELECT password_hash, salt FROM users WHERE user_name=?", (login,)).fetchone()
        if res is None:
            self.error_label.setText("Неверный логин")
        else:
            stored_hash, salt = res
            salt_bytes = bytes.fromhex(salt) if isinstance(salt, str) else salt
            if verify_password(password, stored_hash, salt_bytes):
                self.error_label.setText("Вы вошли! Закройте окно и продолжайте игру.")
                self.timer.start(1000)
                self.timer.timeout.connect(lambda: self.close())
                self.button_begin.show()
                self.parent.ENTER_SYSTEM = True
                self.session.save_session(login)
            else:
                self.error_label.setText("Вы ввели неверный пароль, повторите попытку.")
        self.connection.commit()
