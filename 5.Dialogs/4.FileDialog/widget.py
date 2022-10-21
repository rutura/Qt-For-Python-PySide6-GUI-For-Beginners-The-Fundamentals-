from fileinput import filename
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,QFileDialog
from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("User data")

        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        #getExistingDirectory
        """
        dir = QFileDialog.getExistingDirectory(self, "Open directory",
                                                      "/home",
                                                QFileDialog.ShowDirsOnly| QFileDialog.DontResolveSymlinks)
        print("Chosen dir : ",dir)       
        
        """

        #getOpenFileName  
        """
        file_name,_ = QFileDialog.getOpenFileName(self, "Open File",
                                                      "/home",
                                                      "Images (*.png *.xpm *.jpg);;All files(*.*)")
        print("Your chosen file is : ",  file_name)          
        """   

        #getOpenFileNames
        """
        file_names,_ = QFileDialog.getOpenFileNames(self, "Open File",
                                                      "/home",
                                                      "Images (*.png *.xpm *.jpg);;All files(*.*)")
        for f in file_names:
            print(f)           
        """

        #getSaveFileName
        file_name,_ = QFileDialog.getSaveFileName(self, "Save File",
                                 "/home/jana/untitled.png",
                                 "Images (*.png *.xpm *.jpg);;All files(*.*)")
        print(file_name)

