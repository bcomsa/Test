# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\chatdlg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_chatdlg(object):
    def setupUi(self, chatdlg):
        chatdlg.setObjectName(_fromUtf8("chatdlg"))
        chatdlg.resize(400, 355)
        self.verticalLayout = QtGui.QVBoxLayout(chatdlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.total_chat_box = QtGui.QPlainTextEdit(chatdlg)
        self.total_chat_box.setReadOnly(True)
        self.total_chat_box.setObjectName(_fromUtf8("total_chat_box"))
        self.verticalLayout.addWidget(self.total_chat_box)
        self.chat_box = QtGui.QLineEdit(chatdlg)
        self.chat_box.setObjectName(_fromUtf8("chat_box"))
        self.verticalLayout.addWidget(self.chat_box)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.send_pushButton = QtGui.QPushButton(chatdlg)
        self.send_pushButton.setObjectName(_fromUtf8("send_pushButton"))
        self.horizontalLayout.addWidget(self.send_pushButton)
        self.cancel_pushButton = QtGui.QPushButton(chatdlg)
        self.cancel_pushButton.setObjectName(_fromUtf8("cancel_pushButton"))
        self.horizontalLayout.addWidget(self.cancel_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(chatdlg)
        QtCore.QObject.connect(self.cancel_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), chatdlg.reject)
        QtCore.QMetaObject.connectSlotsByName(chatdlg)

    def retranslateUi(self, chatdlg):
        chatdlg.setWindowTitle(_translate("chatdlg", "Chat", None))
        self.send_pushButton.setText(_translate("chatdlg", "Send", None))
        self.cancel_pushButton.setText(_translate("chatdlg", "Cancel", None))

