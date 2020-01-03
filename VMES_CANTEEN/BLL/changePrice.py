from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from functools import partial

sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../VMES.db')

sys.path.insert(0, '../UI')
import changePrice_ui

class Main(QtWidgets.QMainWindow, changePrice_ui.Ui_changePrice):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.priceMap = {}
        self.pricedMenu = ""
        self.mealTime = ""
        self.current_choice = ""
        self.newPrice = 0
        self.price = 0
        self.status = "Available"
        self.chngPrc_bfastBtn.clicked.connect(partial(self.showMenu,"breakfast"))
        self.chngPrc_lunchBtn.clicked.connect(partial(self.showMenu,"lunch"))
        self.chngPrc_snackBtn.clicked.connect(partial(self.showMenu,"snack"))
        self.save_price.clicked.connect(self.saveNewPrice)
        self.chngPrc_menuCombo.activated.connect(self.showPrice)

    def showMenu(self,mealTime):
        print("showMenu")
        self.mealTime = mealTime
        self.priceMap = {}
        self.chngPrc_menuCombo.clear()
        self.pricedMenu = dh.getMenu(mealTime)
        for x in self.pricedMenu:
            self.chngPrc_menuCombo.addItem(x[0])
            self.priceMap[x[0]] = x[1]
        print("selfmap: ",self.priceMap)

    def showPrice(self):
        self.current_choice = ""
        self.current_choice = self.chngPrc_menuCombo.currentText()
        print("current choice:",self.current_choice)
        print("showPrice")
        
        self.price = 0
        self.price = self.priceMap[self.current_choice]
        self.food_lbl.setText(str(self.current_choice))
        self.chngPrc_currentPrice.setText(str(self.price)+"0")
        print("pricelbl")

    def saveNewPrice(self):
        self.newPrice = 0
        self.newPrice = self.chngPrc_newPrice.text()
        if(self.newPrice == ""):
            self.err = QMessageBox()
            self.err.setIcon(QMessageBox.Warning)
            self.err.setWindowTitle("WARNING!")
            self.err.setText("No Changes!")
            x = self.err.exec()
        else:
            self.newPrice = float(self.newPrice) + 0.00
            print(self.newPrice)

            dh.updateMenu(self.mealTime,self.current_choice,self.newPrice,self.status)

            self.msg = QMessageBox()
            self.msg.setWindowTitle("SUCCESS")
            self.msg.setText(self.current_choice+"'s Price is Updated!")
            z = self.msg.exec()
            self.food_lbl.setText(str(None))
            self.chngPrc_currentPrice.setText(str(0)+"0")
        
    def end(self):
        app = QtWidgets.QApplication.instance()
        app.closeAllWindows()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())