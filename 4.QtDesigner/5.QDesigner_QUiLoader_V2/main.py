import sys

from PySide6 import QtWidgets
from user_interface import UserInterface

app = QtWidgets.QApplication(sys.argv)

window = UserInterface()
window.show()

app.exec()