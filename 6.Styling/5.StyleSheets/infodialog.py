from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from ui_infodialog import Ui_InfoDialog

class InfoDialog(QDialog, Ui_InfoDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Provide your info")

        #Set stylesheet on container widget : Infodialog
        #self.setStyleSheet("QPushButton{color : red ; background-color : white;}")

        #Fields
        self.position = ""
        self.favorite_os = ""

        #Connections
        self.ok_button.clicked.connect(self.ok)
        self.cancel_button.clicked.connect(self.cancel)

        #Set stylesheet on a specific widget 
        self.cancel_button.setStyleSheet("QPushButton{color : red ; background-color : white;}")


    def ok(self):
        if(not(self.position_line_edit.text()=='')):
            self.position = self.position_line_edit.text()
        self.favorite_os = self.favorite_os_combo_box.currentText()
        self.accept()
    def cancel(self):
        self.reject()