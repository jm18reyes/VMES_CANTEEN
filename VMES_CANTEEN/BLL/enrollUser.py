from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

import admin

sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../VMES.db')

sys.path.insert(0, '../UI')
import admin_ui, enroll_ui

class Main(QtWidgets.QMainWindow, enroll_ui.Ui_userRegistration):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.save_reg.clicked.connect(self.getInfo)

    def getInfo(self):
        newUser = self.username_reg.text()
        passWord = self.pass_reg.text()
        passWord2 = self.pass2_reg.text()
        job = self.job_combo.currentText()
        print(passWord)
        print(passWord2)
        print(job)
        if (newUser == ""):
            self.err = QMessageBox()
            self.err.setWindowTitle("ERROR!")
            self.err.setText("No Info Entered")
            self.err.setIcon(QMessageBox.Critical)
            x = self.err.exec_()
        elif(passWord == passWord2):
            print("equals")
            dh.AddUser(newUser,passWord,job)
            self.msg = QMessageBox()
            self.msg.setWindowTitle("ENROLLED SUCCESSFULY!")
            self.msg.setText("Thank You!")
            y = self.msg.exec()
            self.close()
        else:
            self.err2 = QMessageBox()
            self.err2.setWindowTitle("ERROR!")
            self.err2.setText("Doesn't Match! Try again")
            self.err2.setIcon(QMessageBox.Critical)
            self.z = self.err2.exec_()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())