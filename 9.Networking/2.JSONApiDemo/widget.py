from PySide6.QtCore import Qt, QTextStream, QFile, QIODevice, QByteArray, QUrl, QJsonDocument,QJsonArray
from PySide6.QtWidgets import QWidget , QFileDialog, QMessageBox
from PySide6.QtNetwork import QNetworkAccessManager,QNetworkRequest, QNetworkReply
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("JSON API Demo")


        self.net_manager = QNetworkAccessManager(self)
        self.m_data_buffer = QByteArray()
        self.request = QNetworkRequest()
        self.request.setUrl(QUrl("https://jsonplaceholder.typicode.com/posts"))

        #The download is triggered when we click on the button
        self.fetch_button.clicked.connect(self.fetch_button_clicked)

    def fetch_button_clicked(self):
        #Supprised that we can do this in python. Declare class members in a method!!!
        self.net_reply = self.net_manager.get(self.request)
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
            doc = QJsonDocument.fromJson(self.m_data_buffer)
            array = QJsonArray(doc.array())
            for i in range(array.count()):
                object = array.at(i).toObject()
                text = "[" +str(i) + "] :"+ str(object["title"])
                self.listWidget.addItem(text)