from PySide import QtCore, QtGui

# from serval_gui.tools.guirestore import *
# from serval_gui.tools.guisave import *

class AbstractWidget(QtGui.QWidget):
    def __init__(self,parent):
        self.parent = parent
        super(AbstractWidget, self).__init__(None)
        self.name =  str(type(self)).split(".")[-1].split("'")[0]


        # self.settings = QtCore.QSettings(self.name)
        
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
           
    def setTitle(self,title):
        """Set the text in the title bar of the widget
        
        Args:
            title str: Text to set
        
        """
        self.setWindowTitle(QtGui.QApplication.translate("", str(title), None, QtGui.QApplication.UnicodeUTF8))

    def trigger(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()
        