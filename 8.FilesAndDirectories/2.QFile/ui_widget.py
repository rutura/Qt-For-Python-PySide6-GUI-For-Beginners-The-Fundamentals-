# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(501, 370)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textEdit = QTextEdit(Widget)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_3.addWidget(self.textEdit)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.write_button = QPushButton(Widget)
        self.write_button.setObjectName(u"write_button")

        self.verticalLayout.addWidget(self.write_button)

        self.read_button = QPushButton(Widget)
        self.read_button.setObjectName(u"read_button")

        self.verticalLayout.addWidget(self.read_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.source_line_edit = QLineEdit(Widget)
        self.source_line_edit.setObjectName(u"source_line_edit")

        self.horizontalLayout.addWidget(self.source_line_edit)

        self.select_file_button = QPushButton(Widget)
        self.select_file_button.setObjectName(u"select_file_button")

        self.horizontalLayout.addWidget(self.select_file_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dest_line_edit = QLineEdit(Widget)
        self.dest_line_edit.setObjectName(u"dest_line_edit")

        self.horizontalLayout_2.addWidget(self.dest_line_edit)

        self.copy_file_button = QPushButton(Widget)
        self.copy_file_button.setObjectName(u"copy_file_button")

        self.horizontalLayout_2.addWidget(self.copy_file_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.write_button.setText(QCoreApplication.translate("Widget", u"Write", None))
        self.read_button.setText(QCoreApplication.translate("Widget", u"Read", None))
        self.select_file_button.setText(QCoreApplication.translate("Widget", u"Select File", None))
        self.copy_file_button.setText(QCoreApplication.translate("Widget", u"Copy", None))
    # retranslateUi

