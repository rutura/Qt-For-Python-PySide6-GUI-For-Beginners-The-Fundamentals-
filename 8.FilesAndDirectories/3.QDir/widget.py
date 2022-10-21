from PySide6.QtCore import Qt, QTextStream, QFile, QIODevice, QDir,QFileInfo
from PySide6.QtWidgets import QWidget , QFileDialog, QMessageBox
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QDir Demo")


        #Make the connections
        self.choose_dir_button.clicked.connect(self.choose_dir_button_clicked)
        self.create_dir_button.clicked.connect(self.create_dir_button_clicked)
        self.dir_exists_button.clicked.connect(self.dir_exists_button_clicked)
        self.dir_or_file_button.clicked.connect(self.dir_or_file_button_clicked)
        self.folder_content_button.clicked.connect(self.folder_content_button_clicked)


    def choose_dir_button_clicked(self):
        dir_name= QFileDialog.getExistingDirectory(self, "Choose Folder")
        if((dir_name == "")):
            return
        print("file :",dir_name)
        self.lineEdit.setText(dir_name)

    def create_dir_button_clicked(self):
        #Create a dir if it doesn't exist already
        dir_path = self.lineEdit.text()
        if( (dir_path == "")):
            return
        dir = QDir(dir_path)
        if( not(dir.exists())):
            #Create it
            if(dir.mkpath(dir_path)):
                QMessageBox.information(self,"Message","Directory created")
        else:
            QMessageBox.information(self,"Message","Directory already exists")


    def dir_exists_button_clicked(self):
        #Check if a directory exists
        dir_path = self.lineEdit.text()
        if( (dir_path == "")):
            return

        dir = QDir(dir_path)
        if( dir.exists()):
            QMessageBox.information(self,"Message","Directory exists")
        else:
            QMessageBox.information(self,"Message","Directory doesn't exist")


    def folder_content_button_clicked(self):
        self.listWidget.clear()
        dir_path = self.lineEdit.text()
        if( (dir_path == "")):
            return
        dir = QDir(dir_path)
        file_list = dir.entryInfoList()
        for i in range(len(file_list)):
            file_info = QFileInfo(file_list[i])
            self.listWidget.addItem(file_info.absoluteFilePath())

    def dir_or_file_button_clicked(self):
        file_info = QFileInfo(self.listWidget.currentItem().text())
        if( file_info.isDir()):
            QMessageBox.information(self,"Message","This a Dir")
        elif( file_info.isFile()):
            QMessageBox.information(self,"Message","This a File")
        else:
            QMessageBox.information(self,"Message","Something else")
