# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(832, 520)
        Form.setMouseTracking(True)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: #28292c;")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(810, 0, 21, 21))
        font = QFont()
        font.setFamily(u"Adobe Heiti Std R")
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(False)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #1f1f22\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255, 34, 63);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 34, 63);\n"
"	background-color:  #1f1f22\n"
"}")
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(True)
        self.minimize = QPushButton(Form)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setGeometry(QRect(790, 0, 21, 21))
        font1 = QFont()
        font1.setFamily(u"Adobe Heiti Std R")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setKerning(False)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.minimize.setFont(font1)
        self.minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #1f1f22\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(134, 134, 134);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"}")
        self.minimize.setCheckable(False)
        self.minimize.setChecked(False)
        self.minimize.setAutoRepeat(False)
        self.minimize.setAutoExclusive(False)
        self.minimize.setAutoDefault(False)
        self.minimize.setFlat(True)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 20, 241, 501))
        self.frame.setStyleSheet(u"background-color: #1f1f22")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(15, 0, 221, 61))
        font2 = QFont()
        font2.setPointSize(26)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(149, 149, 149)")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 110, 191, 33))
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	margin-right: auto;\n"
"	color: rgb(149, 149, 149)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	outline:none;\n"
"	padding: 5px;\n"
"	margin-left: auto;\n"
"	color:rgb(212, 212, 212)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	outline:none;\n"
"	padding: 5px;\n"
"	margin-right: auto;\n"
"	color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	border: none;\n"
"	outline:none;\n"
"	padding: 5px;\n"
"	margin-right: auto;\n"
"	color:rgb(255, 255, 255)\n"
"}")
        self.pushButton_2.setInputMethodHints(Qt.ImhNone)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(2, 142, 199, 33))
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	margin-right: auto;\n"
"	color: rgb(149, 149, 149)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	outline:none;\n"
"	padding: 5px;\n"
"	margin-left: auto;\n"
"	color:rgb(212, 212, 212)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	outline:none;\n"
"	padding: 5px;\n"
"	margin-right: auto;\n"
"	color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	border: none;\n"
"	outline:none;\n"
"	padding: 5px;\n"
"	margin-right: auto;\n"
"	color:rgb(255, 255, 255)\n"
"}")
        self.pushButton_3.setInputMethodHints(Qt.ImhNone)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(-26, 172, 211, 33))
        self.pushButton_4.setFont(font3)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	margin-right: auto;\n"
"	color: rgb(149, 149, 149)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	outline:none;\n"
"	padding: 5px;\n"
"	margin-left: auto;\n"
"	color:rgb(212, 212, 212)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	outline:none;\n"
"	padding: 5px;\n"
"	margin-right: auto;\n"
"	color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	border: none;\n"
"	outline:none;\n"
"	padding: 5px;\n"
"	margin-right: auto;\n"
"	color:rgb(255, 255, 255)\n"
"}")
        self.pushButton_4.setInputMethodHints(Qt.ImhNone)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(-18, 200, 199, 39))
        self.pushButton_5.setFont(font3)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	margin-right: auto;\n"
"	color: rgb(149, 149, 149)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	outline:none;\n"
"	padding: 5px;\n"
"	margin-left: auto;\n"
"	color:rgb(212, 212, 212)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	outline:none;\n"
"	padding: 5px;\n"
"	margin-right: auto;\n"
"	color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	border: none;\n"
"	outline:none;\n"
"	padding: 5px;\n"
"	margin-right: auto;\n"
"	color:rgb(255, 255, 255)\n"
"}")
        self.pushButton_5.setInputMethodHints(Qt.ImhNone)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setChecked(False)
        self.pushButton_5.setFlat(True)
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 841, 21))
        self.frame_2.setStyleSheet(u"background-color: #1f1f22")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.frame_2.setLineWidth(0)
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(240, 20, 591, 501))
        self.frame_3.setStyleSheet(u"background-color: #2b2b31")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Sunken)
        self.frame_3.setLineWidth(0)
        self.frame_2.raise_()
        self.minimize.raise_()
        self.pushButton.raise_()
        self.frame.raise_()
        self.frame_3.raise_()
        QWidget.setTabOrder(self.pushButton, self.minimize)

        self.retranslateUi(Form)

        self.pushButton.setDefault(False)
        self.minimize.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"X", None))
        self.minimize.setText(QCoreApplication.translate("Form", u"-", None))
        self.label.setText(QCoreApplication.translate("Form", u"MineRunner", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043d\u0441\u043e\u043b\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0441\u0442\u0440\u043e\u043a\u0438", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u041c\u043e\u0434\u044b", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u043d\u0430\u0442", None))
    # retranslateUi

