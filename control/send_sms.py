from ui.send_sms import Ui_SendSMS
from abstract_widget import AbstractWidget
# from post_threading import Post
# import time
class SendSMS(AbstractWidget):
    def __init__(self,parent):
        super(SendSMS,self).__init__(parent)
        self.ui = Ui_SendSMS()
        self.ui.setupUi(self)
        # self.post = Post(self)
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_send_sms.clicked.connect(self.sendSMS)
        
        
    def sendSMS(self):
        number = le_number.text()
        if not number.isdigit():
            return
        text = te_text.text()
        self.parent.sb.sendSMS(number,text)
        