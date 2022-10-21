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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(400, 114)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.provide_info_button = QPushButton(Widget)
        self.provide_info_button.setObjectName(u"provide_info_button")

        self.verticalLayout.addWidget(self.provide_info_button)

        self.info_label = QLabel(Widget)
        self.info_label.setObjectName(u"info_label")
        font = QFont()
        font.setPointSize(11)
        self.info_label.setFont(font)
        self.info_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.info_label)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.provide_info_button.setText(QCoreApplication.translate("Widget", u"Profide info", None))
        self.info_label.setText(QCoreApplication.translate("Widget", u"Your info", None))
    # retranslateUi

