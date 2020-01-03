from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys


sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../VMES.db')

sys.path.insert(0, '../UI')
import accManagement_ui

class Main(QtWidgets.QMainWindow, accManagement_ui.Ui_acctManagement):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.current_choice = ""
        self.id = 0
        self.idMap = {}
        self.newPass = ""
        self.passMap = {}
        self.newJob = ""
        self.acctypeMap = {}
        self.userInfo = dh.getAllUsers()
        for x in self.userInfo:
            self.mng_userCombo.addItem(x[1])
            self.idMap[x[1]] = x[0]
            self.passMap[x[0]] = x[2]
            self.acctypeMap[x[0]] = x[3]

        self.mng_userCombo.activated.connect(self.showUserInfo)
        self.mng_deleteBtn.clicked.connect(self.deleteUser)
        self.mng_saveBtn.clicked.connect(self.saveNewInfo)
        print(self.idMap)
        print(self.passMap)
        print(self.acctypeMap)

    def showUserInfo(self):
        self.current_choice = ""
        self.current_choice = self.mng_userCombo.currentText()
        self.id = self.idMap[self.current_choice]

        self.mng_username.setText(str(self.current_choice))
        self.mng_password.setText(str(self.passMap[self.id]))
        self.mng_accType.setText(str(self.acctypeMap[self.id]))

    def saveNewInfo(self):
        self.current_choice = self.mng_userCombo.currentText()
        self.id = self.idMap[self.current_choice]
        self.newPass = self.mng_new_password.text()
        self.newJob = self.mng_new_accTypeCombo.currentText()
        print(self.newJob)
        self.up = QMessageBox()
        self.up.setWindowTitle("SUCCESS!")
        self.up.setIcon(QMessageBox.Information)
        self.up.setText(self.current_choice+" is updated!")

        if(self.mng_new_password.text() == ""):
            self.noChangeMsg = QMessageBox()
            self.noChangeMsg.setWindowTitle("ERROR!")
            self.noChangeMsg.setIcon(QMessageBox.Warning)
            self.noChangeMsg.setText("NO CHANGES!")
            if(self.newJob == "--SELECT--"):
                m = self.noChangeMsg.exec()
            else:
                self.newPass = self.mng_password.text()
                dh.updateUser(self.id,self.newPass,self.newJob)
                v = self.up.exec()
                self.end()
                self.win2 = Main()
                self.win2.show()
        else:
            dh.updateUser(self.id,self.newPass,self.newJob)
            v = self.up.exec()
            self.end()

    def deleteUser(self):
        if (self.current_choice == ""):
            self.msg = QMessageBox()
            self.msg.setWindowTitle("ERROR!")
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("There is no chosen user yet!")
            z = self.msg.exec()
        else:
            buttonReply = QMessageBox.question(self, 'NOTICE!', "Are you sure you want to delete "+ self.current_choice + "?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if (buttonReply == QMessageBox.Yes):
                delu = dh.deleteUser(self.id)   
                self.fin = QMessageBox()
                self.fin.setIcon(QMessageBox.Information)
                self.fin.setText(self.current_choice + " is deleted")
                y = self.fin.exec()
                self.end()
    def end(self):
        self.close()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())