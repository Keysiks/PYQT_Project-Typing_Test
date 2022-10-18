import sys
import sqlite3

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton

ENTER_SYSTEM = False


class Enter_form(QMainWindow):
    global ENTER_SYSTEM

    def __init__(self):
        self.connection = sqlite3.connect("for_typing_test.bd")
        self.cursor = self.connection.cursor()
        super().__init__()
        uic.loadUi('enter_form.ui', self)
        self.enter_button.clicked.connect(self.check_enter)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(  
                user_name TEXT PRIMARY Key,
                password TEXT);
                """)
        

    def check_enter(self):
        login = self.login_line.text()
        password = self.password_line.text()
        res = self.cursor.execute(f"""SELECT * FROM users WHERE user_name='{login}';""").fetchone()
        if res in None:
            self.error_label.setText("Неверный логин")
        else:
            if res[1] == password:
                self.error_label.setText("Вы вошли! Закройте окно и продолжайте игру.")
                ENTER_SYSTEM = True
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