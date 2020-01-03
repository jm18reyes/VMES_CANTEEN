from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

import main2

sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../VMES.db')


sys.path.insert(0, '../UI')
import loginPage1, loginPage2

class Main(QtWidgets.QMainWindow, loginPage1.Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.btn1.clicked.connect(self.conti)

    def conti(self):
        user = self.blank_usr.text()
        user = user.replace(" ","")
        print(user)
        
        exist = dh.AuthUser(user)
        print(exist)
        if (exist is True):
            username = user
            self.close()
            self.newWin = main2.Main()
            self.newWin.show()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR!")
            msg.setText(user+" Not Found! Try again")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())