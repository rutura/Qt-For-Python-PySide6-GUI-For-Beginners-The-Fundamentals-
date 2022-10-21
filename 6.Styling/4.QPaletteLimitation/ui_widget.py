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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QGroupBox,
    QLCDNumber, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(295, 398)
        self.verticalLayout_3 = QVBoxLayout(Widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.button = QPushButton(Widget)
        self.button.setObjectName(u"button")

        self.verticalLayout_3.addWidget(self.button)

        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout.addWidget(self.checkBox_3)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton = QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_2.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_2.addWidget(self.radioButton_3)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_3.addWidget(self.lineEdit)

        self.spinBox = QSpinBox(Widget)
        self.spinBox.setObjectName(u"spinBox")

        self.verticalLayout_3.addWidget(self.spinBox)

        self.dateTimeEdit = QDateTimeEdit(Widget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.verticalLayout_3.addWidget(self.dateTimeEdit)

        self.lcdNumber = QLCDNumber(Widget)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout_3.addWidget(self.lcdNumber)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.button.setText(QCoreApplication.translate("Widget", u"Click", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"GroupBox", None))
        self.checkBox.setText(QCoreApplication.translate("Widget", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("Widget", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("Widget", u"CheckBox", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"GroupBox", None))
        self.radioButton.setText(QCoreApplication.translate("Widget", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("Widget", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("Widget", u"RadioButton", None))
    # retranslateUi

