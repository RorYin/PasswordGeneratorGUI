from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtGui import QIcon,QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QMessageBox
import pyperclip
from generator import genpassword



class Screen1(QtWidgets.QMainWindow):
    def __init__(self):
        super(Screen1, self).__init__()
        uic.loadUi("uic/sc1.ui", self)

        self.generate.clicked.connect(lambda: self.getinput())
        self.copytoclip.clicked.connect(lambda: self.copyto())

    def copyto(self):
        pyperclip.copy(self.result.text())


    def getinput(self):
        try:
            self.l = self.lower.text()
            self.u = self.upper.text()
            self.d = self.digits.text()
            self.s = self.symbols.text()

            print(self.l,self.u,self.s,self.d)
            
            screen1.result.setText(genpassword(self.l,self.u,self.d,self.s))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Oooops")
            msg.setWindowIcon(QIcon("uic/logo.png"))
            msg.setText("Please check and enter values to generate password")
            msg.exec_()

        


app = QtWidgets.QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
screen1=Screen1()
widget.addWidget(screen1)

widget.setWindowIcon(QIcon("uic/logo.png"))
widget.setWindowTitle("password Generator GUI")
widget.show()

app.exec_()