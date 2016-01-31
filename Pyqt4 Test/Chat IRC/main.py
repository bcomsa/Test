# -*- coding: utf-8 -*-
#!/usr/bin/env python

from PyQt4.QtCore import (Qt, SIGNAL, pyqtSignature)
from PyQt4.QtGui import (QApplication, QDialog, QMessageBox)
import ui_connectiondlg
import socket
import threading

class ConnectionDlg(QDialog,
        ui_connectiondlg.Ui_ConnectionDialog):

    def __init__(self, parent=None):
        super(ConnectionDlg, self).__init__(parent)
        self.setupUi(self)
        self.socket = None
        self.type = 'server'
        self.connect(self, SIGNAL('errorRequest'),
            lambda error: QMessageBox.warning(self, "Error", error))
        self.connect(self, SIGNAL('success'),
            lambda error: QMessageBox.warning(self, "Success", error))

    @pyqtSignature("QString")
    def on_findLineEdit_textEdited(self, text):
        self.__index = 0
        self.updateUi()

    @pyqtSignature("bool")
    def on_server_radioButton_clicked(self, bool):
        self.connect_pushButton.setText("Host")
        self.type = 'server'
        
    @pyqtSignature("bool")
    def on_client_radioButton_clicked(self, bool):
        self.connect_pushButton.setText("Connect")
        self.type = 'client'
        
    @pyqtSignature("")
    def on_connect_pushButton_clicked(self):
        threading.Thread(target=self.make_socket).start()
        
    def make_socket(self):
        ip = str(self.ip_lineEdit.text())
        try:
            port = int(self.port_lineEdit.text())
            if not port:
                port = 6789
        except ValueError:
            self.emit(SIGNAL("errorRequest"), "Port number is incorrect")
        if not ip:
            ip = "127.0.0.1"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if self.type == 'server':
                s.bind((ip, port))
                s.listen(2)
            else:
                s.connect((ip, port))
        except socket.error, e:
            if self.type == 'server':
                self.emit(SIGNAL("errorRequest"), "Cannot host")
            else:
                self.emit(SIGNAL("errorRequest"), "Cannot connect to the server")
            print e
            return False
        self.socket = s
        if self.type == 'server':
            self.emit(SIGNAL("success"), "Hosted %s:%d" % (ip, port))
        else:
            self.emit(SIGNAL("success"), "Connected to %s:%d" % (ip, port))
            
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = ConnectionDlg()
#    form.connect(form, SIGNAL("notfound"), nomore)
    form.show()
    app.exec_()
