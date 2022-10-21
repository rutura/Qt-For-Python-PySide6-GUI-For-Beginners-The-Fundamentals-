from PySide6.QtWidgets import QWidget,QFontDialog,QColorDialog
from PySide6.QtGui import QFont, QPalette
from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QFontDialog Demo")
        self.label.setAutoFillBackground(True)  #Important for the colors to show up

        #Make the connections
        self.text_color_button.clicked.connect(self.text_color_button_clicked)
        self.background_color_button.clicked.connect(self.background_color_button_clicked)
        self.font_button.clicked.connect(self.set_font)

    def text_color_button_clicked(self):
        palette = self.label.palette()
        color = palette.color(QPalette.WindowText)
        chosenColor = QColorDialog.getColor(color,self,"Choose text color")

        if(chosenColor.isValid()):
            palette.setColor(QPalette.WindowText,chosenColor)
            self.label.setPalette(palette)
        else:
            print("User chose a bad text color")


    def background_color_button_clicked(self):
        palette = self.label.palette()
        color = palette.color(QPalette.Window)
        chosenColor = QColorDialog.getColor(color,self,"Choose background color")

        if(chosenColor.isValid()):
            palette.setColor(QPalette.Window,chosenColor)
            self.label.setPalette(palette)
        else:
            print("User chose a bad background color")


    def set_font(self):
    
        ok,font = QFontDialog.getFont(QFont("Helvetica [Cronyx]", 20),self)
        if ok:
            self.label.setFont(font)
        else:
            print("User didn't select any valid font")  