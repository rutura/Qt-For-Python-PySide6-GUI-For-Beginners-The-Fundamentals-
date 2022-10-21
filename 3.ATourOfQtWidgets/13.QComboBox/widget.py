from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QComboBox, QPushButton, QLabel, QLineEdit,QSpacerItem

class Widget(QWidget):
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("QComboBox Demo")


        self.combo_box = QComboBox(self)
        #Add planets to the combobox
        self.combo_box.addItem("Earth")
        self.combo_box.addItem("Venus")
        self.combo_box.addItem("Mars")
        self.combo_box.addItem("Pluton")
        self.combo_box.addItem("Saturn")

        button_current_value = QPushButton("Current Value")
        button_current_value.clicked.connect(self.current_value)
        button_set_current = QPushButton("Set value")
        button_set_current.clicked.connect(self.set_current)
        button_get_values = QPushButton("Get values")
        button_get_values.clicked.connect(self.get_values)


        v_layout = QVBoxLayout()
        v_layout.addWidget(self.combo_box)
        v_layout.addWidget(button_current_value)
        v_layout.addWidget(button_set_current)
        v_layout.addWidget(button_get_values)
    
        self.setLayout(v_layout)

    def current_value(self):
        print("Current item : ", self.combo_box.currentText(),
                " - current index : ", self.combo_box.currentIndex())
    def set_current(self):
        self.combo_box.setCurrentIndex(2)
    def get_values(self):
        for i in range(self.combo_box.count()):
            print ("index [ ", i , "] : ", self.combo_box.itemText(i))