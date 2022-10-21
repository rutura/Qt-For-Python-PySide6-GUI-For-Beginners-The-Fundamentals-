from PySide6.QtCore import Qt, QTextStream, QFile, QIODevice, QByteArray, QUrl
from PySide6.QtWidgets import QWidget , QFileDialog, QMessageBox
from PySide6.QtNetwork import QNetworkAccessManager,QNetworkRequest, QNetworkReply
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QNetworkAccessManager")

        self.manager = QNetworkAccessManager(self)
        self.m_data_buffer = QByteArray()   #The buffer where you'll be the data you get from the network
        self.request = QNetworkRequest()
        #self.request.setUrl(QUrl("https://www.qt.io"))
        #self.request.setUrl(QUrl("https://www.github.com"))
        self.request.setUrl(QUrl("https://twitter.com"))

        self.net_reply = self.manager.get(self.request)

        self.net_reply.readyRead.connect(self.data_ready_to_read)
        self.net_reply.finished.connect(self.data_read_finished)

    def data_ready_to_read(self):
        print("Some data available")
        self.m_data_buffer.append(self.net_reply.readAll())


    def data_read_finished(self):
        print("Data read finished")
        if(self.net_reply.error()):
            print("Some error occured")
        else:
            self.textEdit.setText(str(self.m_data_buffer))