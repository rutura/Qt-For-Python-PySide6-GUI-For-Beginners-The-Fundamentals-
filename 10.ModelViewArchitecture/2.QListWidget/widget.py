from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget , QFileDialog, QMessageBox, QFileSystemModel,QListWidgetItem
from PySide6.QtGui import QStandardItemModel,QStandardItem
from PySide6.QtNetwork import QNetworkAccessManager,QNetworkRequest, QNetworkReply
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QListWidget")

        #Signal slot connections
        self.list_items_button.clicked.connect(self.list_items)
        self.add_item_button.clicked.connect(self.add_items)

    def list_items(self):
       for i in range(self.listWidget.count()):
            item =self.listWidget.item(i)
            data = item.data(Qt.DisplayRole)
            print(data)

    def add_items(self):
        self.listWidget.addItem(QListWidgetItem("Hello"))