import sys
import random

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from save_session import Save_session


class Game_form(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi('game_form.ui', self)
        self.parent = parent
        self.timer = QTimer()
        self.session = Save_session()
        self.reset_icon = QIcon("reset_icon.png")
        self.button_reset.setIcon(self.reset_icon)
        with open("english_base1.txt", "r", encoding="utf-8") as f:
            self.english_base = f.readlines()
        with open("russian_base.txt", "r", encoding="utf-8") as f:
            self.russian_base = f.readlines()
        self.form_text_button.clicked.connect(self.form_text)
        self.start_button.clicked.connect(self.start_printing)
        self.button_reset.clicked.connect(self.reset_timer)

    def form_text(self):
        try:
            self.words_count = int(self.count_group.checkedButton().text())
            self.language = self.language_group.checkedButton().text()
            self.res = self.new_text()
            self.symbols = len(" ".join(self.res))
            self.text_field.setText(' '.join(self.res))
        except AttributeError:
            self.error_label.setText('Заполните поля')
            self.timer.start(3000)
            self.timer.timeout.connect(lambda: self.error_label.setText(""))

    def new_text(self):
        self.text = []
        if self.language == 'Eng':
            for i in range(self.words_count):
                self.text.append(self.english_base[random.randint(0, 9924)].strip())
        else:
            for i in range(self.words_count):
                self.text.append(self.russian_base[random.randint(0, 10000)].strip())
        return self.text

    def start_printing(self):
        self.form_text_button.setEnabled(False)
        self.start_button.setEnabled(False)
        self.timer.timeout.connect(self.counter)
        self.timer.start(1000)
        self.seconds = '00'
        self.minutes = '01'

    def counter(self):
        if self.minutes == "00" and self.seconds == "00":
            self.minutes = "01"
            self.seconds = "00"
            self.timer_label.setText(f"{self.minutes}:{self.seconds}")
            self.form_text_button.setEnabled(True)
            self.start_button.setEnabled(True)
            return
        elif self.minutes == "01":
            self.minutes = "00"
            self.seconds = "59"
        else:
            self.seconds = int(self.seconds) - 1
            self.seconds = str(self.seconds)
            if len(self.seconds) == 1:
                self.seconds = "0" + self.seconds
        self.timer_label.setText(f"{self.minutes}:{self.seconds}")

    def reset_timer(self):
        pass
    

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game_form()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())

