from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

import paths


class Result_form(QMainWindow):
    def __init__(self, result, accuracy):
        super().__init__()
        uic.loadUi(paths.ui("result_window.ui"), self)
        self.setWindowTitle("Результаты")
        self.result_label.setText(f"{result} знаков в минуту")
        self.accuracy_label.setText(f"{accuracy} %")
