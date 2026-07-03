import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer

import paths
from check_password import Check_password
from save_session import Save_session
from password_utils import hash_password


class Register_form(QMainWindow):
    def __init__(self, parent, button_begin):
        super().__init__()
        self.check_password = Check_password()
        self.button_begin = button_begin
        uic.loadUi(paths.ui("registration_form.ui"), self)
        self.connection = sqlite3.connect(paths.DB_PATH)
        self.cursor = self.connection.cursor()
        self.setWindowTitle("Регистрация")
        self.button_registr.clicked.connect(self.registration)
        self.parent = parent
        self.session = Save_session()

    def registration(self):
        login = self.registr_login.text()
        password1 = self.first_password.text()
        password2 = self.second_password.text()
        self.timer = QTimer()
        res = self.cursor.execute("SELECT * FROM users WHERE user_name=?", (login,)).fetchone()
        check_pass = self.check_password.check_password(password1)
        if password1 != password2:
            self.error_label.setText("Пароли не совпадают, введите заново")
        elif login == '' or password1 == "" or password2 == "":
            self.error_label.setText("Поля не должны быть пустыми")
        elif check_pass != 'ok':
            if check_pass == 'wrong lengh':
                self.error_label.setText("Слишком короткий пароль")
            else:
                self.error_label.setText("Слишком простой пароль")
        elif res is not None:
            self.error_label.setText("Данный ник уже используется")
        else:
            self.error_label.setText("Вы успешно зарегистрованы!")
            password_hash, salt = hash_password(password1)
            self.cursor.execute("INSERT INTO users VALUES(?, ?, ?)", (login, password_hash, salt))
            self.cursor.execute("INSERT INTO results VALUES(?, 0, 0)", (login,))
            self.parent.ENTER_SYSTEM = True
            self.timer.start(1000)
            self.timer.timeout.connect(lambda: self.close())
            self.button_begin.show()
            self.session.save_session(login)
        self.connection.commit()
