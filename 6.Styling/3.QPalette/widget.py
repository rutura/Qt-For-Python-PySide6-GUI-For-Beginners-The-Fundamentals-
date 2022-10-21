from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QPalette Demo")

        #Retrieve the global palette. Can also call palette on the application object if available
        palette = QPalette() # palette is a copy

        #Modify the palette with our changes
        palette.setColor(QPalette.Window,Qt.blue)
        palette.setColor(QPalette.WindowText,Qt.red)

        self.the_sky_label.setAutoFillBackground(True)
        #Apply the palette
        self.the_sky_label.setPalette(palette)

        #Grab the palette from another label and use it
        self.blue_label.setAutoFillBackground(True)
        self.blue_label.setPalette(self.the_sky_label.palette())