#VERSION1 : Setting everything up in the global scope
"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first MainWindow App!")

button = QPushButton()
button.setText("Press Me")

window.setCentralWidget(button)

window.show() 
app.exec()

"""


#VERSION2 : Setting up a separate class
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton 

class ButtonHolder(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press Me!")

        #Set up the button as our central widget
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = ButtonHolder()
window.show() 
app.exec()
"""


import sys
from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder
app = QApplication(sys.argv)

window = ButtonHolder()
window.show() 
app.exec()

