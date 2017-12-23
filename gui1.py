import sys
from PyQt5 import QtCore,QtGui
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem

class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.show()
        
    def init_ui(self):
        self.cellChanged.connect(self.c_current)
        self.show()

    def c_current(self):
        row = self.currentRow()
        col = self.currentColumn()
        value = self.item(row, col)
        value = value.text()
        print("The current cell is ", row, ", ", col)
        print("In this cell we have: ", value)

class Sheet(QMainWindow):
    def __init__(self):
        super().__init__()
        self.form_widget = MyTable(10, 10)
        self.setCentralWidget(self.form_widget)
        self.show()




