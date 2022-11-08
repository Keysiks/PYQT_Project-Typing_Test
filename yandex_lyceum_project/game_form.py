import sys
import random
import sqlite3

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon, QTextCursor, QTextCharFormat, QFont, QPen, QColor
from save_session import Save_session
from result_form import Result_form


class Game_form(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi('game_form.ui', self)
        self.parent = parent
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
        self.text_field.setEnabled(False)
        self.symbols_count = 0
        self.connection = sqlite3.connect("for_typing_test.bd")
        self.cursor = self.connection.cursor()
        self.time_count = 0
        self.area_for_typing.document().contentsChange.connect(self.contents_change)
        self.format = QTextCharFormat()
        self.wrong_symbols = 0
        self.format = QTextCharFormat()
        self.format.setFont(QFont("Arial", 22, QFont.Bold))
        self.area_for_typing.setEnabled(False)

    def form_text(self):
        try:
            self.words_count = int(self.count_group.checkedButton().text())
            self.language = self.language_group.checkedButton().text()
            self.res = self.new_text()
            self.symbols = len(" ".join(self.res))
            self.text_field.setText(' '.join(self.res))
        except AttributeError:
            self.error_label.setText('Заполните поля')
            timer = QTimer()
            timer.start(3000)
            timer.timeout.connect(lambda: self.error_label.setText(""))

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
        self.timer = QTimer()
        self.form_text_button.setEnabled(False)
        self.start_button.setEnabled(False)
        self.area_for_typing.setEnabled(True)
        self.timer.timeout.connect(self.counter)
        self.timer.start(1000)
        self.seconds = "00"
        self.minutes = "01"

    def counter(self):
        if self.minutes == "00" and self.seconds == "00":
            self.end()
            return
        elif self.minutes == "01":
            self.minutes = "00"
            self.seconds = "59"
            self.time_count += 1
        else:
            self.seconds = int(self.seconds) - 1
            self.seconds = str(self.seconds)
            if len(self.seconds) == 1:
                self.seconds = "0" + self.seconds
            self.time_count += 1
        self.timer_label.setText(f"{self.minutes}:{self.seconds}")

    def reset_timer(self):
        del self.timer
        self.minutes = "01"
        self.seconds = "00"
        self.timer_label.setText(f"{self.minutes}:{self.seconds}")
        self.start_button.setEnabled(True)
        self.form_text_button.setEnabled(True)

    def contents_change(self, position):
        if len(self.area_for_typing.toPlainText()) == 0:
            return
        cursor = self.text_field.textCursor()
        cursor.setPosition(position)
        end = cursor.movePosition(QTextCursor.NextCharacter, 1)  # передвигает курсор на 1 позицию вправо
        self.text = self.text_field.toPlainText()
        try:
            if end:
                letter_text = self.text[position]
                letter_area_for_typing = self.area_for_typing.toPlainText()[position]
                if letter_text == letter_area_for_typing:
                    self.format.setTextOutline(QPen(QColor("#32CD32")))
                    self.symbols_count += 1
                else:
                    self.format.setTextOutline(QPen(QColor("red")))
                    self.wrong_symbols += 1
            else:
                self.end()
        except:
            pass
        cursor.mergeCharFormat(self.format)

    def end(self):
        self.minutes = "01"
        self.seconds = "00"
        self.timer_label.setText(f"{self.minutes}:{self.seconds}")
        self.form_text_button.setEnabled(True)
        self.start_button.setEnabled(True)
        del self.timer
        self.result = round(self.symbols_count / self.time_count * 60)
        self.accuracy = round((self.symbols_count - self.wrong_symbols) / self.symbols_count) * 100
        self.time_count = 0
        self.symbols_count = 0
        self.wrong_symbols = 0
        self.result_form = Result_form(self.result, self.accuracy)
        self.result_form.show()
        player_res = self.cursor.execute(
            f"""SELECT * FROM results WHERE user_name='{self.session.check_session().split()[0]}'""").fetchone()
        if self.language == "Ru":
            print(self.result)
            print(self.accuracy)
            if self.result > int(player_res[1]):
                print(player_res[1], "true")
                self.cursor.execute(
                    f"""UPDATE results SET ru_result = {self.result} 
                               WHERE user_name='{self.session.check_session().split()[0]}'""")

        else:
            if self.result > int(player_res[2]):
                self.cursor.execute(
                    f"""UPDATE results SET eng_result = {self.result} 
                               WHERE user_name='{self.session.check_session().split()[0]}'""")
        print(self.cursor.execute(
            f"""SELECT * FROM results WHERE user_name='{self.session.check_session().split()[0]}'""").fetchone())
        self.area_for_typing.setText("")
        self.area_for_typing.setEnabled(False)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game_form()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
