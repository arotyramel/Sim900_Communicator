from ui.sent_sms import Ui_SentSMSfrom abstract_widget import AbstractWidgetclass SentSMS(AbstractWidget):    def __init__(self,parent):        super(SentSMS,self).__init__(parent)        self.ui = Ui_SentSMS()        self.ui.setupUi(self)        self.ui.btn_close.clicked.connect(self.close)