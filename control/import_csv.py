import csv
from ui.import_csv import Ui_ImportCSV
from abstract_widget import AbstractWidget
from PySide import QtGui, QtCore
class ImportCSV(AbstractWidget):
    def __init__(self,parent):
        super(ImportCSV,self).__init__(parent)
        self.ui = Ui_ImportCSV()
        self.ui.setupUi(self)
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_import_csv.clicked.connect(self.importCSV)
        self.ui.btn_tick_all.clicked.connect(lambda state: self.tickAll(True))
        self.ui.btn_untick_all.clicked.connect(lambda state: self.tickAll(False))
        self.ui.btn_send_sms.clicked.connect(self.sendSMS)
        
        
    def importCSV(self):
        file_name =  QtGui.QFileDialog.getOpenFileName(self,"Choose a CSV file")[0]
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
        pass
        
    def sendSMS(self):
        pass
        
    def createTableEntry(self,row):
        for col, cell in enumerate(row):
            print "row", self.row, "col",col,"value", cell
            item = QtGui.QTableWidgetItem(cell)
            self.ui.tbl.setItem(self.row,col,item)
