import sys

from PySide6 import QtWidgets
from widget import Widget

app = QtWidgets.QApplication(sys.argv)

# Open the css styles file and read in the css-alike styling code
with open('styles/style.css', 'r') as f:
    style = f.read()
    # Set the stylesheet of the application
    app.setStyleSheet(style)

window = Widget()
window.show()

app.exec()