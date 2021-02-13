from PyQt5 import QtCore, QtWidgets, QtGui
from asd import Ui_Form  # импорт нашего сгенерированного файла
import sys

a = 0

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.a = 0
        super(mywindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        firstPageWidget = QtWidgets.QWidget()
        secondPageWidget = QtWidgets.QWidget()
        thirdPageWidget = QtWidgets.QWidget()
        fourthPageWidget = QtWidgets.QWidget()
        
        stackedWidget = QtWidgets.QStackedWidget()
        stackedWidget.addWidget(firstPageWidget)
        stackedWidget.addWidget(secondPageWidget)
        stackedWidget.addWidget(thirdPageWidget)
        stackedWidget.addWidget(fourthPageWidget)
        layout =  QtWidgets.QVBoxLayout()
        layout.addWidget(stackedWidget)
        QtWidgets.QWidget.setLayout(layout)
        
        self.ui.pushButton.clicked.connect(self.pushButtonClicked)
        self.ui.minimize.clicked.connect(self.minimizeClicked)
        self.ui.pushButton_2.clicked.connect(self.pushButtonTwo)
        self.ui.pushButton_3.clicked.connect(self.pushButtonThree)
        self.ui.pushButton_4.clicked.connect(self.pushButtonFour)
        self.ui.pushButton_5.clicked.connect(self.pushButtonFive)


    def pushButtonTwo(self):
        self.ui.pushButton_3.setChecked(False)
        self.ui.pushButton_4.setChecked(False)
        self.ui.pushButton_5.setChecked(False)
        QtWidgets.QStackedWidget().setCurrentIndex(0)

    def pushButtonThree(self):
        self.ui.pushButton_2.setChecked(False)
        self.ui.pushButton_4.setChecked(False)
        self.ui.pushButton_5.setChecked(False)
        QtWidgets.QStackedWidget().setCurrentIndex(1)

    def pushButtonFour(self):
        self.ui.pushButton_3.setChecked(False)
        self.ui.pushButton_2.setChecked(False)
        self.ui.pushButton_5.setChecked(False)
        QtWidgets.QStackedWidget().setCurrentIndex(2)

    def pushButtonFive(self):
        self.ui.pushButton_3.setChecked(False)
        self.ui.pushButton_4.setChecked(False)
        self.ui.pushButton_2.setChecked(False)
        QtWidgets.QStackedWidget().setCurrentIndex(3)

    def pushButtonClicked(self):
        sys.exit()
    
    def minimizeClicked(self):
        self.showMinimized()

    # def mousePressEvent(self, event):
    #     QtGui.QMoveEvent.oldPos() = event.globalPos()

    # def mouseMoveEvent(self, event):
    #     delta = QtCore.QPoint(event.globalPos() - self.oldPos)
    #     #print(delta)
    #     self.move(self.x() + delta.x(), self.y() + delta.y())
    #     self.oldPos = event.globalPos()
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())