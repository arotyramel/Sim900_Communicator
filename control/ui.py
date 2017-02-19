#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import time
import traceback
import sys
from ui.mainwindow import Ui_MainWindow
from call import Call
from incoming_call import IncomingCall
from incoming_sms import IncomingSMS
from import_csv import ImportCSV
from received_sms import ReceivedSMS
from sent_sms import SentSMS
from send_sms import SendSMS
from serial_bridge import SerialBridge
from PySide.QtCore import QObject, Signal, Slot
from post_threading import Post
class Application(QtGui.QApplication):
    """used to be able to terminate the qt window by ctrl+c
    """
    def event(self, e):    
        """Summary
        
        Args:
            e (TYPE): Description
        
        Returns:
            TYPE: Description
        """
#         print "app event"
        return QtGui.QApplication.event(self, e)

    def notify(self, obj, event):
        """Summary
        
        Args:
            obj (TYPE): Description
            event (TYPE): Description
        
        Returns:
            TYPE: Description
        """
        isex = False
        try:
            return QtGui.QApplication.notify(self, obj, event)
        except Exception as e:
            isex = True
            print "Unexpected Error : " + str(e)
            print traceback.format_exception(*sys.exc_info())
            return False
        finally:
            if isex:
                self.quit()
                
class ControlMainWindow(QtGui.QMainWindow):
    updateFeedbackSignal = Signal(str)
    def __init__(self, app):
        super(ControlMainWindow, self).__init__(None)
        # self.settings = QtCore.QSettings("root_window")
        self.app = app
        self.post = Post(self)
        self.widgets={}
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusbar.showMessage("Not connected")
        self.show()
        
        self.post.initSerialBridge()
        self.initUi()
    
    def initUi(self):
        self.ui.btn_close.clicked.connect(self.close)
        
        self.widgets["call"] =Call(self)
        self.ui.btn_call.clicked.connect(self.widgets["call"].show)
        
        
        self.widgets["import_csv"] = ImportCSV(self)
        self.ui.btn_import_csv.clicked.connect(self.widgets["import_csv"].show)
        
        self.widgets["received_sms"] = ReceivedSMS(self)
        self.ui.btn_show_sms.clicked.connect(self.widgets["received_sms"].show)
        
        self.widgets["sent_sms"] = SentSMS(self)
        self.ui.btn_sent_sms.clicked.connect(self.widgets["sent_sms"].show)
        
        self.widgets["send_sms"] = SendSMS(self)
        self.ui.btn_send_sms.clicked.connect(self.widgets["send_sms"].show)
        
        self.widgets["incoming_call"] = IncomingCall(self)
        self.widgets["incoming_sms"] = IncomingSMS(self)
        self.updateFeedbackSignal.connect(self.updateFeedback)
        # self.widgets["import_csv"].show()
        # self.widgets["incomding_sms"].show()
    
    def initSerialBridge(self):
        self.sb = SerialBridge()
        time.sleep(2.0)
        self.sb.send("AT")
        self.sb.trigger_words +=["AT","RING","ATA","ATH","ATD","CMT","NO CARRIER"]
        self.sb.callback = self.cbSim
        
    def cbSim(self,feedback):
        self.updateFeedbackSignal.emit(feedback)
    
    @Slot(str)
    def updateFeedback(self,feedback):
        print "got feedback"
        if feedback == "RING":
            self.widgets["incoming_call"].incomingCall()
        if feedback == "ATA":
            self.widgets["incoming_call"].callAnswered()
        if feedback == "ATH":
            self.widgets["incoming_call"].callStopped()
            self.widgets["call"].callStopped()
        if "ATD" in feedback:
            self.widgets["call"].callStarted()
        if "AT" == feedback:
            self.ui.statusbar.showMessage("Connected")
        if "CMT" in feedback:
            self.widgets["incoming_sms"].incomingSMS(feedback)
        # if "CMGR" in feedback:
            # self.widgets["incoming_sms"].messageContent(feedback)
        if "NO CARRIER" in feedback:
            self.widgets["incoming_call"].callStopped()

    def keyPressEvent(self, e):
        """Summary
        
        Args:
            e (TYPE): Description
        
        Returns:
            TYPE: Description
        """
        #closes the window on escape
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
            
    def closeEvent(self, event):
        try:
            self.sb.close()
        except:
            pass
        for widget in self.widgets.values():
            widget.close()
        super(ControlMainWindow,self).closeEvent(event)

def main():
        app = Application(sys.argv)
        app.startTimer(200)
        gui = ControlMainWindow(app)
        sys.exit(app.exec_())
        

if __name__ == '__main__':
    main()