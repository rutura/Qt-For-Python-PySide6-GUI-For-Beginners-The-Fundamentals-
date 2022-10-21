from PySide6.QtCore import Qt, QModelIndex, QIODevice, QByteArray, QUrl, QJsonDocument,QDir
from PySide6.QtWidgets import QWidget , QFileDialog, QMessageBox, QFileSystemModel,QTreeWidgetItem
from PySide6.QtGui import QStandardItemModel,QStandardItem
from PySide6.QtNetwork import QNetworkAccessManager,QNetworkRequest, QNetworkReply
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QTreeWidget")

        self.treeWidget.setColumnCount(2)

        #Set header data
        self.treeWidget.setHeaderLabels( ["ID","Name"])


        #Add data
        treeItem1 = QTreeWidgetItem(self.treeWidget)
        treeItem1.setText(0, "11")
        treeItem1.setText(1, "Snow")

        treeItem2 = QTreeWidgetItem(self.treeWidget)
        treeItem2.setText(0, "22")
        treeItem2.setText(1, "David")

        treeItem3 = QTreeWidgetItem() # We don't give it an affiliation
        treeItem3.setText(0, "33")
        treeItem3.setText(1, "Steve")

        #Add item3 as a child of item2
        treeItem2.addChild(treeItem3)

        #Signal slot connections
        self.list_items_button.clicked.connect(self.list_items)

    def list_items(self):
        top_level_item_count = self.treeWidget.topLevelItemCount()
        for i in range(top_level_item_count):
            item = self.treeWidget.topLevelItem(i)
            if(item):
                print("ID : ", item.data(0,Qt.DisplayRole)," | Name : ",item.data(1,Qt.DisplayRole))
                child_count = item.childCount()
                if(not(child_count == 0)):
                    for c in range(child_count):
                        child = item.child(c)
                        print("---ID : ", child.data(0,Qt.DisplayRole)," | Name : "
                                ,child.data(1,Qt.DisplayRole))