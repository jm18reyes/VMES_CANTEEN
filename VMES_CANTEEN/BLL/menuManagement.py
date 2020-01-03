from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

import addMenu, changePrice, deleteItem

sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../VMES.db')

sys.path.insert(0, '../UI')
import menuManagement_ui

class Main(QtWidgets.QMainWindow, menuManagement_ui.Ui_menuManagement):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.add_menu.clicked.connect(self.addFood)
        self.change_price.clicked.connect(self.changeThePrice)
        self.delete_menu.clicked.connect(self.removeFood)

    def addFood(self):
        self.win1 = addMenu.Main()
        self.win1.show()

    def changeThePrice(self):
        self.win2 = changePrice.Main()
        self.win2.show()

    def removeFood(self):
        self.win3 = deleteItem.Main()
        self.win3.show()

    def end(self):
        app = QtWidgets.QApplication.instance()
        app.closeAllWindows()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())