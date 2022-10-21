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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(400, 85)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.text_color_button = QPushButton(Widget)
        self.text_color_button.setObjectName(u"text_color_button")

        self.horizontalLayout.addWidget(self.text_color_button)

        self.background_color_button = QPushButton(Widget)
        self.background_color_button.setObjectName(u"background_color_button")

        self.horizontalLayout.addWidget(self.background_color_button)

        self.font_button = QPushButton(Widget)
        self.font_button.setObjectName(u"font_button")

        self.horizontalLayout.addWidget(self.font_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.text_color_button.setText(QCoreApplication.translate("Widget", u"Text Color", None))
        self.background_color_button.setText(QCoreApplication.translate("Widget", u"Background Color", None))
        self.font_button.setText(QCoreApplication.translate("Widget", u"Font", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Some text", None))
    # retranslateUi

