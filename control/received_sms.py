import csv
from ui.received_sms import Ui_ReceivedSMS
from abstract_widget import AbstractWidget
class ReceivedSMS(AbstractWidget):
    def __init__(self,parent):
        super(ReceivedSMS,self).__init__(parent)
        self.ui = Ui_ReceivedSMS()
        self.ui.setupUi(self)
        self.ui.btn_close.clicked.connect(self.close)