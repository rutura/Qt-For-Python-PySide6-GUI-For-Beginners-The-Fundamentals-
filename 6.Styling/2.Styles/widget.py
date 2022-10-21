from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Styles")


    def button_clicked(self):
        print("Hello")