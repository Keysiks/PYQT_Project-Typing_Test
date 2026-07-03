from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

import paths


class About_Programm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(paths.ui("about_programm.ui"), self)
        self.setWindowTitle("О программе")
        self.about_programm_txt = 'Приветствуем вас в приложении "Typing test". \n' \
                                  'Это приложение основано на библиотеке PYQT5. \n' \
                                  'Разработчик Редько Кирилл.'
        self.programm_text.setEnabled(False)
        self.programm_text.setText(self.about_programm_txt)
