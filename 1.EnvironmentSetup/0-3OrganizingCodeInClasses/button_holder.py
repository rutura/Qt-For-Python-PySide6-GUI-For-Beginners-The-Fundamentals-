from PySide6.QtWidgets import QMainWindow, QPushButton 

class ButtonHolder(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press Me!")

        #Set up the button as our central widget
        self.setCentralWidget(button)