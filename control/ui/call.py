# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M:\user\Arotyramel\GoogleDrive\Arduino\GSM Modules\Anna\git\control\ui\call.ui'
#
# Created: Sun Feb 19 17:29:31 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Call(object):
    def setupUi(self, Call):
        Call.setObjectName("Call")
        Call.resize(349, 204)
        self.formLayout_2 = QtGui.QFormLayout(Call)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtGui.QLabel(Call)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.le_number = QtGui.QLineEdit(Call)
        self.le_number.setObjectName("le_number")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.le_number)
        self.btn_get_contact = QtGui.QPushButton(Call)
        self.btn_get_contact.setObjectName("btn_get_contact")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.btn_get_contact)
        self.le_contact = QtGui.QLineEdit(Call)
        self.le_contact.setObjectName("le_contact")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.le_contact)
        self.btn_hangup = QtGui.QPushButton(Call)
        self.btn_hangup.setObjectName("btn_hangup")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.btn_hangup)
        self.btn_call = QtGui.QPushButton(Call)
        self.btn_call.setObjectName("btn_call")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.btn_call)
        self.btn_mute = QtGui.QPushButton(Call)
        self.btn_mute.setObjectName("btn_mute")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.btn_mute)
        self.line = QtGui.QFrame(Call)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.line)
        self.btn_close = QtGui.QPushButton(Call)
        self.btn_close.setObjectName("btn_close")
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.FieldRole, self.btn_close)
        self.lbl_state = QtGui.QLabel(Call)
        self.lbl_state.setObjectName("lbl_state")
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.lbl_state)
        self.label_3 = QtGui.QLabel(Call)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lbl_duration = QtGui.QLabel(Call)
        self.lbl_duration.setObjectName("lbl_duration")
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.lbl_duration)
        self.label_2 = QtGui.QLabel(Call)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_2)

        self.retranslateUi(Call)
        QtCore.QMetaObject.connectSlotsByName(Call)

    def retranslateUi(self, Call):
        Call.setWindowTitle(QtGui.QApplication.translate("Call", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Call", "Number", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_get_contact.setText(QtGui.QApplication.translate("Call", "Get Contact", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_hangup.setText(QtGui.QApplication.translate("Call", "Hangup", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_call.setText(QtGui.QApplication.translate("Call", "Call", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_mute.setText(QtGui.QApplication.translate("Call", "Mute Mic", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_close.setText(QtGui.QApplication.translate("Call", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_state.setText(QtGui.QApplication.translate("Call", "idle", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Call", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_duration.setText(QtGui.QApplication.translate("Call", "00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Call", "Duration", None, QtGui.QApplication.UnicodeUTF8))

