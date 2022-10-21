from PySide6 import QtCore
from PySide6.QtCore import Qt,QModelIndex,QAbstractItemModel
from PySide6.QtGui import QColor

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, *args):
        super(TableModel, self).__init__(*args)

        self.table = [
            ["John","Doe","32","Farmer","Single","Gounduana","red"],
            ["Mary","Jane","27","Teacher","Married","Verkso","green"],
            ["John","Doe","32","Farmer","Single","Gounduana","blue"],
            ["Mary","Jane","27","Teacher","Married","Verkso","yellow"]
        ]

    def data(self, index, role):
        if(role == Qt.DisplayRole or role == Qt.EditRole) : 
            return  self.table[index.row()] [index.column()]
        #Target th favorite color column
        elif ((role == Qt.DecorationRole) and (index.column() == 6)) :
            return QColor(self.table[index.row()][index.column()])

    def rowCount(self, index:QModelIndex):
        if(not(index.isValid())):
            return len(self.table)
        return 0

    def columnCount(self,index) :
        if(not(index.isValid())):
            return len(self.table[0])


    def headerData(self, section, orientation, role) :
        if(orientation == Qt.Horizontal and role == Qt.DisplayRole) : 
            if(section == 0 ) : return "First Name"
            if(section == 1 ) : return "Last Name"
            if(section == 2 ) : return "Age"
            if(section == 3 ) : return "Proffession"
            if(section == 4 ) : return "Marital Status"
            if(section == 5 ) : return "Country"
            if(section == 6 ) : return "Favorite Color"
        return super().headerData(section, orientation, role)


    def setData(self, index, value, role):
        if(not(role == Qt.EditRole)):
            return False
        self.table[index.row()][index.column()] = value
        self.dataChanged.emit(index,index)
        return True


    def flags(self, index) :
        return  Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsEditable