from PySide6.QtCore import Qt, QModelIndex, QIODevice, QByteArray, QUrl, QJsonDocument,QDir
from PySide6.QtWidgets import QWidget , QFileDialog, QMessageBox, QFileSystemModel,QTableWidgetItem
from PySide6.QtGui import QStandardItemModel,QStandardItem
from PySide6.QtNetwork import QNetworkAccessManager,QNetworkRequest, QNetworkReply
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QTableWidget")

        #Signal slot connections
        self.list_items_button.clicked.connect(self.list_items)
        self.set_item_button.clicked.connect(self.set_item)

    def list_items(self):
       rows = self.tableWidget.rowCount()
       columns = self.tableWidget.columnCount()
       for r in range(rows): 
            for c in range(columns):
                item = self.tableWidget.item(r,c)
                if(item):
                    data = item.data(Qt.DisplayRole)
                    print(data)
                else:
                    print("No data")


    def set_item(self):
        #Expand the table : new row and new column at the end
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        self.tableWidget.insertColumn(self.tableWidget.columnCount())

        #Set item at the end
        item = QTableWidgetItem("Hello")
        self.tableWidget.setItem(self.tableWidget.rowCount()-1,self.tableWidget.columnCount()-1,item)

