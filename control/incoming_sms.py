from ui.incoming_sms import Ui_IncomingSMS
from abstract_widget import AbstractWidget
from post_threading import Post
import time
class IncomingSMS(AbstractWidget):
    def __init__(self,parent):
        super(IncomingSMS,self).__init__(parent)
        self.ui = Ui_IncomingSMS()
        self.ui.setupUi(self)
        self.post = Post(self)
        self.calling = False
        self.call_active = False
        self.ui.btn_close.clicked.connect(self.close)
        
    def incomingSMS(self,msg):
        self.show()
        print "incoming sms",msg
        number = "+"+msg.split(",")[0].split("+")[-1][:-1]
        name=msg.split("\"")[3]
        text = msg.split("\"")[-1]
        self.ui.lbl_number.setText(number)
        self.ui.lbl_name.setText(name)
        self.ui.te_text.setText(text)
        
    # def messageContent(self,msg):
        # print "msg:",msg
        
    