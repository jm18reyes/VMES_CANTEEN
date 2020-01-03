from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

import main, admin, home

sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../VMES.db')

sys.path.insert(0, '../UI')
import loginPage2 

class Main(QtWidgets.QMainWindow, loginPage2.Ui_MainWindow2):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.btn_login.clicked.connect(self.login)
    
    def login(self):
        print("hey")
        password = self.blank_pass.text()
        realPass, job = dh.AuthPass()
        print("JOB="+job)
        if (password == realPass):
            print("LOGGED IN")
            app = QtWidgets.QApplication.instance()
            app.closeAllWindows()
            if (job == "admin"):
                self.Win1 = admin.Main()
                self.Win1.show()
            else:
                self.Win2 = home.Main()
                self.Win2.show()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR!")
            msg.setText("Wrong Password! Try again")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())