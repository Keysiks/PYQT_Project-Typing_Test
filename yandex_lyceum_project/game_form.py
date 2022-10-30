import sys
import pymorphy2
import datetime

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton
from PyQt5.QtCore import QTimer


class Game_form(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi('game_form.ui', self)
        self.parent = parent
        self.timer = QTimer()
        self.exit_button.clicked.connect(self.exit_from_game)
        self.form_text_button.clicked.connect(self.form_text)

    def exit_from_game(self):
        self.parent.game_form.close()

    def form_text(self):
        try:
            self.words_count = int(self.count_group.checkedButton().text())
            self.language = self.language_group.checkedButton().text()
        except AttributeError:
            self.error_label.setText('Заполните поля')
            self.timer.start(3000)
            self.timer.timeout.connect(lambda: self.error_label.setText(""))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game_form()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())