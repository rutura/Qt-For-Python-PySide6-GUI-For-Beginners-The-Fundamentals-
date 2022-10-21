from PySide6.QtWidgets import QApplication,QWidget
from rockwidget import RocWidget

import sys
app = QApplication(sys.argv)

window = RocWidget()
window.show()

app.exec()