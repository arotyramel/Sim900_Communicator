import serial
from post_threading import Post
import time

class SerialBridge:
    def __init__(self):
        self.post = Post(self)
        self.conn_down = True
        self.initConnection()
        self.trigger_words = []
        self.callback = None
        
    def openSerialPort(self,i):
        
        try:
            self.ser = serial.Serial('COM'+str(i), 19200)
            self.ser.flushInput()
            self.ser.flush()
            self.conn_down = False
            return True
        except serial.serialutil.SerialException as e:
            if "could not open port" in str(e):
                return False
            else:
                print "Problem accessing the device",e
                exit(1)
                
    def initConnection(self):
        for i in xrange(20):
            if self.openSerialPort(i):
                break
            
        if self.conn_down:
            print "could not establish connection"
            exit(1)
            return
        self.post.readFeedback()
        
    def readFeedback(self):
        print "reading feedback"
        while not self.conn_down:
            feedback =  self.ser.readline()
            feedback = feedback.replace("\n","")
            feedback = feedback.replace ("\r","")
            print feedback
            if not self.callback is None and feedback in self.trigger_words:
                self.callback(feedback)
            time.sleep(0.1)
        print "done reading feedback"
            
    def send(self, data):
        if len(data)>0:
            print "send", data
            self.ser.write(data+"\n\r")
            self.ser.flush()
            
    def sendSMS(self, number, text):
        self.send("SMS:"+str(number)+";"+str(text))
        
    def answerCall(self):
        self.send("ATA")
        
    def hangupCall(self):
        self.send("ATH")

    def callNumber(self,number):
        self.send("ATD"+str(number))
        
    def getReceivedSMS(self):
        pass
        
    def getSentSMS(self):
        pass
        
    def close(self):
        self.conn_down = True
        self.ser.close()
    