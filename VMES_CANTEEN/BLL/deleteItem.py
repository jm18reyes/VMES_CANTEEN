from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from functools import partial

sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../VMES.db')

sys.path.insert(0, '../UI')
import deleteItem_ui

class Main(QtWidgets.QMainWindow, deleteItem_ui.Ui_deleteMenu):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.mealTime = ""
        self.current_choice = ""
        self.idMap = {}
        self.dltMenu_bfastBtn.clicked.connect(partial(self.showMenu,"breakfast"))
        self.dltMenu_lunchBtn.clicked.connect(partial(self.showMenu,"lunch"))
        self.dltMenu_snackBtn.clicked.connect(partial(self.showMenu,"snack"))
        self.dltMenu_menuCombo.activated.connect(self.chooseThisFood)
        self.remove_item.clicked.connect(self.removeThisFood)

    def showMenu(self,mealTime):
        print("showMenu")
        self.mealTime = mealTime
        print(self.mealTime)
        self.idMap = {}
        self.dltMenu_menuCombo.clear()
        self.Menu = dh.getMenu(mealTime)
        for x in self.Menu:
            self.dltMenu_menuCombo.addItem(x[0])
            self.idMap[x[0]] = x[2]
        print("selfmap: ",self.idMap)

    def chooseThisFood(self):
        self.current_choice = ""
        self.current_choice = self.dltMenu_menuCombo.currentText()
        print(self.current_choice)
        self.food_lbl.setText(self.current_choice)

    def removeThisFood(self):
        print(self.current_choice)
        if (self.current_choice == ""):
            self.err = QMessageBox()
            self.err.setIcon(QMessageBox.Warning)
            self.err.setWindowTitle("ERROR!")
            self.err.setText("Nothing to Delete Yet!")
            x = self.err.exec()
        else:

            self.id = self.idMap[self.current_choice]
            dh.deleteFood(self.mealTime,self.id)
            self.msg = QMessageBox()
            self.msg.setWindowTitle("SUCCESS")
            self.msg.setText(self.current_choice+" has been removed!")
            z = self.msg.exec()

    def end(self):
        app = QtWidgets.QApplication.instance()
        app.closeAllWindows()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())