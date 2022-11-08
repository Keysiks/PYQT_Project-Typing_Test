import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from save_session import Save_session


class Best_Results(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('results.ui', self)
        self.connection = sqlite3.connect("for_typing_test.bd")
        self.cursor = self.connection.cursor()
        self.session = Save_session()
        results = self.cursor.execute(
            f"""SELECT * FROM results WHERE user_name='{self.session.check_session().split()[0]}'""").fetchone()
        print(results)
        self.ru_res.setText(f"{results[1]} знаков в минуту")
        self.eng_res.setText(f"{results[2]} знаков в минуту")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Best_Results()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
