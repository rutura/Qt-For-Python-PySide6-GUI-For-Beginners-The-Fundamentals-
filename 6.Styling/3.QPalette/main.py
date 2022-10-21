import sys

from PySide6.QtWidgets import QApplication, QLabel
from widget import Widget

app = QApplication(sys.argv)

window = Widget()
window.show()

app.exec()