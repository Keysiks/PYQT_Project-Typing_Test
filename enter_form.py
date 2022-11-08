import sys
import sqlite3

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton
from PyQt5.QtCore import QTimer
from save_session import Save_session


class Enter_form(QMainWindow):
    global ENTER_SYSTEM

    def __init__(self, button_begin, parent):
        super(Enter_form, self).__init__()
        uic.loadUi('enter_form.ui', self)
        self.connection = sqlite3.connect("for_typing_test.bd")
        self.setWindowTitle("Войти")
        self.cursor = self.connection.cursor()
        self.timer = QTimer()
        self.button_begin = button_begin
        self.parent = parent
        self.session = Save_session()
        self.res = self.session.check_session()
        print(self.res)
        if self.res is False:
            pass
        else:
            self.login_line.setText(self.res.split()[0])
            self.password_line.setText(self.res.split()[1])
        self.enter_button.clicked.connect(self.check_enter)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(  
                user_name TEXT PRIMARY Key,
                password TEXT);
                """)

    def check_enter(self):
        login = self.login_line.text()
        password = self.password_line.text()
        res = self.cursor.execute(f"""SELECT * FROM users WHERE user_name='{login}';""").fetchone()
        if res is None:
            self.error_label.setText("Неверный логин")
        else:
            if res[1] == password:
                self.error_label.setText("Вы вошли! Закройте окно и продолжайте игру.")
                self.timer.start(1000)
                self.timer.timeout.connect(lambda: self.close())
                self.button_begin.show()
                self.parent.ENTER_SYSTEM = True
                self.session.save_session(login, password)
            else:
                self.error_label.setText("Вы ввели неверный пароль, повторите попытку.")
        self.connection.commit()

    def registr_new_user(self):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Enter_form()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())