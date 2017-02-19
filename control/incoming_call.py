from ui.incoming_call import Ui_IncomingCall
from abstract_widget import AbstractWidget
from post_threading import Post
import time
class IncomingCall(AbstractWidget):
    def __init__(self,parent):
        super(IncomingCall,self).__init__(parent)
        self.ui = Ui_IncomingCall()
        self.ui.setupUi(self)
        self.post = Post(self)
        self.calling = False
        self.call_active = False
        self.ui.btn_hangup.clicked.connect(self.hangup)
        self.ui.btn_answer.clicked.connect(self.answer)
        self.ui.btn_close.clicked.connect(self.close)
        
    def incomingCall(self):
        if self.calling or self.call_active:
            return
        self.ui.btn_close.setEnabled(False)
        self.ui.btn_hangup.setEnabled(True)
        self.ui.btn_answer.setEnabled(True)        
        self.calling = True
        self.show()
    
    def hangup(self):
        self.parent.sb.hangupCall()
        
    def answer(self):
        self.parent.sb.answerCall()
        
    
    def callAnswered(self):
        self.call_active = True
        self.calling = False
        self.call_start = time.time()
        self.ui.btn_answer.setEnabled(False)
        self.post.showDuration()

    def callStopped(self):
        self.call_active = False
        self.calling = False
        self.ui.btn_close.setEnabled(True)
        self.ui.btn_hangup.setEnabled(False)
        self.ui.btn_answer.setEnabled(False)
    
    def showDuration(self):
        while self.call_active:
            now = time.time()-self.call_start
            minutes = int(now/60)
            seconds = int(now%60)
            self.ui.lbl_duration.setText("%02.d:%02.d"%(minutes,seconds))
            time.sleep(1)
        
    def closeEvent(self,event):
        if self.call_active or self.calling:
            event.ignore()
            self.hangup()
        else:
            event.accept()