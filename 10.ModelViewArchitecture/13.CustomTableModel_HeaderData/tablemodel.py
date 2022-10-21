from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QTime, QTimer
from PySide6.QtGui import QFont,QBrush

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kwargs):
        super(TableModel, self).__init__(*args, **kwargs)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timer_timeout)
        self.timer.start()

    def timer_timeout(self):
        top_left = self.index(0,0)
        self.dataChanged.emit(top_left,top_left)

    def data(self, index, role): #Give me the data at index under a given role
        row = index.row()
        col = index.column()

        if role == Qt.DisplayRole:
            if( row == 0 and col == 1):
                 return "<--left"
            if( row == 1 and col == 1):
                 return "right -->"
            if( row == 0 and col ==0):
                return QTime.currentTime().toString()
            value = " [ Row : " + str(index.row() + 1) + ", Column : " + str(index.column() + 1) +"]"
            return value

        #Font role
        if( role == Qt.FontRole):
            font = QFont()
            font.setBold(True)
            return font

        #Background role
        if(role == Qt.BackgroundRole):
            if( row == 1 and col ==2):
                background = QBrush(Qt.yellow)
                return background

        #TextAlignment role
        if(role == Qt.TextAlignmentRole):
            if( row == 1 and col ==1):
                return Qt.AlignRight #Ignored by PySide6.

    def rowCount(self, parent) : # How many rows do we have under index as parent
        return 2

    def columnCount(self, parent) :#How many columns do we have under index as parent
        return 3


    def headerData(self, section, orientation, role) :
        if( role == Qt.DisplayRole):
            if(orientation == Qt.Horizontal):
                if(section == 0) : return "First"
                if(section == 1) : return "Second"
                if(section == 2) : return "Third"
        return super().headerData(section, orientation, role)