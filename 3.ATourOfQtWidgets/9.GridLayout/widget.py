from PySide6.QtWidgets import QWidget,  QSizePolicy, QGridLayout, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("QGridLayout Demo")


        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")
        button_3.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button_4 = QPushButton("Four")
        button_5 = QPushButton("Five")
        button_6 = QPushButton("Six")
        button_7 = QPushButton("Seven")


        grid_layout = QGridLayout()
        grid_layout.addWidget(button_1,0,0)
        grid_layout.addWidget(button_2,0,1,1,2) #Take up 1 row and 2 columns
        grid_layout.addWidget(button_3,1,0,2,1) #Take up 2 rows and 1 column
        grid_layout.addWidget(button_4,1,1)
        grid_layout.addWidget(button_5,1,2)
        grid_layout.addWidget(button_6,2,1)
        grid_layout.addWidget(button_7,2,2)

        self.setLayout(grid_layout)