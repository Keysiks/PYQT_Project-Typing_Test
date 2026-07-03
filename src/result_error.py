from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

import paths


class Result_error(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(paths.ui("result_error_window.ui"), self)
        self.setWindowTitle("Ошибка")
        self.error_label.setText("Войдите, чтобы увидеть результаты")
