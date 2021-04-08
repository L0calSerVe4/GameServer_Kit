from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QUrl
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication
from PySide2.QtWebEngine import QtWebEngine
from PySide2.QtWidgets import (QApplication, QDialog, QLayout, QGridLayout,
                               QMessageBox, QGroupBox, QSpinBox, QSlider,
                               QProgressBar, QDial, QDialogButtonBox,
                               QComboBox, QLabel)
from asd import Ui_Form  # импорт нашего сгенерированного файла
import sys
import os

a = 0


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.a = 0
        super(mywindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle("Тест")
        
        self.ui.pushButton.clicked.connect(self.pushButtonClicked)
        self.ui.minimize.clicked.connect(self.minimizeClicked)
        self.ui.pushButton_2.clicked.connect(self.pushButtonTwo)
        self.ui.pushButton_3.clicked.connect(self.pushButtonThree)
        self.ui.pushButton_4.clicked.connect(self.pushButtonFour)
        self.ui.pushButton_5.clicked.connect(self.pushButtonFive)


    def StackedWidget(self):
        vbox = QtWidgets.QVBoxLayout()

        vbox.addWidget(QtWidgets.QStackedWidget())

        for x in range(0,4):
            label = QtWidgets.QLabel("Stacked Child " + str(x) )
            label.setFont(QtGui.QFont("Sanserif", 15))
            label.setStyleSheet("Color: red")
        
            QtWidgets.QStackedWidget().addWidget(label)
        
        firstPageWidget = QtWidgets.QWidget()
        secondPageWidget = QtWidgets.QWidget()
        thirdPageWidget = QtWidgets.QWidget()
        fourthPageWidget = QtWidgets.QWidget()

        vbox.addWidget(firstPageWidget)
        vbox.addWidget(secondPageWidget)
        vbox.addWidget(thirdPageWidget)
        vbox.addWidget(fourthPageWidget)
        label = QtWidgets.QLabel("Stacked Child")
        QtWidgets.QStackedWidget().addWidget(label)

    def pushButtonTwo(self):
        self.ui.pushButton_2.setChecked(True)
        self.ui.pushButton_3.setChecked(False)
        self.ui.pushButton_4.setChecked(False)
        self.ui.pushButton_5.setChecked(False)
        QtWidgets.QStackedWidget().setCurrentIndex(0)
        
    def pushButtonThree(self):
        self.ui.pushButton_2.setChecked(False)
        self.ui.pushButton_3.setChecked(True)
        self.ui.pushButton_4.setChecked(False)
        self.ui.pushButton_5.setChecked(False)
        QtWidgets.QStackedWidget().setCurrentIndex(1)

    def pushButtonFour(self):
        self.ui.pushButton_3.setChecked(False)
        self.ui.pushButton_2.setChecked(False)
        self.ui.pushButton_4.setChecked(True)
        self.ui.pushButton_5.setChecked(False)
        QtWidgets.QStackedWidget().setCurrentIndex(2)

    def pushButtonFive(self):
        self.ui.pushButton_3.setChecked(False)
        self.ui.pushButton_4.setChecked(False)
        self.ui.pushButton_2.setChecked(False)
        self.ui.pushButton_5.setChecked(True)
        QtWidgets.QStackedWidget().setCurrentIndex(3)

    def pushButtonClicked(self):
        sys.exit()
    
    def minimizeClicked(self):
        self.showMinimized()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

# class TabWidget(QtWidgets.QTabWidget):
#     def __init__(self, *args, **kwargs):
#         QtWidgets.QTabWidget.__init__(self, *args, **kwargs)
#         self.setTabBar(TabBar(self))
#         self.setTabPosition(QtWidgets.QTabWidget.West)

# class TabBar(QtWidgets.QTabBar):
#     def tabSizeHint(self, index):
#         s = QtWidgets.QTabBar.tabSizeHint(self, index)
#         s.transpose()
#         return s

#     def paintEvent(self, event):
#         painter = QtWidgets.QStylePainter(self)
#         opt = QtWidgets.QStyleOptionTab()

#         for i in range(self.count()):
#             self.initStyleOption(opt, i)
#             painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
#             painter.save()

#             s = opt.rect.size()
#             s.transpose()
#             r = QtCore.QRect(QtCore.QPoint(), s)
#             r.moveCenter(opt.rect.center())
#             opt.rect = r

#             c = self.tabRect(i).center()
#             painter.translate(c)
#             painter.rotate(90)
#             painter.translate(-c)
#             painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt)
#             painter.restore()

# class MyWindow(QtWidgets.QWidget):
#     def __init__(self, parent = None):
#         super().__init__(parent)
#         self.setFixedSize(800, 400)
#         self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)         # !!!    

#         self.tabs = TabWidget()                                                  # QtWidgets.QTabWidget()

#         self.tabs.setTabPosition(QtWidgets.QTabWidget.West)                      #
#         self.tabs.setDocumentMode(True)
#         self.tabs.setMovable(True)
#         self.tabs.addTab(QtWidgets.QLabel('Тест', alignment=QtCore.Qt.AlignCenter), 
#                  '1')                                    # 'Вкладка 1'

#         self.tabs.addTab(QtWidgets.QLabel('2'), '2')          # , 'Вкладка 2'

#         self.tabs.setCurrentIndex(0)

#         box = QtWidgets.QVBoxLayout(self)
#         box.addWidget(self.tabs)
#         box.setContentsMargins(0, 0, 0, 0)

#     def closeTab(self, index):
#         tab = self.tabs.widget(index)
#         tab.deleteLater()
#         self.tabs.removeTab(index)

 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
app.exec_()