from PySide6.QtCore import Qt, QModelIndex, QIODevice, QByteArray, QUrl, QJsonDocument,QDir
from PySide6.QtWidgets import QWidget , QFileDialog, QMessageBox, QFileSystemModel
from PySide6.QtGui import QStandardItemModel,QStandardItem
from PySide6.QtNetwork import QNetworkAccessManager,QNetworkRequest, QNetworkReply
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QFileSystemModel, ListView, TreeView")

        #Using QFileSystemModel
        """
         self.dir_model = QFileSystemModel(self)
        self.dir_model.setFilter( QDir.Dirs | QDir.Files)
        self.dir_model.setRootPath(QDir.currentPath())

        self.treeView.setModel(self.dir_model)
        self.listView.setModel(self.dir_model)        
        """ 

        #QStandardItemModel
        self.standard_model =  QStandardItemModel()
        parent_item = self.standard_model.invisibleRootItem()

        for i in range(4):
            item = QStandardItem("Item :" + str(i))
            parent_item.appendRow(item)
            parent_item = item 

        self.treeView.setModel(self.standard_model)
        self.listView.setModel(self.standard_model)  

        #Make the connections
        self.read_tree_model_data_button.clicked.connect(self.read_data_button_clicked)


    def read_data_button_clicked(self):
        #QFileSystemModel : Reading data
        """
         print("Row count : ", self.dir_model.rowCount(QModelIndex()))
        print("Column count : ", self.dir_model.columnCount(QModelIndex()))
        index = self.dir_model.index(0,0,QModelIndex())
        data = index.data()
        print(data)       
        """


        #QStandardItemModel : Reading data
        print("Row count : ", self.standard_model.rowCount(QModelIndex()))
        print("Column count : ", self.standard_model.columnCount(QModelIndex()))
        index = self.standard_model.index(0,0,QModelIndex())
        data = index.data()
        print(data)        



            