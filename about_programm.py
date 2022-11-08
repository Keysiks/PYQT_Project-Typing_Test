import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton


class About_Programm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('about_programm.ui', self)
        self.setWindowTitle("О программе")
        self.about_programm_txt = 'Приветствуем вас в приложении "Typing test". \n' \
                                  'Это приложение основано на библиотеке PYQT5. \n' \
                                  'Разрaботчик Редько Кирилл.'
        self.programm_text.setEnabled(False)
        self.programm_text.setText(self.about_programm_txt)
