from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap, QFont
import sys
from random import randint


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button_clicked(self):
        i = randint(1,2)
        txt = "WYGRYWA TRIP" + str(i)
        path = str(i) + ".jpg"
        self.label.setText(txt)
        self.image.setPixmap(QPixmap(path))


    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("Losowanko")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("")
        self.label.move(155,30)

        self.image = QtWidgets.QLabel(self)
        self.image.setPixmap(QPixmap(""))
        self.image.setFixedSize(380, 245)
        self.image.move(10, 70)


        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Losowanko!")
        self.b1.move(150,350)
        self.b1.clicked.connect(self.button_clicked)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()