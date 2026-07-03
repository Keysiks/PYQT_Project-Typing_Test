import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

import paths
from save_session import Save_session


class Best_Results(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(paths.ui("results.ui"), self)
        self.setWindowTitle('Лучшие результаты')
        self.connection = sqlite3.connect(paths.DB_PATH)
        self.cursor = self.connection.cursor()
        self.session = Save_session()

    def showEvent(self, event):
        user_name = self.session.check_session().split()[0]
        results = self.cursor.execute(
            "SELECT * FROM results WHERE user_name=?", (user_name,)).fetchone()
        self.ru_res.setText(f"{results[1]} знаков в минуту")
        self.eng_res.setText(f"{results[2]} знаков в минуту")
        super().showEvent(event)
