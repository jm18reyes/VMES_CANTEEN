from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

import enrollUser, home, accManagement, menuManagement, orderedItems

sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../VMES.db')

sys.path.insert(0, '../UI')
import admin_ui


class Main(QtWidgets.QMainWindow, admin_ui.Ui_adminPage):
	def __init__(self):
		super(Main, self).__init__()
		self.setupUi(self)
		self.user_reg_btn.clicked.connect(self.enroll)
		self.hmpg_btn.clicked.connect(self.goHome)
		self.menu_mngBtn.clicked.connect(self.manageMenu)
		self.acc_mngBtn.clicked.connect(self.manageAccount)
		self.logout_btn.clicked.connect(self.end)
		self.totalEarn_btn.clicked.connect(self.showEarnings)

	def goHome(self):
		self.win1 = home.Main()
		self.win1.show()

	def manageMenu(self):
		self.win2 = menuManagement.Main()
		self.win2.show()

	def showEarnings(self):
		self.win3 = orderedItems.Main()
		self.win3.show()

	def enroll(self):
		self.win4 = enrollUser.Main()
		self.win4.show()

	def manageAccount(self):
		self.win5 = accManagement.Main()
		self.win5.show()
		
	def end(self):
		app = QtWidgets.QApplication.instance()
		app.closeAllWindows()
    
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	form = Main()
	form.show()
	sys.exit(app.exec_())