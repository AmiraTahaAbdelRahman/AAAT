# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 14:40:34 2017

@author: toka eldeeb
"""

import sys
from PyQt5 import QtCore,QtGui
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem,QLabel,QSizePolicy,QLineEdit,QScrollArea,QMessageBox

import datetime

class window(QMainWindow):
    
    
    i=0 
    stop_flag =0
    timer = QtCore.QTimer()
    p=0
    hexInfo=[]
    contentInfo=[]
    content=""
    summary=""
    hexinfo=""
    src=""
    dest=""
    size=""
    proto=""
    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 1000, 1000)
        self.setWindowTitle('WireShark')
        self.timer.timeout.connect(self.count)
        self.home()

    def home(self):
        btn = QPushButton('start', self)
        btn.clicked.connect(self.table_data)
        btn.setToolTip('Start Capturing <b>Packages</b>')
        btn.resize(50, 50)
        btn.move(10, 10)
        btn2 = QPushButton('Quit', self)
        btn2.clicked.connect(QCoreApplication.instance().quit)
        btn2.resize(50, 50)
        btn2.move(70, 10)
        self.show()
        
    def handleStop(self):
        self.stop_flag =1

    def table_data(self):
        self.form_widget = MyTable(10000, 6)
        self.setCentralWidget(self.form_widget)
        col_headers = ['Number', 'Time', 'Source', 'Destination', 'Protocol', 'Length']
        self.form_widget.setHorizontalHeaderLabels(col_headers) 
        btn3 =QPushButton('Stop', self)
        btn3.clicked.connect(self.stop)
        btn3.resize(50, 50)
        btn3.move(980, 30)
        btn3.show()
        self.textbox = QLineEdit(self)
        self.textbox.move(780, 20)
        self.textbox.resize(100,30)
        self.textbox.show()
        btn4 =QPushButton('Filter', self)
        btn4.clicked.connect(self.filterprot)
        btn4.resize(50, 50)
        btn4.move(880, 30)
        btn4.show()
        

        
        self.show()
        self.start()

        
    def start(self):
        # Number of milliseconds the timer waits until the timeout
        self.timer.start(1000)

    def stop(self):
        print("end")
        self.timer.stop()
        

    
    def count(self):

       #sniff function called here
       #set all attributes(src,dest,proto,size....)
        
        src1 = QTableWidgetItem(str(self.src))
        dest1=QTableWidgetItem(str(self.dest))
        protocol1=QTableWidgetItem(str(self.proto))
        time = QTableWidgetItem(str(time))
        size = QTableWidgetItem(str(self.size))
        number = QTableWidgetItem(str(self.i))
        
        self.form_widget.setCurrentCell(0, 0)
        self.form_widget.setItem(self.i, 0, number)
        self.form_widget.setItem(self.i, 1, time)
        self.form_widget.setItem(self.i, 2, src1)
        self.form_widget.setItem(self.i, 3, dest1)
        self.form_widget.setItem(self.i, 4, protocol1)
        self.form_widget.setItem(self.i, 5, size)
        
        self.form_widget.clicked.connect(self.subwindow)
        self.i=self.i+1
        

        
    def subwindow(self,p):
        rows=[idx.row() for idx in self.form_widget.selectionModel().selectedIndexes()]
        
        #get content of packet and its hexcode 
        middle=self.contentInfo[rows[0]]
        last=self.hexInfo[rows[0]]
        
        self.label = QLabel(middle, self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.move(750,80)
        self.label.resize(390,400)
        self.label.setStyleSheet("QLabel {background-color: pink;}")
        self.label.show()
        
        self.label2 = QLabel(last, self)
        self.label2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label2.move(750,400)
        self.label2.resize(390,400)
        self.label2.setStyleSheet("QLabel {background-color: yellow;}")
        self.label2.show()
        
        
    def filterprot(self):
        self.timer.stop()
        # filter proxy model
        filter_proxy_model = QtGui.QSortFilterProxyModel()
        filter_proxy_model.setSourceModel(self.form_widget)
        filter_proxy_model.setFilterKeyColumn(4) # forth column
        t=self.textbox.text()
        print(t)
   



    
def run():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())

run()
