from PySide6.QtCore import Qt, QModelIndex, QIODevice, QUrl,QDir,QStringListModel
from PySide6.QtWidgets import QWidget,QFileSystemModel
from PySide6.QtGui import QStandardItemModel,QStandardItem
from ui_widget import Ui_Widget
from tablemodel import TableModel

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Custom TableModel")

        self.model = TableModel()
        self.tableView.setModel(self.model)