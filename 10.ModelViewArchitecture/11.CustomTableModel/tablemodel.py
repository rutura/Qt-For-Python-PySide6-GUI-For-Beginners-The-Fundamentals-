from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kwargs):
        super(TableModel, self).__init__(*args, **kwargs)

    def data(self, index, role): #Give me the data at index under a given role
        if role == Qt.DisplayRole:
            value = " [ Row : " + str(index.row() + 1) + ", Column : " + str(index.column() + 1)
            return value

    def rowCount(self, parent) : # How many rows do we have under index as parent
        return 2

    def columnCount(self, parent) :#How many columns do we have under index as parent
        return 3