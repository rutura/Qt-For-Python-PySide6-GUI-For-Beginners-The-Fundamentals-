from PySide6.QtWidgets import QWidget,QInputDialog,QLineEdit
from PySide6.QtCore import QDir
from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QInputDialog Demo")

        #Make the connections
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        #Get text
        """
        text, ok = QInputDialog.getText(self, "getText", "Enter your name : ")
        if (ok and not (text=="")) :
            self.value_label.setText(text)        
        """


        #Get double : Value :150 , min : 100, max : 200
        """
         value, ok = QInputDialog.getDouble(self, "Get double", "Select a value : ",150,100,200)
        if (ok) :
            self.value_label.setText(f'{value}')  #The f thing is turning the number into a string       
       
        """


        #Get int : Value :150 , min : 100, max : 200
        """
        value, ok = QInputDialog.getInt(self, "Get int", "Select a value : ",150,100,200)
        if (ok) :
            self.value_label.setText(f'{value}')     #The f thing is turning the number into a string          

        """

        #GetItem
        items = ["Spring","Summer","Fall","Winter"]
        item,ok = QInputDialog.getItem(self, "QInputDialog.getItem()","Season:", items)
        if (ok):
            self.value_label.setText(item)
