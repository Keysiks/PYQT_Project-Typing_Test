import sys
import sqlite3

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton
from check_password_class import Check_password
from PyQt5.QtCore import QTimer
from save_session import Save_session


class Register_form(QMainWindow):
    def __init__(self, parent, button_begin):
        super().__init__()
        self.check_password = Check_password()
        self.button_begin = button_begin
        uic.loadUi('regestration_form.ui', self)
        self.connection = sqlite3.connect("for_typing_test.bd")
        self.cursor = self.connection.cursor()
        self.button_registr.clicked.connect(self.registration)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(  
                        user_name TEXT PRIMARY Key,
                        password TEXT);
                        """)
        self.parent = parent
        self.session = Save_session()

    def registration(self):
        login = self.registr_login.text()
        password1 = self.first_password.text()
        password2 = self.second_password.text()
        self.timer = QTimer()
        res = self.cursor.execute(f"""SELECT * FROM users WHERE user_name='{login}';""").fetchone()
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
            self.cursor.execute(f"""INSERT INTO users VALUES(?, ?);""", (login, password1))
            self.parent.ENTER_SYSTEM = True
            self.timer.start(1000)
            self.timer.timeout.connect(lambda: self.close())
            self.button_begin.show()
            self.session.save_session(login, password1)
        self.connection.commit()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Register_form()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())