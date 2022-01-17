import string
import random
from PyQt5 import QtWidgets, uic  

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QMessageBox
import pyperclip #to copy from the output to the clipboard #pip install pyperclip


#Code for generating strong password 
lowercase=string.ascii_lowercase 
uppercase=string.ascii_uppercase
digits =string.digits
symbols = string.punctuation

def genpassword(l,h,d,s): 

    password = ""
    l=int(l)
    h=int(h)
    d=int(d)
    s=int(s)

    if l<1 or h<1 or d<1 or s<1:
        return "1 is the minimum number for all fields"
    try:

        for i in range(0,h):
            password=password+random.choice(uppercase)

        for i in range(0,l):
            password=password+random.choice(lowercase)

        for i in range(0,d):
            password=password+random.choice(digits)

        for i in range(0,s):
            password=password+random.choice(symbols)

        return(password)
    except:
        return("Something went wrong")


#Code for integrating gui components to python code

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
            
            result=genpassword(self.l,self.u,self.d,self.s)
            screen1.result.setText(result)
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