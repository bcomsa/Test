# -*- coding: utf-8 -*-
#!/usr/bin/env python

from PyQt4.QtCore import (Qt, SIGNAL, pyqtSignature)
from PyQt4.QtGui import (QApplication, QDialog, QMessageBox)
import ui_chatdlg
import socket
import threading

class ChatDlg(QDialog,
        ui_chatdlg.Ui_chatdlg):

    def __init__(self, socket, parent=None):
        super(ChatDlg, self).__init__(parent)
        self.setupUi(self)
        self.socket = socket
        self.connect(self, SIGNAL('errorRequest'),
            lambda error: QMessageBox.warning(self, "Error", error))
        self.connect(self, SIGNAL('recieve'), self.total_chat_box.setPlainText)
        threading.Thread(target=self.socket_implement).start()
        
    def socket_implement(self):
        while True:
            text = str(self.socket.recv(1024))
            self.emit(SIGNAL("recieve"), text)
            
    @pyqtSignature("")
    def on_send_pushButton_clicked(self):
        text = str(self.chat_box.text())
        if text:
            self.total_chat_box.setPlainText(text)
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = ChatDlg(1)
    form.show()
    app.exec_()
