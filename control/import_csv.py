#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
from ui.import_csv import Ui_ImportCSV
from abstract_widget import AbstractWidget
from PySide import QtGui, QtCore
from PySide.QtCore import QObject, Signal, Slot
class ImportCSV(AbstractWidget):
    def __init__(self,parent):
        super(ImportCSV,self).__init__(parent)
        self.ui = Ui_ImportCSV()
        self.ui.setupUi(self)
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_import_csv.clicked.connect(self.importCSV)
        self.ui.btn_tick_all.clicked.connect(lambda: self.tickAll(True))
        self.ui.btn_untick_all.clicked.connect(lambda: self.tickAll(False))
        self.ui.btn_send_sms.clicked.connect(self.sendSMS)
        self.importCSV()
        
    def importCSV(self):
        # file_name =  QtGui.QFileDialog.getOpenFileName(self,"Choose a CSV file")[0]
        file_name = "example.csv"
        print file_name
        if file_name == "":
            return
        self.row = 0
        with open(file_name, 'rb') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                self.createTableEntry(row)
                self.row+=1
            
        
        
    def tickAll(self,state):
        for i in xrange(self.ui.tbl.rowCount()):
            if state:
                self.ui.tbl.item(i,0).setCheckState(QtCore.Qt.Checked)
            else:
                self.ui.tbl.item(i,0).setCheckState(QtCore.Qt.Unchecked)
        
    def sendSMS(self):
        for i in xrange(self.ui.tbl.rowCount()):
            if self.ui.tbl.item(i,0).checkState() == QtCore.Qt.Checked:
                number= self.ui.tbl.item(i,1).text()
                text = self.ui.tbl.item(i,3).text()
                self.parent.sb.sendSMS(number,text.encode("utf-8"))
        
    def createTableEntry(self,row):
        self.ui.tbl.setRowCount(self.row+1)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)    
        self.ui.tbl.setItem(self.row,0,item)
        for col, cell in enumerate(row):
            print "row", self.row, "col",col,"value", cell
            item = QtGui.QTableWidgetItem(cell)
            self.ui.tbl.setItem(self.row,col+1,item)
        # self.ui.tbl.cellChanged.connect(self.cellChanged)

    # @Slot(int,int)
    # def cellChanged(self,row,col):
        # print row,";",col
        
    