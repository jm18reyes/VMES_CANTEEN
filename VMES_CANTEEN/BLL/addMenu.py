from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../VMES.db')

sys.path.insert(0, '../UI')
import addMenu_ui

class Main(QtWidgets.QMainWindow, addMenu_ui.Ui_addMenuItem):
	def __init__(self):
		super(Main, self).__init__()
		self.setupUi(self)
		self.food = ""
		self.price = 0
		self.mealTime = ""
		self.save_menuItem.clicked.connect(self.addNewFood)
		self.addMenu_mealCombo.activated.connect(self.whatMealTime)

	def whatMealTime(self):
		self.mealTime = ""
		self.mealTime = self.addMenu_mealCombo.currentText()
		self.chosen_meal.setText(self.mealTime)

	def addNewFood(self):
		self.mealTime = self.addMenu_mealCombo.currentText()
		self.food = self.new_menuItem.text()
		print("e",str(self.food))
		if(self.food == ""):
			self.msg = QMessageBox()
			self.msg.setIcon(QMessageBox.Warning)
			self.msg.setWindowTitle("ERROR!")
			self.msg.setText("No Information Yet!")
			x = self.msg.exec()
		else:
			
			self.price = self.add_price.text()
			self.price = float(self.price) + 0.00
			dh.AddMenu(self.mealTime,self.food,self.price)
			self.msg = QMessageBox()
			self.msg.setWindowTitle("SUCCESS")
			self.msg.setText(self.food+" has been added!")
			z = self.msg.exec()

	def end(self):
		app = QtWidgets.QApplication.instance()
		app.closeAllWindows()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())