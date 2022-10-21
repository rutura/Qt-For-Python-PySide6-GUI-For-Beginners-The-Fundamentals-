import sys

from PySide6 import QtWidgets
from widget import Widget

app = QtWidgets.QApplication(sys.argv)

#Set stylesheet on entire application
#app.setStyleSheet("QPushButton{color : red ; background-color : white;}")

window = Widget()
window.show()

app.exec()