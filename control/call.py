from ui.call import Ui_Call
from abstract_widget import AbstractWidget
class Call(AbstractWidget):
    def __init__(self,parent):
        super(Call,self).__init__(parent)
        self.ui = Ui_Call()
        self.ui.setupUi(self)
        self.call_active = False
        self.calling = False
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_call.clicked.connect(self.call)
        self.ui.btn_mute.clicked.connect(self.mute)
        self.ui.btn_hangup.clicked.connect(self.hangup)
        self.ui.btn_get_contact.clicked.connect(self.getContact)
        
        
    def show(self):
        self.ui.btn_hangup.setEnabled(False)
        super(Call,self).show()
        
    def call(self):
        number = self.ui.le_number.text()
        if not number.isdigit():
            self.ui.lbl_state.setText("Invalid number")
            return
        self.ui.lbl_state.setText("Calling")
        #todo make call
        self.calling = True
        self.parent.sb.callNumber(number)
        
    
    def callStarted(self):
        self.call_active = True
        self.calling = False
        self.call_start = time.time()
        self.ui.btn_call.setEnabled(False)
        self.ui.btn_close.setEnabled(False)
        self.ui.lbl_state.setText("Connected")
        self.post.showDuration()
    
    def callStopped(self):
        self.call_active = False
        self.ui.lbl_duration.setText("00:00")
        self.ui.btn_hangup.setEnabled(False)
        
    def mute(self):
        # AT+CMUT=1
        pass
    
    def hangup(self):
        self.parent.sb.hangupCall()
        
        
    def getContact(self):
        #todo get contact list and open list popup widget
        pass
        
    def closeEvent(self,event):
        if self.call_active or self.calling:
            event.ignore()
            self.hangup()
        else:
            event.accept()
        
    def showDuration(self):
        while self.call_active:
            now = time.time()-self.call_start
            minutes = int(now/60)
            seconds = int(now%60)
            self.ui.lbl_duration.setText("%02.d:%02.d"%(minutes,seconds))
            time.sleep(1)