# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\connectiondlg.ui'
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

class Ui_ConnectionDialog(object):
    def setupUi(self, ConnectionDialog):
        ConnectionDialog.setObjectName(_fromUtf8("ConnectionDialog"))
        ConnectionDialog.resize(305, 146)
        self.verticalLayout = QtGui.QVBoxLayout(ConnectionDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ip_label = QtGui.QLabel(ConnectionDialog)
        self.ip_label.setObjectName(_fromUtf8("ip_label"))
        self.gridLayout.addWidget(self.ip_label, 0, 0, 1, 1)
        self.port_label = QtGui.QLabel(ConnectionDialog)
        self.port_label.setObjectName(_fromUtf8("port_label"))
        self.gridLayout.addWidget(self.port_label, 1, 0, 1, 1)
        self.port_lineEdit = QtGui.QLineEdit(ConnectionDialog)
        self.port_lineEdit.setObjectName(_fromUtf8("port_lineEdit"))
        self.gridLayout.addWidget(self.port_lineEdit, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.ip_lineEdit = QtGui.QLineEdit(ConnectionDialog)
        self.ip_lineEdit.setObjectName(_fromUtf8("ip_lineEdit"))
        self.gridLayout.addWidget(self.ip_lineEdit, 0, 1, 1, 2)
        self.groupBox = QtGui.QGroupBox(ConnectionDialog)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.server_radioButton = QtGui.QRadioButton(self.groupBox)
        self.server_radioButton.setChecked(True)
        self.server_radioButton.setObjectName(_fromUtf8("server_radioButton"))
        self.horizontalLayout_2.addWidget(self.server_radioButton)
        self.client_radioButton = QtGui.QRadioButton(self.groupBox)
        self.client_radioButton.setChecked(False)
        self.client_radioButton.setObjectName(_fromUtf8("client_radioButton"))
        self.horizontalLayout_2.addWidget(self.client_radioButton)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 171, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.connect_pushButton = QtGui.QPushButton(ConnectionDialog)
        self.connect_pushButton.setObjectName(_fromUtf8("connect_pushButton"))
        self.horizontalLayout.addWidget(self.connect_pushButton)
        self.cancel_pushButton = QtGui.QPushButton(ConnectionDialog)
        self.cancel_pushButton.setObjectName(_fromUtf8("cancel_pushButton"))
        self.horizontalLayout.addWidget(self.cancel_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ConnectionDialog)
        QtCore.QObject.connect(self.cancel_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ConnectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConnectionDialog)
        ConnectionDialog.setTabOrder(self.ip_lineEdit, self.port_lineEdit)
        ConnectionDialog.setTabOrder(self.port_lineEdit, self.server_radioButton)
        ConnectionDialog.setTabOrder(self.server_radioButton, self.client_radioButton)
        ConnectionDialog.setTabOrder(self.client_radioButton, self.connect_pushButton)
        ConnectionDialog.setTabOrder(self.connect_pushButton, self.cancel_pushButton)

    def retranslateUi(self, ConnectionDialog):
        ConnectionDialog.setWindowTitle(_translate("ConnectionDialog", "Connection", None))
        self.ip_label.setText(_translate("ConnectionDialog", "IP", None))
        self.port_label.setText(_translate("ConnectionDialog", "Port", None))
        self.server_radioButton.setText(_translate("ConnectionDialog", "SERVER", None))
        self.client_radioButton.setText(_translate("ConnectionDialog", "CLIENT", None))
        self.connect_pushButton.setText(_translate("ConnectionDialog", "Host", None))
        self.cancel_pushButton.setText(_translate("ConnectionDialog", "Cancel", None))

