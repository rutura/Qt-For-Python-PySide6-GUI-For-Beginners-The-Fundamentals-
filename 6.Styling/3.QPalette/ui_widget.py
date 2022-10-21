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
        Widget.resize(432, 189)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.the_sky_label = QLabel(Widget)
        self.the_sky_label.setObjectName(u"the_sky_label")
        font = QFont()
        font.setPointSize(24)
        self.the_sky_label.setFont(font)

        self.verticalLayout.addWidget(self.the_sky_label)

        self.is_label = QLabel(Widget)
        self.is_label.setObjectName(u"is_label")
        self.is_label.setFont(font)

        self.verticalLayout.addWidget(self.is_label)

        self.blue_label = QLabel(Widget)
        self.blue_label.setObjectName(u"blue_label")
        self.blue_label.setFont(font)

        self.verticalLayout.addWidget(self.blue_label)

        self.button = QPushButton(Widget)
        self.button.setObjectName(u"button")

        self.verticalLayout.addWidget(self.button)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.the_sky_label.setText(QCoreApplication.translate("Widget", u"The sky", None))
        self.is_label.setText(QCoreApplication.translate("Widget", u"is", None))
        self.blue_label.setText(QCoreApplication.translate("Widget", u"blue", None))
        self.button.setText(QCoreApplication.translate("Widget", u"Click", None))
    # retranslateUi

