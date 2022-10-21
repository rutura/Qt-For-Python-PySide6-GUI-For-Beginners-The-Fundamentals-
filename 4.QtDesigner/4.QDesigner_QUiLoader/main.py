import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader() #Set up a loader object

app = QtWidgets.QApplication(sys.argv)
window = loader.load("widget.ui", None) #Load the ui - happens at run time!

def do_something() :
    print(window.full_name_line_edit.text(),"is a ", window.occupation_line_edit.text())

#Changing the properties in the form
window.setWindowTitle("User data")

#Accessing widgets in the form
window.submit_button.clicked.connect(do_something)
window.show()
app.exec()